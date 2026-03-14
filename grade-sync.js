/*  Grade Sync — auto-submit student scores to Firebase Firestore
    Loaded by quiz/test pages after firebase-config.js + Firebase SDK  */

// Initialize Firebase (only once)
if (!window._fbApp) {
    window._fbApp = firebase.initializeApp(firebaseConfig);
    window._db = firebase.firestore();
    // Sign in anonymously so students don't need Google accounts
    firebase.auth().signInAnonymously().catch(e => console.warn('Auth error:', e));
}

const db = window._db;

/**
 * Submit a score for the current student.
 * @param {string} assessmentId - e.g. "q1", "q2", "t1", "t2", "final"
 * @param {number} score - 0-100
 * @param {object} details - optional { answers: [...], total: N, correct: N }
 */
async function submitScore(assessmentId, score, details = {}) {
    // Get student name from localStorage (set by student portal login)
    const studentData = localStorage.getItem('williams_student');
    if (!studentData) { console.warn('No student logged in'); return; }
    const student = JSON.parse(studentData);
    const studentName = student.name || student.username || 'Unknown';
    const username = student.username || studentName.toLowerCase().replace(/\s+/g, '_');
    
    try {
        await db.collection('scores').doc(`${username}_${assessmentId}`).set({
            student: studentName,
            username: username,
            assessment: assessmentId,
            score: Math.round(score * 10) / 10,
            details: details,
            timestamp: firebase.firestore.FieldValue.serverTimestamp(),
            updatedAt: new Date().toISOString()
        }, { merge: true });
        
        console.log(`✅ Score submitted: ${studentName} → ${assessmentId} = ${score}`);
        return true;
    } catch (e) {
        console.error('Submit error:', e);
        // Save locally as backup
        const pending = JSON.parse(localStorage.getItem('pending_scores') || '[]');
        pending.push({ username, student: studentName, assessment: assessmentId, score, timestamp: Date.now() });
        localStorage.setItem('pending_scores', JSON.stringify(pending));
        return false;
    }
}

/**
 * Auto-grade a quiz/test by comparing inputs to answer key.
 * @param {Array} answerKey - [{id: "q1", answer: "42", type: "exact"}, ...]
 *   type: "exact" (string match), "number" (numeric ±tolerance), "choice" (multiple choice)
 * @param {string} assessmentId - e.g. "q1"
 */
function autoGradeAndSubmit(answerKey, assessmentId) {
    let correct = 0;
    const total = answerKey.length;
    const results = [];
    
    answerKey.forEach(q => {
        const el = document.getElementById(q.id);
        if (!el) return;
        const studentAnswer = (el.value || el.textContent || '').trim();
        let isCorrect = false;
        
        switch (q.type) {
            case 'number':
                const tolerance = q.tolerance || 0.01;
                const numAnswer = parseFloat(studentAnswer);
                const numCorrect = parseFloat(q.answer);
                isCorrect = !isNaN(numAnswer) && Math.abs(numAnswer - numCorrect) <= tolerance;
                break;
            case 'choice':
                isCorrect = studentAnswer.toLowerCase() === q.answer.toLowerCase();
                break;
            default: // exact
                isCorrect = studentAnswer.toLowerCase().replace(/\s+/g, ' ') === 
                           q.answer.toLowerCase().replace(/\s+/g, ' ');
        }
        
        if (isCorrect) correct++;
        results.push({ id: q.id, student: studentAnswer, correct: q.answer, isCorrect });
    });
    
    const score = total > 0 ? (correct / total) * 100 : 0;
    submitScore(assessmentId, score, { total, correct, results });
    return { score, correct, total, results };
}

/**
 * Retry any pending scores that failed to submit (offline backup).
 */
async function retryPendingScores() {
    const pending = JSON.parse(localStorage.getItem('pending_scores') || '[]');
    if (!pending.length) return;
    
    const remaining = [];
    for (const p of pending) {
        try {
            await db.collection('scores').doc(`${p.username}_${p.assessment}`).set({
                student: p.student, username: p.username, assessment: p.assessment,
                score: p.score, timestamp: firebase.firestore.FieldValue.serverTimestamp(),
                updatedAt: new Date().toISOString()
            }, { merge: true });
        } catch (e) { remaining.push(p); }
    }
    localStorage.setItem('pending_scores', JSON.stringify(remaining));
}

// Retry pending on load
firebase.auth().onAuthStateChanged(user => { if (user) retryPendingScores(); });
