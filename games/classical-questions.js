// Classical Music Math Relay — Full Question Bank (80 questions)
// Each game picks 20 at random (18 regular + 2 bonus), shuffled fresh every time.

const QUESTION_BANK = [
  // ── ADDITION & SUBTRACTION ─────────────────────────────────────
  {q:"🎻 <b>Vivaldi's Violin Strings</b><br>Vivaldi had 24 violin strings. He broke 7 during rehearsal and restrung 4 new ones. How many strings does he have now?", a:["21"], pts:10, hint:"24 − 7 + 4"},
  {q:"🎹 <b>Mozart's Sonatas</b><br>Mozart wrote 18 piano sonatas before age 20 and 9 after. He dedicated 5 to patrons. How many were not dedicated?", a:["22"], pts:10, hint:"18 + 9 − 5"},
  {q:"🎼 <b>Beethoven's Symphonies</b><br>Beethoven planned 11 symphonies but only finished 9. He sketched 3 extra movements that were never finished. How many movements remained unfinished?", a:["5"], pts:10, hint:"(11 − 9) + 3"},
  {q:"🎷 <b>Orchestra Seats</b><br>The concert hall had 48 seats in the front section and 37 in the back. 15 seats were reserved for VIPs. How many seats were available to the public?", a:["70"], pts:10, hint:"48 + 37 − 15"},
  {q:"🎺 <b>Trumpet Players</b><br>An orchestra had 52 musicians. 19 left for intermission, then 8 returned early. How many musicians were on stage?", a:["41"], pts:10, hint:"52 − 19 + 8"},
  {q:"🎵 <b>Sheet Music Pages</b><br>A conductor had 64 pages of sheet music. She marked 27 pages for review. How many pages were not marked?", a:["37"], pts:10, hint:"64 − 27"},

  // ── MULTIPLICATION ─────────────────────────────────────────────
  {q:"🎻 <b>String Quartets</b><br>A music school formed 9 string quartets with 4 players each. How many string players in total?", a:["36"], pts:10, hint:"9 × 4"},
  {q:"🎼 <b>Measures per Movement</b><br>A symphony has 8 movements with 12 measures each. How many measures in all?", a:["96"], pts:10, hint:"8 × 12"},
  {q:"🎹 <b>Piano Keys Practice</b><br>A pianist practiced 12 scales with 3 variations each. How many scale variations total?", a:["36"], pts:10, hint:"12 × 3"},
  {q:"🏛️ <b>Concert Hall Rows</b><br>The grand hall has 15 rows of seats with 11 seats per row. How many seats total?", a:["165"], pts:10, hint:"15 × 11"},
  {q:"🎶 <b>Bach's Preludes</b><br>Bach wrote preludes in 9 groups of 14. How many preludes total?", a:["126"], pts:10, hint:"9 × 14"},
  {q:"🎵 <b>Music Stands</b><br>Each of 7 orchestra sections has 12 music stands. How many stands in all?", a:["84"], pts:10, hint:"7 × 12"},

  // ── DIVISION ───────────────────────────────────────────────────
  {q:"🎻 <b>Dividing Sheet Music</b><br>72 pages of sheet music divided equally among 9 musicians. How many pages each?", a:["8"], pts:10, hint:"72 ÷ 9"},
  {q:"🎺 <b>Orchestra Sections</b><br>240 musicians organized into 8 equal sections. How many per section?", a:["30"], pts:10, hint:"240 ÷ 8"},
  {q:"🎼 <b>Sharing the Program</b><br>84 concert programs shared equally among 4 classes. How many programs per class?", a:["21"], pts:10, hint:"84 ÷ 4"},
  {q:"🎹 <b>Piano Exercises</b><br>126 exercises divided into sets of 7. How many sets?", a:["18"], pts:10, hint:"126 ÷ 7"},
  {q:"🎵 <b>Rehearsal Groups</b><br>48 choir members split into groups of 6. How many groups?", a:["8"], pts:10, hint:"48 ÷ 6"},

  // ── FRACTIONS ──────────────────────────────────────────────────
  {q:"🎶 <b>Fraction Review</b><br>There are 20 instruments in the orchestra. ¾ are string instruments. How many string instruments?", a:["15"], pts:10, hint:"20 × 3 ÷ 4"},
  {q:"🎹 <b>Chopin's Nocturnes</b><br>Chopin composed 24 nocturnes. ¾ were dedicated to women. How many were dedicated?", a:["18"], pts:10, hint:"24 × 3 ÷ 4"},
  {q:"🎻 <b>Violin Strings</b><br>The string section had 40 violins. Half were played by left-handed musicians. How many?", a:["20"], pts:10, hint:"40 ÷ 2"},
  {q:"🎼 <b>Completed Scores</b><br>Brahms started 36 compositions. He completed ⅔ of them. How many did he complete?", a:["24"], pts:10, hint:"36 × 2 ÷ 3"},
  {q:"🎵 <b>The Choir</b><br>A choir had 60 singers. ¼ were sopranos. How many sopranos?", a:["15"], pts:10, hint:"60 ÷ 4"},
  {q:"🎺 <b>Rehearsal Time</b><br>The orchestra rehearsed 80 hours total. They spent ⅜ of the time on concertos. How many hours on concertos?", a:["30"], pts:10, hint:"80 × 3 ÷ 8"},

  // ── PERCENTAGES ────────────────────────────────────────────────
  {q:"💯 <b>Percentage Review</b><br>80 concert tickets were sold. 25% were student discounts. How many student tickets?", a:["20"], pts:10, hint:"80 ÷ 4"},
  {q:"🎟️ <b>Sold-Out Concert</b><br>The concert hall held 200 guests. 15% were music students. How many were music students?", a:["30"], pts:10, hint:"200 × 0.15"},
  {q:"🎻 <b>String Section</b><br>An orchestra has 500 musicians. 40% are in the string section. How many string players?", a:["200"], pts:10, hint:"500 × 0.40"},
  {q:"🎼 <b>Completed Pieces</b><br>A composer planned 300 pieces. He completed 30%. How many did he complete?", a:["90"], pts:10, hint:"300 × 0.30"},
  {q:"🎹 <b>Piano Students</b><br>A conservatory has 120 students. 75% study piano. How many piano students?", a:["90"], pts:10, hint:"120 × 0.75"},

  // ── PERIMETER ──────────────────────────────────────────────────
  {q:"📐 <b>Perimeter Review</b><br>A rehearsal room is 15 feet long and 10 feet wide. What is its perimeter?", a:["50","50 feet","50ft"], pts:10, hint:"2 × (15 + 10)"},
  {q:"🏛️ <b>The Concert Stage</b><br>The stage is 40 ft long and 25 ft wide. How many feet of trim around the edge?", a:["130","130 feet","130ft"], pts:10, hint:"2 × (40 + 25)"},
  {q:"🎵 <b>The Practice Room</b><br>A square practice room has sides of 8 feet each. What is the perimeter?", a:["32","32 feet","32ft"], pts:10, hint:"4 × 8"},
  {q:"🎻 <b>The Recital Hall</b><br>A recital hall is 22 meters long and 9 meters wide. What is its perimeter?", a:["62","62 meters","62m"], pts:10, hint:"2 × (22 + 9)"},
  {q:"🎼 <b>The Orchestra Pit</b><br>The orchestra pit is 35 ft long and 20 ft wide. How long is the railing around it?", a:["110","110 feet","110ft"], pts:10, hint:"2 × (35 + 20)"},

  // ── AREA ───────────────────────────────────────────────────────
  {q:"📏 <b>Area Review</b><br>A square music stand platform has sides of 9 feet. What is its area?", a:["81","81 sq ft","81 square feet"], pts:10, hint:"9 × 9"},
  {q:"🎹 <b>The Grand Ballroom Stage</b><br>A perfect square stage has each side 12 feet. What is the area?", a:["144","144 sq ft","144 square feet"], pts:10, hint:"12 × 12"},
  {q:"🏛️ <b>The Orchestra Hall</b><br>The hall is 18 feet long and 14 feet wide. What is its area?", a:["252","252 sq ft","252 square feet"], pts:10, hint:"18 × 14"},
  {q:"🎶 <b>The Outdoor Stage</b><br>An outdoor stage is 25 meters long and 16 meters wide. What is its area?", a:["400","400 sq m","400 square meters"], pts:10, hint:"25 × 16"},
  {q:"🎵 <b>The Green Room</b><br>The green room is 11 ft by 9 ft. What is its area?", a:["99","99 sq ft","99 square feet"], pts:10, hint:"11 × 9"},

  // ── UNIT CONVERSION ────────────────────────────────────────────
  {q:"📏 <b>Unit Conversion</b><br>A double bass is 3 feet tall. How many inches? (1 ft = 12 in)", a:["36","36 inches"], pts:10, hint:"3 × 12"},
  {q:"🎻 <b>The Violin Bow</b><br>A violin bow is 9 inches shorter than a cello bow. The cello bow is 1 foot long. How long is the violin bow (in inches)?", a:["3","3 inches"], pts:10, hint:"12 − 9"},
  {q:"🎺 <b>The Trumpet Length</b><br>A trumpet is 2 feet long when uncoiled. How many inches is that?", a:["24","24 inches"], pts:10, hint:"2 × 12"},
  {q:"🚗 <b>Tour Distance</b><br>The orchestra toured 5 miles to the venue. How many feet is that? (1 mile = 5,280 feet)", a:["26400","26,400","26400 feet"], pts:10, hint:"5 × 5,280"},
  {q:"🕰️ <b>The Long Tour</b><br>The orchestra's European tour lasted 3 years. How many months is that?", a:["36","36 months"], pts:10, hint:"3 × 12"},
  {q:"⏱️ <b>Symphony Duration</b><br>Beethoven's 9th lasts 2 hours. How many minutes is that?", a:["120","120 minutes"], pts:10, hint:"2 × 60"},

  // ── TIME ───────────────────────────────────────────────────────
  {q:"⏰ <b>Time Review</b><br>A concert starts at 2:15 PM and runs 1 hour 45 minutes. What time does it end?", a:["4:00","4:00 pm","4 pm","4:00 PM"], pts:10, hint:"2:15 + 1:45"},
  {q:"🌅 <b>Morning Rehearsal</b><br>Rehearsal began at 9:30 AM and lasted 2 hours 15 minutes. What time did it end?", a:["11:45","11:45 am","11:45 AM"], pts:10, hint:"9:30 + 2:15"},
  {q:"🌙 <b>Evening Performance</b><br>The evening concert started at 6:00 PM and ran 3 hours 30 minutes. What time did it end?", a:["9:30","9:30 pm","9:30 PM"], pts:10, hint:"6:00 + 3:30"},
  {q:"🏛️ <b>The Master Class</b><br>The master class started at 10:45 AM and ended at 1:15 PM. How long did it last?", a:["2 hours 30 minutes","2.5 hours","2h 30m","150 minutes"], pts:10, hint:"1:15 PM − 10:45 AM"},

  // ── MULTI-STEP ─────────────────────────────────────────────────
  {q:"🔢 <b>Multi-Step Problem</b><br>5 music stands. Each stand holds 4 folders. Each folder has 12 pages. Total pages?", a:["240"], pts:10, hint:"5 × 4 × 12"},
  {q:"🎼 <b>Programs for the Concert</b><br>6 sections of the hall, each needing 4 ushers, each carrying 8 programs. How many programs total?", a:["192"], pts:10, hint:"6 × 4 × 8"},
  {q:"🎹 <b>Recital Supplies</b><br>7 recitals each need 5 programs. Each program has 9 pages. How many pages total?", a:["315"], pts:10, hint:"7 × 5 × 9"},
  {q:"🎻 <b>String Section</b><br>The string section has 4 rows of musicians. Each row has 6 players. Each player uses 3 bow strings per season. How many bow strings total?", a:["72"], pts:10, hint:"4 × 6 × 3"},
  {q:"🏛️ <b>The Archive Room</b><br>The music library has 3 archive rooms. Each room has 8 shelves. Each shelf holds 25 scores. How many scores total?", a:["600"], pts:10, hint:"3 × 8 × 25"},

  // ── DIVISION WITH REMAINDER ────────────────────────────────────
  {q:"🔢 <b>Division Review</b><br>46 choir members split into groups of 5. How many complete groups, and how many singers left over?", a:["9 groups, 1 left over","9 groups 1 left over","9r1","9 remainder 1"], pts:10, hint:"46 ÷ 5"},
  {q:"🎵 <b>Programs in Stacks</b><br>50 programs stacked in piles of 7. How many full piles, and how many programs left over?", a:["7 piles, 1 left over","7r1","7 remainder 1","7 piles 1 left"], pts:10, hint:"50 ÷ 7"},
  {q:"🎻 <b>Bow Bundles</b><br>75 violin bows bundled in groups of 8. How many full bundles, and how many bows left over?", a:["9 bundles, 3 left over","9r3","9 remainder 3","9 bundles 3 left"], pts:10, hint:"75 ÷ 8"},

  // ── WORD PROBLEMS (MIXED) ──────────────────────────────────────
  {q:"🎹 <b>Practicing Scales</b><br>A pianist practices 12 scales per hour. How many scales in 3 hours?", a:["36","36 scales"], pts:10, hint:"12 × 3"},
  {q:"🚂 <b>Tour by Train</b><br>The orchestra travels 15 miles per hour by train. How far in 4 hours?", a:["60","60 miles"], pts:10, hint:"15 × 4"},
  {q:"🎟️ <b>Concert Tickets</b><br>Mozart bought a program for 45 coins and a seat cushion for 78 coins. He paid with 150 coins. How much change did he get?", a:["27","27 coins"], pts:10, hint:"150 − 45 − 78"},
  {q:"🎻 <b>Violin Practice</b><br>A violinist practiced 12 pieces each day for 6 days. She performed 58 of them perfectly. How many still needed work?", a:["14"], pts:10, hint:"(12 × 6) − 58"},
  {q:"🍞 <b>Feeding the Orchestra</b><br>Each musician eats 3 sandwiches at intermission. There are 24 musicians. How many sandwiches for 5 intermissions?", a:["360"], pts:10, hint:"3 × 24 × 5"},
  {q:"🎵 <b>The Metronome</b><br>A metronome has 2 batteries. Each battery lasts 45 hours. The musician has already used 12 hours. How many hours remain?", a:["78"], pts:10, hint:"(2 × 45) − 12"},
  {q:"🎼 <b>Conducting Tempo</b><br>A conductor beats 8 measures per minute in adagio. How many measures in 15 minutes?", a:["120"], pts:10, hint:"8 × 15"},
  {q:"🏛️ <b>Balcony Stairs</b><br>Each balcony level in the concert hall has 36 steps. There are 4 levels. How many steps total?", a:["144"], pts:10, hint:"36 × 4"},
  {q:"⭐ <b>Stars on the Program</b><br>The program listed 6 groups of 13 featured performers. How many featured performers total?", a:["78"], pts:10, hint:"6 × 13"},
  {q:"🎺 <b>Instrument Inventory</b><br>The school had 96 brass instruments. 32 were loaned to new students. Then 14 more arrived from storage. How many instruments now?", a:["78"], pts:10, hint:"96 − 32 + 14"},

  // ── BONUS QUESTIONS (pts:15) ───────────────────────────────────
  {q:"🎹 <b>BONUS ⭐ — Beethoven's Archives</b><br>Shelf 1: 9 rows × 12 scores. Shelf 2: 6 rows × 15 scores. Shelf 3: 4 rows × 18 scores. Each score has 8 pages. Total pages?", a:["1488"], pts:15, hint:"(9×12 + 6×15 + 4×18) × 8 = 270 × 8"},
  {q:"🎻 <b>BONUS ⭐ — The Orchestra Auction</b><br>8 violins @ 15 coins, 6 cellos @ 24, 12 flutes @ 30, 4 harps @ 55, 9 trumpets @ 20. Grand total?", a:["1258","1,258"], pts:15, hint:"(8×15)+(6×24)+(12×30)+(4×55)+(9×20)"},
  {q:"🚂 <b>BONUS ⭐ — The Grand Tour</b><br>The orchestra toured 3 legs: 120 miles, 85 miles, 97 miles. They returned halfway home. Total distance traveled?", a:["453","453 miles"], pts:15, hint:"120+85+97 = 302; return = 302÷2 = 151; 302+151"},
  {q:"🏛️ <b>BONUS ⭐ — Concert Hall Renovation</b><br>The hall has 5 wings. Each wing has 4 floors. Each floor has 8 rooms. Each room needs 3 windows. How many windows total?", a:["480"], pts:15, hint:"5 × 4 × 8 × 3"},
  {q:"💰 <b>BONUS ⭐ — The Music Fund</b><br>The fund has 4 accounts. Account 1: 125 coins. Account 2: 250 coins. Account 3: double account 1. Account 4: half of account 2. Total coins?", a:["625"], pts:15, hint:"125 + 250 + (2×125) + (250÷2)"},
  {q:"🎼 <b>BONUS ⭐ — Festival Supplies</b><br>A music festival has 6 stages × 24 performers each. Each performer carries 3 instruments and 2 music folders. How many total items carried?", a:["720"], pts:15, hint:"6×24 = 144 performers; 144 × (3+2) = 144 × 5"}
];

// Separate regular and bonus questions
const REGULAR_Q = QUESTION_BANK.filter(function(q){ return q.pts === 10; });
const BONUS_Q = QUESTION_BANK.filter(function(q){ return q.pts === 15; });

// Fisher-Yates shuffle
function shuffleArray(arr) {
  var a = arr.slice();
  for (var i = a.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var tmp = a[i]; a[i] = a[j]; a[j] = tmp;
  }
  return a;
}

// Pick 18 regular + 2 bonus, shuffled
function buildGameQuestions() {
  var reg = shuffleArray(REGULAR_Q).slice(0, 18);
  var bon = shuffleArray(BONUS_Q).slice(0, 2);
  return reg.concat(bon);
}
