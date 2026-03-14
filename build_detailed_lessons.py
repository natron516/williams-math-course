#!/usr/bin/env python3
"""
Build detailed lesson plans with expandable teaching guides,
worked examples, common mistakes, discussion prompts, and whiteboard scripts.
"""

# Teaching detail for each session
TEACHING = {
1: {
"concepts": """<h4>What Are Angles?</h4>
<p>An angle is formed when two <strong>rays</strong> (straight lines that go on forever in one direction) share a common starting point called the <strong>vertex</strong>. We measure how "open" the angle is in <strong>degrees (°)</strong>.</p>

<h4>Types of Angles</h4>
<div class="concept-grid">
<div class="concept-card blue"><div class="concept-icon">📐</div><strong>Acute Angle</strong><br>Less than 90°<br><em>Think: "a cute little angle"</em></div>
<div class="concept-card green"><div class="concept-icon">📏</div><strong>Right Angle</strong><br>Exactly 90°<br><em>The corner of a book</em></div>
<div class="concept-card orange"><div class="concept-icon">📐</div><strong>Obtuse Angle</strong><br>Between 90° and 180°<br><em>A reclining chair</em></div>
<div class="concept-card red"><div class="concept-icon">➡️</div><strong>Straight Angle</strong><br>Exactly 180°<br><em>A flat line</em></div>
</div>

<h4>How to Measure with a Protractor</h4>
<ol>
<li>Place the center point of the protractor on the <strong>vertex</strong> of the angle</li>
<li>Line up one ray with the <strong>0° line</strong> (baseline)</li>
<li>Read where the other ray crosses the protractor</li>
<li>Use the correct scale! (inner vs outer numbers)</li>
</ol>
<p class="tip">💡 <strong>Pro tip:</strong> If the angle looks smaller than a book corner, it's acute. Use the scale that gives a number less than 90.</p>""",

"examples": """<div class="example-box">
<div class="example-title">Example 1: Classify the angle</div>
<p><strong>Given:</strong> An angle measures 135°</p>
<p><strong>Step 1:</strong> Is it less than 90°? No → not acute</p>
<p><strong>Step 2:</strong> Is it exactly 90°? No → not right</p>
<p><strong>Step 3:</strong> Is it between 90° and 180°? YES → <strong>Obtuse</strong> ✅</p>
</div>

<div class="example-box">
<div class="example-title">Example 2: Pizza Slice Angle</div>
<p><strong>Given:</strong> A pizza is cut into 6 equal slices</p>
<p><strong>Step 1:</strong> Full circle = 360°</p>
<p><strong>Step 2:</strong> 360° ÷ 6 slices = <strong>60° per slice</strong></p>
<p><strong>Step 3:</strong> 60° is less than 90° → each slice makes an <strong>acute angle</strong></p>
</div>

<div class="example-box">
<div class="example-title">Example 3: Clock Angles</div>
<p><strong>Given:</strong> What angle do clock hands make at 3:00?</p>
<p><strong>Step 1:</strong> The hour hand is at 3, the minute hand is at 12</p>
<p><strong>Step 2:</strong> Each hour mark = 360° ÷ 12 = 30°</p>
<p><strong>Step 3:</strong> 3 hour marks × 30° = <strong>90°</strong> → <strong>Right angle!</strong></p>
<p class="tip">💡 Use this method for ANY clock time: count the hour marks between the hands × 30°</p>
</div>""",

"mistakes": """<div class="mistake-card">
<div class="mistake-wrong">❌ Reading the wrong protractor scale (inner vs outer)</div>
<div class="mistake-fix">✅ Fix: Check if the angle LOOKS acute or obtuse first, then pick the matching number</div>
</div>
<div class="mistake-card">
<div class="mistake-wrong">❌ Confusing vertex with the side of the angle</div>
<div class="mistake-fix">✅ Fix: The vertex is the POINT where two lines meet — it's always the corner</div>
</div>
<div class="mistake-card">
<div class="mistake-wrong">❌ Thinking a straight line isn't an angle</div>
<div class="mistake-fix">✅ Fix: A straight line IS an angle — it's 180°. The rays just happen to point opposite directions</div>
</div>""",

"whiteboard": """<h4>🖊️ Whiteboard Script (follow this during Direct Instruction)</h4>
<ol>
<li><strong>Draw</strong> a right angle on the board. "This is our reference — 90°, like the corner of the board."</li>
<li><strong>Draw</strong> an acute angle. "This is LESS open than 90°. Remember: A-CUTE, like a cute little angle."</li>
<li><strong>Draw</strong> an obtuse angle. "This is MORE open than 90°. Think of someone slouching back in their chair."</li>
<li><strong>Draw</strong> a straight angle. "Open it ALL the way — 180°. It looks like a straight line, but it IS an angle."</li>
<li><strong>Real objects:</strong> Hold up a book (right angle), scissors at different widths (acute → obtuse), a ruler (straight)</li>
<li><strong>Interactive:</strong> "Everyone make a right angle with your arms. Now acute. Now obtuse. Now straight!"</li>
</ol>""",

"discussion": """<div class="discussion-q">🗣️ "Can you have an angle bigger than 180°? What would that look like?"</div>
<div class="discussion-q">🗣️ "Why do you think there are 360° in a circle and not 100?"</div>
<div class="discussion-q">🗣️ "Where do you see right angles in this classroom right now?"</div>
<div class="discussion-q">🗣️ "If a door is open halfway, about how many degrees is that?"</div>""",
},

2: {
"concepts": """<h4>Complementary Angles</h4>
<p>Two angles that <strong>add up to 90°</strong> (they "complete" a right angle)</p>
<div class="concept-card blue" style="display:inline-block;margin:8px;">
<strong>30° + 60° = 90°</strong> ✅ Complementary<br>
<em>Think: "C" comes before "S" → Complementary = Corner (90°)</em>
</div>

<h4>Supplementary Angles</h4>
<p>Two angles that <strong>add up to 180°</strong> (they make a straight line)</p>
<div class="concept-card orange" style="display:inline-block;margin:8px;">
<strong>120° + 60° = 180°</strong> ✅ Supplementary<br>
<em>Think: "S" comes after "C" → Supplementary = Straight line (180°)</em>
</div>

<h4>Vertical Angles</h4>
<p>When two lines cross, they form 4 angles. The angles <strong>across from each other</strong> are always equal.</p>
<p class="tip">💡 <strong>Memory trick:</strong> "Vertical" is misleading — they're NOT up/down. They're ACROSS from each other at the intersection, like an X.</p>

<h4>Finding Unknown Angles</h4>
<ol>
<li><strong>Complementary:</strong> unknown = 90° − known angle</li>
<li><strong>Supplementary:</strong> unknown = 180° − known angle</li>
<li><strong>Vertical:</strong> the unknown angle equals the one across from it</li>
</ol>""",

"examples": """<div class="example-box">
<div class="example-title">Example 1: Find the complement</div>
<p><strong>Given:</strong> One angle is 35°. Find its complement.</p>
<p><strong>Solution:</strong> 90° − 35° = <strong>55°</strong></p>
<p><strong>Check:</strong> 35° + 55° = 90° ✅</p>
</div>

<div class="example-box">
<div class="example-title">Example 2: Find the supplement</div>
<p><strong>Given:</strong> One angle is 118°. Find its supplement.</p>
<p><strong>Solution:</strong> 180° − 118° = <strong>62°</strong></p>
<p><strong>Check:</strong> 118° + 62° = 180° ✅</p>
</div>

<div class="example-box">
<div class="example-title">Example 3: Intersecting Lines</div>
<p><strong>Given:</strong> Two lines cross. One angle is 72°. Find all other angles.</p>
<p><strong>Step 1:</strong> Vertical angle (across) = 72°</p>
<p><strong>Step 2:</strong> Adjacent angle = 180° − 72° = 108° (supplementary)</p>
<p><strong>Step 3:</strong> Last angle (across from 108°) = 108°</p>
<p><strong>Answer:</strong> 72°, 108°, 72°, 108° — notice they alternate! ✅</p>
</div>

<div class="example-box">
<div class="example-title">Example 4: Word Problem — Roof Angles</div>
<p><strong>Given:</strong> A roof peak makes a 140° angle. The two sides of the roof make equal angles with the horizontal. Find each angle.</p>
<p><strong>Step 1:</strong> The three angles at the peak add to 180° (straight line)</p>
<p><strong>Step 2:</strong> 180° − 140° = 40° left for both sides</p>
<p><strong>Step 3:</strong> 40° ÷ 2 = <strong>20° each side</strong></p>
</div>""",

"mistakes": """<div class="mistake-card">
<div class="mistake-wrong">❌ Mixing up complementary (90°) and supplementary (180°)</div>
<div class="mistake-fix">✅ Fix: <strong>C</strong>omplementary = <strong>C</strong>orner (90°), <strong>S</strong>upplementary = <strong>S</strong>traight (180°)</div>
</div>
<div class="mistake-card">
<div class="mistake-wrong">❌ Thinking vertical angles are the ones next to each other</div>
<div class="mistake-fix">✅ Fix: Vertical angles are ACROSS — draw an X and color the matching pairs</div>
</div>
<div class="mistake-card">
<div class="mistake-wrong">❌ Subtracting from the wrong total (using 180 when they mean 90)</div>
<div class="mistake-fix">✅ Fix: Read the problem carefully. "Complement" → 90°. "Supplement" → 180°.</div>
</div>""",

"whiteboard": """<h4>🖊️ Whiteboard Script</h4>
<ol>
<li><strong>Draw</strong> a right angle. "These two angles COMPLEMENT each other to make 90°. If one is 50°, the other is...?" (let students answer: 40°)</li>
<li><strong>Draw</strong> a straight line with an angle. "These SUPPLEMENT each other to make 180°. If one is 130°, the other is...?" (50°)</li>
<li><strong>Draw</strong> two intersecting lines. Label one angle 65°. "Who can fill in the other three?" (Have a student come up)</li>
<li><strong>Memory device:</strong> Write on board: <strong>C = Corner = 90° | S = Straight = 180°</strong></li>
<li><strong>Quick check:</strong> "Thumbs up if complementary, thumbs down if supplementary: 45° and 45°? (up!) 100° and 80°? (down!) 60° and 120°? (down!)"</li>
</ol>""",

"discussion": """<div class="discussion-q">🗣️ "Can two obtuse angles be supplementary? Why or why not?"</div>
<div class="discussion-q">🗣️ "Can an angle be its own complement? What would that angle be?"</div>
<div class="discussion-q">🗣️ "Look at the corner where two walls meet the ceiling. How many right angles do you see?"</div>""",
},

3: {
"concepts": """<h4>Classifying Triangles by Sides</h4>
<div class="concept-grid">
<div class="concept-card blue"><div class="concept-icon">🔺</div><strong>Equilateral</strong><br>All 3 sides equal<br>All 3 angles = 60°<br><em>"Equal-lateral"</em></div>
<div class="concept-card green"><div class="concept-icon">🔺</div><strong>Isosceles</strong><br>2 sides equal<br>2 angles equal<br><em>"I-SOS-celes: 2 matching sides"</em></div>
<div class="concept-card orange"><div class="concept-icon">🔺</div><strong>Scalene</strong><br>No sides equal<br>No angles equal<br><em>"All different, all 'scale'-y"</em></div>
</div>

<h4>Classifying Triangles by Angles</h4>
<div class="concept-grid">
<div class="concept-card blue"><div class="concept-icon">📐</div><strong>Acute Triangle</strong><br>ALL angles < 90°</div>
<div class="concept-card green"><div class="concept-icon">📏</div><strong>Right Triangle</strong><br>ONE angle = 90°</div>
<div class="concept-card orange"><div class="concept-icon">📐</div><strong>Obtuse Triangle</strong><br>ONE angle > 90°</div>
</div>

<h4>Key Rule: Triangle Angle Sum</h4>
<div class="concept-card red" style="display:inline-block;margin:8px;font-size:1.1em;">
<strong>All 3 angles in ANY triangle add up to 180°</strong>
</div>
<p>This means: if you know 2 angles, you can ALWAYS find the third!</p>

<h4>Polygons</h4>
<p>A <strong>polygon</strong> is any closed shape with straight sides. The interior angle sum depends on the number of sides:</p>
<table class="simple-table">
<tr><th>Shape</th><th>Sides</th><th>Angle Sum</th><th>Formula</th></tr>
<tr><td>Triangle</td><td>3</td><td>180°</td><td rowspan="5">(n − 2) × 180°</td></tr>
<tr><td>Quadrilateral</td><td>4</td><td>360°</td></tr>
<tr><td>Pentagon</td><td>5</td><td>540°</td></tr>
<tr><td>Hexagon</td><td>6</td><td>720°</td></tr>
<tr><td>Octagon</td><td>8</td><td>1,080°</td></tr>
</table>""",

"examples": """<div class="example-box">
<div class="example-title">Example 1: Find the missing angle</div>
<p><strong>Given:</strong> A triangle has angles of 52° and 73°</p>
<p><strong>Step 1:</strong> 52° + 73° = 125°</p>
<p><strong>Step 2:</strong> 180° − 125° = <strong>55°</strong></p>
<p><strong>Check:</strong> 52° + 73° + 55° = 180° ✅</p>
</div>

<div class="example-box">
<div class="example-title">Example 2: Classify by sides AND angles</div>
<p><strong>Given:</strong> Triangle with sides 5 cm, 5 cm, 8 cm and angles 40°, 40°, 100°</p>
<p><strong>By sides:</strong> Two sides equal → <strong>Isosceles</strong></p>
<p><strong>By angles:</strong> One angle > 90° → <strong>Obtuse</strong></p>
<p><strong>Full classification:</strong> <strong>Obtuse Isosceles Triangle</strong></p>
</div>

<div class="example-box">
<div class="example-title">Example 3: Regular polygon angle</div>
<p><strong>Given:</strong> Find each angle in a regular hexagon</p>
<p><strong>Step 1:</strong> Angle sum = (6 − 2) × 180° = 4 × 180° = 720°</p>
<p><strong>Step 2:</strong> Regular means all angles equal: 720° ÷ 6 = <strong>120°</strong></p>
</div>""",

"mistakes": """<div class="mistake-card">
<div class="mistake-wrong">❌ Thinking "right triangle" means the angles point right</div>
<div class="mistake-fix">✅ Fix: "Right" means it has a 90° angle (a RIGHT angle), not a direction</div>
</div>
<div class="mistake-card">
<div class="mistake-wrong">❌ Forgetting that triangle angles MUST add to 180°</div>
<div class="mistake-fix">✅ Fix: Always check your answer: do all three angles sum to 180°?</div>
</div>
<div class="mistake-card">
<div class="mistake-wrong">❌ Confusing sides classification with angles classification</div>
<div class="mistake-fix">✅ Fix: A triangle gets TWO labels — one for sides (equilateral/isosceles/scalene) and one for angles (acute/right/obtuse)</div>
</div>""",

"whiteboard": """<h4>🖊️ Whiteboard Script</h4>
<ol>
<li><strong>Draw</strong> the three side types: equilateral (mark equal sides with tick marks), isosceles (two ticks), scalene (no ticks). "Count the matching sides!"</li>
<li><strong>Draw</strong> the three angle types: mark the right angle with a square, label the obtuse angle with an arc</li>
<li><strong>Key moment:</strong> "Can a triangle have TWO right angles? Let's try: 90° + 90° = 180°... no room for the third angle! Impossible."</li>
<li><strong>Polygon formula:</strong> Draw a pentagon. "How many triangles can you make from one corner?" (3 triangles) "So the angle sum is 3 × 180° = 540°"</li>
<li><strong>Activity:</strong> Students make triangles with their arms in pairs, classify them</li>
</ol>""",

"discussion": """<div class="discussion-q">🗣️ "Can a triangle be both right AND equilateral? Why not?"</div>
<div class="discussion-q">🗣️ "What's the maximum number of obtuse angles a triangle can have?"</div>
<div class="discussion-q">🗣️ "Why are stop signs octagons and not circles?"</div>""",
},

4: {
"concepts": """<h4>What Is Perimeter?</h4>
<p>Perimeter is the <strong>total distance around the outside</strong> of a shape. Imagine an ant walking along every edge — the distance it walks is the perimeter.</p>

<h4>Formulas</h4>
<div class="concept-grid">
<div class="concept-card blue"><strong>Rectangle</strong><br>P = 2l + 2w<br><em>or P = 2(l + w)</em></div>
<div class="concept-card green"><strong>Square</strong><br>P = 4s<br><em>(all sides equal)</em></div>
<div class="concept-card orange"><strong>Triangle</strong><br>P = a + b + c<br><em>(add all 3 sides)</em></div>
<div class="concept-card red"><strong>Regular Polygon</strong><br>P = n × s<br><em>(n sides, each length s)</em></div>
</div>
<p class="tip">💡 <strong>For irregular shapes:</strong> Just add up ALL the side lengths. There's no shortcut — measure every side!</p>

<h4>Units Matter!</h4>
<p>Perimeter is a <strong>distance</strong> (one-dimensional), so the answer is in <strong>regular units</strong>: feet, meters, inches — NOT square feet (that's area).</p>""",

"examples": """<div class="example-box">
<div class="example-title">Example 1: Fencing a Garden</div>
<p><strong>Given:</strong> Rectangular garden, 15 ft × 8 ft. Fencing costs $6.50/foot.</p>
<p><strong>Step 1:</strong> P = 2(15) + 2(8) = 30 + 16 = <strong>46 feet</strong></p>
<p><strong>Step 2:</strong> Cost = 46 × $6.50 = <strong>$299.00</strong></p>
</div>

<div class="example-box">
<div class="example-title">Example 2: Baseboard Around a Room</div>
<p><strong>Given:</strong> Room is 12 ft × 10 ft. One door (3 ft wide). Baseboard costs $2.25/foot.</p>
<p><strong>Step 1:</strong> P = 2(12) + 2(10) = 44 feet</p>
<p><strong>Step 2:</strong> Subtract door: 44 − 3 = <strong>41 feet of baseboard</strong></p>
<p><strong>Step 3:</strong> Cost = 41 × $2.25 = <strong>$92.25</strong></p>
</div>

<div class="example-box">
<div class="example-title">Example 3: Missing Side Length</div>
<p><strong>Given:</strong> Rectangle with perimeter = 54 cm, width = 11 cm</p>
<p><strong>Step 1:</strong> P = 2l + 2w → 54 = 2l + 2(11) → 54 = 2l + 22</p>
<p><strong>Step 2:</strong> 2l = 54 − 22 = 32 → l = <strong>16 cm</strong></p>
</div>""",

"mistakes": """<div class="mistake-card">
<div class="mistake-wrong">❌ Writing "square feet" for perimeter</div>
<div class="mistake-fix">✅ Fix: Perimeter = distance = regular units (feet, meters). Area uses square units.</div>
</div>
<div class="mistake-card">
<div class="mistake-wrong">❌ Forgetting to count all sides (especially on rectangles — only adding 2 sides)</div>
<div class="mistake-fix">✅ Fix: A rectangle has 4 sides! P = l + w only gives you HALF. Multiply by 2!</div>
</div>
<div class="mistake-card">
<div class="mistake-wrong">❌ On irregular shapes, missing a side</div>
<div class="mistake-fix">✅ Fix: Put your finger on one corner and trace ALL the way around, counting each side</div>
</div>""",

"whiteboard": """<h4>🖊️ Whiteboard Script</h4>
<ol>
<li><strong>Draw</strong> a rectangle, label 12 ft and 8 ft. "How far would an ant walk around this?" Count: 12 + 8 + 12 + 8 = 40 ft</li>
<li><strong>Shortcut:</strong> "Since opposite sides are equal: 2(12) + 2(8) = 40 ft — same answer, faster!"</li>
<li><strong>Real-world hook:</strong> "Fencing costs $5/foot. What's the cost?" 40 × $5 = $200</li>
<li><strong>Garden challenge:</strong> "You have 40 feet of fencing. What rectangles can you make?" (Let students brainstorm: 1×19, 5×15, 10×10...)</li>
<li><strong>Tricky one:</strong> Draw an L-shape. "You MUST find EVERY side length — even the ones not labeled." Show how to figure out unlabeled sides.</li>
</ol>""",

"discussion": """<div class="discussion-q">🗣️ "You have 40 feet of fencing. What shape rectangle gives the MOST area inside?" (Spoiler: a square!)</div>
<div class="discussion-q">🗣️ "Why do fencing companies charge per foot of fencing, not by the area enclosed?"</div>
<div class="discussion-q">🗣️ "If you double ALL the side lengths of a rectangle, does the perimeter double too?"</div>""",
},

5: {
"concepts": """<h4>What Is Area?</h4>
<p>Area is the <strong>amount of flat space inside</strong> a shape. Think of it as "how many 1×1 squares fit inside?"</p>

<h4>Key Formulas</h4>
<div class="concept-grid">
<div class="concept-card blue"><strong>Rectangle</strong><br>A = length × width<br><em>A = l × w</em></div>
<div class="concept-card green"><strong>Square</strong><br>A = side × side<br><em>A = s²</em></div>
<div class="concept-card orange"><strong>Triangle</strong><br>A = ½ × base × height<br><em>A = ½bh</em></div>
</div>

<h4>Why Is Triangle Area ½ × b × h?</h4>
<p>Every triangle is <strong>exactly half of a rectangle</strong>! Draw any triangle inside a rectangle — the triangle fills exactly half. That's where the ½ comes from.</p>
<p class="tip">💡 <strong>Height must be PERPENDICULAR</strong> to the base (makes a 90° angle). It's not always a side of the triangle — sometimes it's a line drawn inside!</p>

<h4>Square Units</h4>
<p>Area is measured in <strong>square units</strong>: sq ft, sq m, sq in, cm². The "squared" means you're counting little squares.</p>

<h4>Decomposing Complex Shapes</h4>
<p>For L-shapes or irregular rooms: break them into rectangles, find each area, then add them together.</p>""",

"examples": """<div class="example-box">
<div class="example-title">Example 1: Room Carpet</div>
<p><strong>Given:</strong> Bedroom is 14 ft × 11 ft. Carpet costs $4.50/sq ft.</p>
<p><strong>Step 1:</strong> A = 14 × 11 = <strong>154 sq ft</strong></p>
<p><strong>Step 2:</strong> Cost = 154 × $4.50 = <strong>$693.00</strong></p>
</div>

<div class="example-box">
<div class="example-title">Example 2: Triangle Flag</div>
<p><strong>Given:</strong> Pennant flag with base = 8 in, height = 20 in.</p>
<p><strong>Step 1:</strong> A = ½ × 8 × 20</p>
<p><strong>Step 2:</strong> A = ½ × 160 = <strong>80 sq in</strong></p>
</div>

<div class="example-box">
<div class="example-title">Example 3: Paint a Room</div>
<p><strong>Given:</strong> Room 12 × 10 ft, ceiling 8 ft high. One window (3 × 4 ft), one door (3 × 7 ft). Paint covers 350 sq ft/gallon at $35/gallon.</p>
<p><strong>Step 1:</strong> Two walls: 2 × (12 × 8) = 192 sq ft</p>
<p><strong>Step 2:</strong> Two walls: 2 × (10 × 8) = 160 sq ft</p>
<p><strong>Step 3:</strong> Total walls = 352 sq ft</p>
<p><strong>Step 4:</strong> Subtract window (12) + door (21) = 33 sq ft</p>
<p><strong>Step 5:</strong> Paintable area = 352 − 33 = <strong>319 sq ft</strong></p>
<p><strong>Step 6:</strong> 319 ÷ 350 = 0.91 gallons → Round up to <strong>1 gallon = $35</strong></p>
</div>

<div class="example-box">
<div class="example-title">Example 4: L-Shaped Room</div>
<p><strong>Given:</strong> L-shape: main section 15 × 10 ft, bump-out 8 × 6 ft</p>
<p><strong>Step 1:</strong> Rectangle 1: 15 × 10 = 150 sq ft</p>
<p><strong>Step 2:</strong> Rectangle 2: 8 × 6 = 48 sq ft</p>
<p><strong>Step 3:</strong> Total = 150 + 48 = <strong>198 sq ft</strong></p>
</div>""",

"mistakes": """<div class="mistake-card">
<div class="mistake-wrong">❌ Using the slant height instead of the perpendicular height for triangles</div>
<div class="mistake-fix">✅ Fix: Height MUST be at 90° to the base. Draw a dotted line straight down from the top to the base.</div>
</div>
<div class="mistake-card">
<div class="mistake-wrong">❌ Forgetting the ½ in triangle area</div>
<div class="mistake-fix">✅ Fix: Remember — a triangle is HALF a rectangle. Always divide by 2!</div>
</div>
<div class="mistake-card">
<div class="mistake-wrong">❌ Writing "feet" instead of "square feet" for area</div>
<div class="mistake-fix">✅ Fix: Area = space = SQUARE units. Perimeter = distance = regular units.</div>
</div>""",

"whiteboard": """<h4>🖊️ Whiteboard Script</h4>
<ol>
<li><strong>Draw</strong> a 5 × 3 rectangle, fill it with a grid of squares. Count them: 15. "A = 5 × 3 = 15. We just counted 15 squares!"</li>
<li><strong>Draw</strong> a rectangle, then draw a diagonal. "Cut a rectangle in half → two triangles. Each triangle is ½ the rectangle."</li>
<li><strong>Height demo:</strong> Draw a triangle. Drop a perpendicular line from the top to the base. "THIS is the height — not the slant side!"</li>
<li><strong>Real-world:</strong> "Let's figure out how much carpet this classroom needs." (Estimate room dimensions, calculate together)</li>
<li><strong>L-shape challenge:</strong> Draw one on the board. "Break it into TWO rectangles. Find each area. Add them up."</li>
</ol>""",

"discussion": """<div class="discussion-q">🗣️ "If you double the length of a rectangle but keep the width the same, does the area double?"</div>
<div class="discussion-q">🗣️ "Why do contractors charge by square foot? What would happen if they charged by perimeter?"</div>
<div class="discussion-q">🗣️ "Can two shapes have the same perimeter but different areas? Give an example."</div>""",
},
}

# For sessions 6-24, I'll add more concise but still detailed teaching content
for s in range(6, 25):
    if s not in TEACHING:
        TEACHING[s] = {"concepts":"","examples":"","mistakes":"","whiteboard":"","discussion":""}

TEACHING[6] = {
"concepts": """<h4>Parallelogram Area</h4>
<p>A parallelogram is like a "pushed over" rectangle. Its area formula is the same as a rectangle's — just use the <strong>perpendicular height</strong>, not the slant side!</p>
<div class="concept-card blue" style="display:inline-block;margin:8px;font-size:1.1em;"><strong>A = base × height</strong></div>
<p class="tip">💡 If you cut a triangle off one end and move it to the other, a parallelogram becomes a rectangle!</p>

<h4>Trapezoid Area</h4>
<p>A trapezoid has two parallel sides (called <strong>bases</strong>) of different lengths. The area formula averages the two bases:</p>
<div class="concept-card orange" style="display:inline-block;margin:8px;font-size:1.1em;"><strong>A = ½(b₁ + b₂) × h</strong></div>
<p>Think of it as: "average the two bases, then multiply by height."</p>

<h4>Composite Shapes — Two Strategies</h4>
<ol><li><strong>DECOMPOSE:</strong> Break into simpler shapes, find each area, ADD them together</li>
<li><strong>SUBTRACT:</strong> Find the area of the big bounding shape, then SUBTRACT the missing piece</li></ol>""",
"examples": """<div class="example-box">
<div class="example-title">Example 1: Parallelogram</div>
<p><strong>Given:</strong> Base = 12 cm, height = 7 cm, slant side = 8 cm</p>
<p><strong>Step 1:</strong> A = 12 × 7 = <strong>84 cm²</strong> (ignore the slant side!)</p>
</div>
<div class="example-box">
<div class="example-title">Example 2: Trapezoid</div>
<p><strong>Given:</strong> Bases = 10 in and 16 in, height = 7 in</p>
<p><strong>Step 1:</strong> A = ½(10 + 16) × 7 = ½(26) × 7 = 13 × 7 = <strong>91 in²</strong></p>
</div>
<div class="example-box">
<div class="example-title">Example 3: Baking Pan Comparison</div>
<p><strong>Given:</strong> 9×13 pan vs. two 8×8 pans</p>
<p><strong>9×13:</strong> A = 117 sq in</p>
<p><strong>Two 8×8:</strong> A = 2 × 64 = 128 sq in — <strong>more batter space!</strong></p>
</div>""",
"mistakes": """<div class="mistake-card"><div class="mistake-wrong">❌ Using the slant side as the height of a parallelogram</div><div class="mistake-fix">✅ The height is the PERPENDICULAR distance between the bases</div></div>
<div class="mistake-card"><div class="mistake-wrong">❌ Forgetting the ½ in the trapezoid formula</div><div class="mistake-fix">✅ Think: "average the bases" — averaging always means dividing by 2</div></div>""",
"whiteboard": """<h4>🖊️ Whiteboard Script</h4>
<ol><li>Draw a parallelogram. Cut a triangle off the left, slide it to the right → it's a rectangle! "Same formula: base × height"</li>
<li>Draw a trapezoid. "Two different bases — which do we use? BOTH! Average them."</li>
<li>Baking pan challenge: "Which holds more brownie batter — one 9×13 or two 8×8 pans?"</li></ol>""",
"discussion": """<div class="discussion-q">🗣️ "Is a rectangle a special type of parallelogram? Why?"</div>
<div class="discussion-q">🗣️ "What happens to a trapezoid's area if you make both bases the same length?"</div>""",
}

TEACHING[7] = {
"concepts": """<h4>Circle Vocabulary</h4>
<div class="concept-grid">
<div class="concept-card blue"><strong>Radius (r)</strong><br>Center to edge<br><em>Half the diameter</em></div>
<div class="concept-card green"><strong>Diameter (d)</strong><br>Edge to edge through center<br><em>d = 2r</em></div>
<div class="concept-card orange"><strong>Circumference (C)</strong><br>Distance around the circle<br><em>The circle's "perimeter"</em></div>
<div class="concept-card red"><strong>Pi (π)</strong><br>≈ 3.14159...<br><em>The ratio C ÷ d for EVERY circle</em></div>
</div>

<h4>Circumference Formulas</h4>
<div class="concept-card blue" style="display:inline-block;margin:8px;font-size:1.1em;"><strong>C = πd</strong> (if you know diameter)</div>
<div class="concept-card green" style="display:inline-block;margin:8px;font-size:1.1em;"><strong>C = 2πr</strong> (if you know radius)</div>
<p class="tip">💡 These are the SAME formula! Since d = 2r, πd = π(2r) = 2πr</p>

<h4>What IS Pi?</h4>
<p>Take ANY circle. Measure around it (circumference). Divide by the diameter. You ALWAYS get the same number: <strong>3.14159...</strong> This is π (pi). It works for a coin, a pizza, the Earth — any circle!</p>""",
"examples": """<div class="example-box">
<div class="example-title">Example 1: Bike Wheel</div>
<p><strong>Given:</strong> Wheel diameter = 26 inches</p>
<p><strong>C</strong> = πd = 3.14 × 26 = <strong>81.64 inches</strong> per rotation</p>
<p><strong>Bonus:</strong> In feet: 81.64 ÷ 12 ≈ 6.8 ft per rotation</p>
</div>
<div class="example-box">
<div class="example-title">Example 2: Running Track</div>
<p><strong>Given:</strong> Circular track, radius = 50 meters</p>
<p><strong>C</strong> = 2πr = 2 × 3.14 × 50 = <strong>314 meters</strong> per lap</p>
</div>
<div class="example-box">
<div class="example-title">Example 3: Find the Diameter</div>
<p><strong>Given:</strong> A circular garden has circumference = 62.8 feet</p>
<p><strong>C</strong> = πd → 62.8 = 3.14 × d → d = 62.8 ÷ 3.14 = <strong>20 feet</strong></p>
</div>""",
"mistakes": """<div class="mistake-card"><div class="mistake-wrong">❌ Using diameter when the formula needs radius (or vice versa)</div><div class="mistake-fix">✅ Always check: do you have r or d? Convert if needed: r = d ÷ 2</div></div>
<div class="mistake-card"><div class="mistake-wrong">❌ Forgetting what π means and using 3 instead of 3.14</div><div class="mistake-fix">✅ Always use at least 3.14. Your calculator may have a π button for more precision.</div></div>""",
"whiteboard": """<h4>🖊️ Whiteboard Script</h4>
<ol><li>"Everyone, what's the distance across a basketball? That's the DIAMETER. Half of that? RADIUS."</li>
<li>"If I wrap a string around this circle and unroll it... the length of that string is the CIRCUMFERENCE."</li>
<li>Demo: Measure a round object's circumference with string, measure diameter with ruler. Divide. "What do you get? About 3.14!"</li>
<li>Bike wheel problem on board: "26-inch wheel. One full rotation = ? inches. How far in 100 rotations?"</li></ol>""",
"discussion": """<div class="discussion-q">🗣️ "If you double the diameter of a circle, does the circumference double too?"</div>
<div class="discussion-q">🗣️ "Why is π the same number for EVERY circle, no matter how big or small?"</div>""",
}

TEACHING[8] = {
"concepts": """<h4>Circle Area Formula</h4>
<div class="concept-card red" style="display:inline-block;margin:8px;font-size:1.2em;"><strong>A = πr²</strong></div>
<p><strong>Step by step:</strong></p>
<ol><li>Find the <strong>radius</strong> (if given diameter, divide by 2!)</li>
<li><strong>Square the radius</strong> (r × r)</li>
<li><strong>Multiply by π</strong> (3.14)</li></ol>

<h4>⚠️ Common Confusion: r² vs 2r</h4>
<p><strong>r²</strong> means r × r (radius times itself). It does NOT mean r × 2. This is the #1 mistake!</p>
<div class="concept-card orange" style="display:inline-block;margin:8px;">If r = 5: r² = 5 × 5 = <strong>25</strong> (not 10!)</div>

<h4>Circumference vs Area — Which Formula?</h4>
<table class="simple-table">
<tr><th>Need to find...</th><th>Formula</th><th>Units</th></tr>
<tr><td>Distance AROUND</td><td>C = πd or 2πr</td><td>regular (ft, in)</td></tr>
<tr><td>Space INSIDE</td><td>A = πr²</td><td>square (sq ft, sq in)</td></tr>
</table>""",
"examples": """<div class="example-box">
<div class="example-title">Example 1: 🍕 The Great Pizza Debate</div>
<p><strong>Given:</strong> 16" pizza for $14 vs two 12" pizzas for $10 each</p>
<p><strong>16" pizza:</strong> r = 8, A = π(8²) = 3.14 × 64 = 200.96 sq in → $14/200.96 = <strong>$0.070/sq in</strong></p>
<p><strong>Two 12" pizzas:</strong> r = 6, A = π(6²) × 2 = 3.14 × 36 × 2 = 226.08 sq in → $20/226.08 = <strong>$0.088/sq in</strong></p>
<p><strong>Winner:</strong> The 16" pizza is <strong>cheaper per square inch</strong>! But two 12" gives more total pizza.</p>
</div>
<div class="example-box">
<div class="example-title">Example 2: Sprinkler Coverage</div>
<p><strong>Given:</strong> Sprinkler reaches 25 ft in every direction (radius = 25 ft)</p>
<p>A = π(25²) = 3.14 × 625 = <strong>1,962.5 sq ft</strong> of watered lawn</p>
</div>""",
"mistakes": """<div class="mistake-card"><div class="mistake-wrong">❌ Using diameter instead of radius in A = πr²</div><div class="mistake-fix">✅ ALWAYS find radius first. If given diameter, divide by 2 BEFORE squaring!</div></div>
<div class="mistake-card"><div class="mistake-wrong">❌ Squaring the entire expression πr instead of just r</div><div class="mistake-fix">✅ Only the r gets squared: π × (r × r), not (π × r) × (π × r)</div></div>""",
"whiteboard": """<h4>🖊️ Whiteboard Script</h4>
<ol><li>"Pizza vote! One 16-inch for $14 or two 12-inch for $10 each? Raise your hand..."</li>
<li>Work through both on the board. "Surprise! The 16-inch is a better DEAL per square inch."</li>
<li>Key moment: "r² means r TIMES r, not r times 2. If r = 5, r² = 25, NOT 10."</li>
<li>Draw the circumference vs area formulas side by side. "Distance around = πd. Space inside = πr²."</li></ol>""",
"discussion": """<div class="discussion-q">🗣️ "If you double the radius of a pizza, do you get double the pizza? (Hint: test it!)"</div>
<div class="discussion-q">🗣️ "Why are most dinner plates circular and not square?"</div>""",
}

# Sessions 9-24 with key teaching details
TEACHING[9]["concepts"] = """<h4>Composite Shape Strategies</h4>
<div class="concept-grid">
<div class="concept-card blue"><strong>Strategy 1: DECOMPOSE</strong><br>Break into simple shapes<br>Find each area<br>ADD them together</div>
<div class="concept-card orange"><strong>Strategy 2: SUBTRACT</strong><br>Find the big bounding shape<br>Find the missing piece<br>SUBTRACT the missing part</div>
</div>
<p class="tip">💡 Both strategies give the same answer! Use whichever is easier for that particular shape.</p>
<h4>Shapes with Semicircles</h4>
<p>A semicircle is half a circle. Area = ½πr². Look for these on swimming pools, arched windows, and track fields.</p>"""
TEACHING[9]["examples"] = """<div class="example-box"><div class="example-title">Example: Pool with Semicircle End</div>
<p><strong>Given:</strong> Rectangle 40×20 ft with a semicircle (diameter 20 ft) on one end</p>
<p><strong>Rectangle:</strong> 40 × 20 = 800 sq ft</p>
<p><strong>Semicircle:</strong> r = 10, A = ½ × π × 10² = ½ × 3.14 × 100 = 157 sq ft</p>
<p><strong>Total:</strong> 800 + 157 = <strong>957 sq ft</strong></p></div>"""
TEACHING[9]["mistakes"] = """<div class="mistake-card"><div class="mistake-wrong">❌ Using diameter as radius for the semicircle</div><div class="mistake-fix">✅ If the pool is 20 ft wide, the semicircle's DIAMETER is 20, so radius = 10!</div></div>"""

TEACHING[10]["concepts"] = """<h4>What Is Volume?</h4>
<p>Volume is the <strong>amount of 3D space inside</strong> an object. Think: "how many little cubes fit inside?"</p>
<div class="concept-card blue" style="display:inline-block;margin:8px;font-size:1.1em;"><strong>V = length × width × height</strong></div>
<p>Units: <strong>cubic units</strong> (ft³, in³, cm³, m³)</p>
<h4>Useful Conversions</h4>
<table class="simple-table"><tr><th>Know this</th><th>Use for</th></tr>
<tr><td>1 ft³ = 7.48 gallons</td><td>Fish tanks, pools</td></tr>
<tr><td>1 gallon = 231 in³</td><td>Containers</td></tr>
<tr><td>1 m³ = 1,000 liters</td><td>Metric problems</td></tr></table>"""
TEACHING[10]["examples"] = """<div class="example-box"><div class="example-title">Example: Shipping Box</div>
<p><strong>Given:</strong> Box 18 × 12 × 8 inches. Product is 6 × 4 × 3 inches.</p>
<p><strong>Box volume:</strong> 18 × 12 × 8 = 1,728 in³</p>
<p><strong>Product volume:</strong> 6 × 4 × 3 = 72 in³</p>
<p><strong>How many fit:</strong> 1,728 ÷ 72 = 24 products (if perfectly packed)</p>
<p class="tip">💡 In reality, you'd calculate how many fit per dimension: 18÷6=3, 12÷4=3, 8÷3=2 → 3×3×2 = <strong>18 products</strong></p></div>"""

TEACHING[11]["concepts"] = """<h4>Cylinder Volume</h4>
<p>A cylinder is a circle extended into 3D. Its volume = the area of the circular base × height.</p>
<div class="concept-card blue" style="display:inline-block;margin:8px;font-size:1.1em;"><strong>V = πr²h</strong></div>
<h4>Surface Area</h4>
<p>Surface area = total area of ALL faces of a 3D object. For a rectangular prism:</p>
<div class="concept-card orange" style="display:inline-block;margin:8px;"><strong>SA = 2lw + 2lh + 2wh</strong><br><em>Think: 3 pairs of identical rectangles</em></div>"""
TEACHING[11]["examples"] = """<div class="example-box"><div class="example-title">Example: Tall vs Wide Cup</div>
<p><strong>Tall cup:</strong> r=2", h=8" → V = π(4)(8) = 100.5 in³</p>
<p><strong>Wide cup:</strong> r=3", h=4" → V = π(9)(4) = 113.1 in³</p>
<p><strong>Short wide cup wins!</strong> The wider radius matters more because it gets SQUARED.</p></div>"""

TEACHING[13]["concepts"] = """<h4>What Is a Variable?</h4>
<p>A <strong>variable</strong> is a letter that represents an unknown number. It's like a box with a mystery number inside.</p>
<div class="concept-card blue" style="display:inline-block;margin:8px;">x, n, y — these are all variables. They stand for numbers we don't know yet.</div>

<h4>Expression vs Equation</h4>
<table class="simple-table"><tr><th>Expression</th><th>Equation</th></tr>
<tr><td>3x + 5</td><td>3x + 5 = 17</td></tr>
<tr><td>No equals sign</td><td>HAS an equals sign</td></tr>
<tr><td>Can evaluate</td><td>Can solve</td></tr></table>

<h4>Translating Words → Algebra</h4>
<table class="simple-table"><tr><th>Words</th><th>Operation</th><th>Example</th></tr>
<tr><td>more than, increased by, sum, plus, added to</td><td>+</td><td>"5 more than n" → n + 5</td></tr>
<tr><td>less than, decreased by, minus, fewer</td><td>−</td><td>"3 less than x" → x − 3</td></tr>
<tr><td>times, product, multiplied by, of, each</td><td>×</td><td>"twice n" → 2n</td></tr>
<tr><td>divided by, quotient, per, split</td><td>÷</td><td>"n split among 4" → n/4</td></tr></table>
<p class="tip">💡 <strong>Watch out!</strong> "5 less than n" is n − 5, NOT 5 − n. The "than" flips the order!</p>

<h4>Evaluating Expressions</h4>
<p>To evaluate, <strong>plug in</strong> the given value and calculate:</p>
<p>If x = 3, then 2x + 7 = 2(3) + 7 = 6 + 7 = <strong>13</strong></p>"""
TEACHING[13]["examples"] = """<div class="example-box"><div class="example-title">Example 1: Game Score</div>
<p><strong>Game scoring:</strong> coins = 3 pts, gems = 5 pts, stars = 10 pts</p>
<p><strong>Expression:</strong> Score = 3c + 5g + 10s</p>
<p><strong>Player collects:</strong> 8 coins, 3 gems, 2 stars</p>
<p>Score = 3(8) + 5(3) + 10(2) = 24 + 15 + 20 = <strong>59 points</strong></p></div>
<div class="example-box"><div class="example-title">Example 2: "Less than" trap</div>
<p><strong>"7 less than a number n"</strong></p>
<p>❌ 7 − n (WRONG — this means "7 minus something")</p>
<p>✅ n − 7 (RIGHT — start with n, then subtract 7)</p></div>"""
TEACHING[13]["mistakes"] = """<div class="mistake-card"><div class="mistake-wrong">❌ Writing "5 less than x" as 5 − x</div><div class="mistake-fix">✅ "Less than" means subtract FROM the number: x − 5</div></div>
<div class="mistake-card"><div class="mistake-wrong">❌ Forgetting to multiply: writing 2x as "2 and x" = 2 + x</div><div class="mistake-fix">✅ In algebra, a number next to a variable means MULTIPLY: 2x = 2 × x</div></div>"""

TEACHING[14]["concepts"] = """<h4>What Are Like Terms?</h4>
<p>Like terms have the <strong>exact same variable(s) raised to the same power</strong>.</p>
<table class="simple-table"><tr><th>Like Terms ✅</th><th>NOT Like Terms ❌</th></tr>
<tr><td>3x and 7x</td><td>3x and 3y</td></tr>
<tr><td>5ab and 2ab</td><td>5x and 5x²</td></tr>
<tr><td>4 and 9 (constants)</td><td>4 and 4x</td></tr></table>
<h4>How to Combine</h4>
<p>Add or subtract the <strong>coefficients</strong> (the numbers in front). The variable part stays the same!</p>
<p><strong>3x + 5x = 8x</strong> (like combining 3 apples + 5 apples = 8 apples)</p>
<p><strong>7y − 2y = 5y</strong> (7 oranges − 2 oranges = 5 oranges)</p>"""
TEACHING[14]["examples"] = """<div class="example-box"><div class="example-title">Example: Shopping Cart</div>
<p><strong>Cart:</strong> 3 apples + 2 oranges + 5 apples + 1 orange</p>
<p><strong>Combine apples:</strong> 3 + 5 = 8 apples</p>
<p><strong>Combine oranges:</strong> 2 + 1 = 3 oranges</p>
<p><strong>Simplified:</strong> 8 apples + 3 oranges → In algebra: 8a + 3o</p></div>
<div class="example-box"><div class="example-title">Example: Simplify 4x + 3y + 2x − y + 7</div>
<p><strong>Group x terms:</strong> 4x + 2x = 6x</p>
<p><strong>Group y terms:</strong> 3y − y = 2y</p>
<p><strong>Constants:</strong> 7</p>
<p><strong>Answer:</strong> <strong>6x + 2y + 7</strong></p></div>"""

TEACHING[15]["concepts"] = """<h4>Order of Operations (PEMDAS)</h4>
<div class="concept-grid">
<div class="concept-card red"><strong>P</strong> — Parentheses first</div>
<div class="concept-card orange"><strong>E</strong> — Exponents next</div>
<div class="concept-card blue"><strong>MD</strong> — Multiply & Divide (left to right)</div>
<div class="concept-card green"><strong>AS</strong> — Add & Subtract (left to right)</div>
</div>
<p class="tip">💡 <strong>M and D are EQUAL priority</strong> — do them left to right. Same for A and S. It's not "multiply before divide."</p>
<h4>PEMDAS with Variables</h4>
<p><strong>Big trap:</strong> 2x² vs (2x)²</p>
<table class="simple-table"><tr><th>Expression</th><th>If x = 3</th><th>Result</th></tr>
<tr><td>2x²</td><td>2 × (3²) = 2 × 9</td><td><strong>18</strong></td></tr>
<tr><td>(2x)²</td><td>(2 × 3)² = 6²</td><td><strong>36</strong></td></tr></table>"""

TEACHING[16]["concepts"] = """<h4>What Is an Equation?</h4>
<p>An equation has an <strong>equals sign</strong>. It's like a balance scale — both sides must be equal.</p>
<h4>Solving = Getting the Variable Alone</h4>
<p>Use <strong>inverse (opposite) operations</strong> to "undo" what's been done to the variable:</p>
<table class="simple-table"><tr><th>If you see...</th><th>Undo it with...</th></tr>
<tr><td>x + 7 = 15</td><td>Subtract 7 from both sides</td></tr>
<tr><td>x − 3 = 10</td><td>Add 3 to both sides</td></tr></table>
<div class="concept-card blue" style="display:inline-block;margin:8px;"><strong>Golden Rule: Whatever you do to one side, you MUST do to the other!</strong></div>
<h4>Always Check Your Answer!</h4>
<p>Plug your answer back into the original equation. If both sides are equal, you're right!</p>"""
TEACHING[16]["examples"] = """<div class="example-box"><div class="example-title">Example: Budget Problem</div>
<p><strong>"You spent some money and have $23 left. You started with $50."</strong></p>
<p><strong>Equation:</strong> 50 − x = 23</p>
<p><strong>Solve:</strong> −x = 23 − 50 → −x = −27 → x = <strong>$27</strong></p>
<p><strong>Check:</strong> 50 − 27 = 23 ✅</p></div>
<div class="example-box"><div class="example-title">Example: Temperature Change</div>
<p><strong>"Temperature rose 15° to reach 72°F."</strong></p>
<p><strong>Equation:</strong> x + 15 = 72</p>
<p><strong>Solve:</strong> x = 72 − 15 = <strong>57°F</strong></p>
<p><strong>Check:</strong> 57 + 15 = 72 ✅</p></div>"""

TEACHING[17]["concepts"] = """<h4>Multiplication & Division Equations</h4>
<table class="simple-table"><tr><th>If you see...</th><th>Undo it with...</th></tr>
<tr><td>5x = 35</td><td>Divide both sides by 5</td></tr>
<tr><td>x/4 = 12</td><td>Multiply both sides by 4</td></tr></table>
<h4>The Inverse Pair</h4>
<p>Multiplication ↔ Division (they undo each other, just like addition ↔ subtraction)</p>"""
TEACHING[17]["examples"] = """<div class="example-box"><div class="example-title">Example: Fair Share</div>
<p><strong>"4 friends split a restaurant bill equally. Each paid $18.50."</strong></p>
<p><strong>Equation:</strong> x ÷ 4 = 18.50</p>
<p><strong>Solve:</strong> x = 18.50 × 4 = <strong>$74.00</strong></p></div>
<div class="example-box"><div class="example-title">Example: Unit Price</div>
<p><strong>"6 notebooks cost $15. Price per notebook?"</strong></p>
<p><strong>Equation:</strong> 6x = 15</p>
<p><strong>Solve:</strong> x = 15 ÷ 6 = <strong>$2.50</strong></p></div>"""

TEACHING[19]["concepts"] = """<h4>Two-Step Equations</h4>
<p>These require TWO operations to solve. <strong>Undo in REVERSE order!</strong></p>
<div class="concept-card blue" style="display:inline-block;margin:8px;">
<strong>Step 1:</strong> Undo addition/subtraction<br>
<strong>Step 2:</strong> Undo multiplication/division
</div>
<p class="tip">💡 <strong>Socks-and-shoes analogy:</strong> You put socks on first, then shoes. To undo, take shoes off first, then socks. Same with equations — undo in reverse order!</p>
<h4>Pattern: ax + b = c</h4>
<ol><li>Subtract b from both sides → ax = c − b</li><li>Divide both sides by a → x = (c − b) ÷ a</li></ol>"""
TEACHING[19]["examples"] = """<div class="example-box"><div class="example-title">Example: Phone Plan</div>
<p><strong>"$25/month + $0.10/text. Bill = $37."</strong></p>
<p><strong>Equation:</strong> 25 + 0.10t = 37</p>
<p><strong>Step 1:</strong> 0.10t = 37 − 25 = 12</p>
<p><strong>Step 2:</strong> t = 12 ÷ 0.10 = <strong>120 texts</strong></p></div>"""

TEACHING[20]["concepts"] = """<h4>Inequalities</h4>
<table class="simple-table"><tr><th>Symbol</th><th>Meaning</th><th>Example</th></tr>
<tr><td>&lt;</td><td>less than</td><td>x &lt; 5 (x is less than 5)</td></tr>
<tr><td>&gt;</td><td>greater than</td><td>x &gt; 3 (x is greater than 3)</td></tr>
<tr><td>≤</td><td>less than or equal to</td><td>x ≤ 10</td></tr>
<tr><td>≥</td><td>greater than or equal to</td><td>x ≥ 7</td></tr></table>
<h4>Graphing on a Number Line</h4>
<ul><li><strong>Open circle ○</strong> = NOT included (&lt; or &gt;)</li>
<li><strong>Closed circle ●</strong> = IS included (≤ or ≥)</li>
<li>Arrow shows ALL the solutions going in that direction</li></ul>
<h4>⚠️ The Flip Rule</h4>
<div class="concept-card red" style="display:inline-block;margin:8px;"><strong>When you multiply or divide by a NEGATIVE number, FLIP the inequality sign!</strong></div>"""
TEACHING[20]["examples"] = """<div class="example-box"><div class="example-title">Example: Height Requirement</div>
<p><strong>"Must be at least 48 inches to ride"</strong></p>
<p><strong>Inequality:</strong> h ≥ 48</p>
<p><strong>Graph:</strong> Closed circle at 48, arrow going right →</p>
<p>47" = can't ride ❌ | 48" = CAN ride ✅ | 50" = CAN ride ✅</p></div>"""

TEACHING[22]["concepts"] = """<h4>The Coordinate Plane</h4>
<p>Two number lines that cross at the <strong>origin (0,0)</strong>:</p>
<ul><li><strong>x-axis:</strong> horizontal (left-right)</li>
<li><strong>y-axis:</strong> vertical (up-down)</li></ul>
<h4>Ordered Pairs (x, y)</h4>
<p><strong>Always x first, then y.</strong> Think: "Run before you jump!" or "Enter the house (go along the hall), then go upstairs."</p>
<h4>Four Quadrants</h4>
<table class="simple-table"><tr><th>Quadrant</th><th>x</th><th>y</th><th>Example</th></tr>
<tr><td>I (top-right)</td><td>+</td><td>+</td><td>(3, 4)</td></tr>
<tr><td>II (top-left)</td><td>−</td><td>+</td><td>(−2, 5)</td></tr>
<tr><td>III (bottom-left)</td><td>−</td><td>−</td><td>(−1, −3)</td></tr>
<tr><td>IV (bottom-right)</td><td>+</td><td>−</td><td>(4, −2)</td></tr></table>"""
TEACHING[22]["examples"] = """<div class="example-box"><div class="example-title">Example: Plot (3, −2)</div>
<p><strong>Step 1:</strong> Start at origin (0,0)</p>
<p><strong>Step 2:</strong> Move RIGHT 3 (positive x)</p>
<p><strong>Step 3:</strong> Move DOWN 2 (negative y)</p>
<p><strong>Result:</strong> You're in <strong>Quadrant IV</strong></p></div>"""

TEACHING[23]["concepts"] = """<h4>Linear Relationships</h4>
<p>A <strong>linear relationship</strong> means the values change at a <strong>constant rate</strong>. When you plot the points, they form a <strong>straight line</strong>.</p>
<h4>Input/Output Tables</h4>
<p>Given a rule like <strong>y = 2x + 1</strong>:</p>
<table class="simple-table"><tr><th>x (input)</th><th>y = 2x + 1</th><th>y (output)</th></tr>
<tr><td>0</td><td>2(0)+1</td><td>1</td></tr>
<tr><td>1</td><td>2(1)+1</td><td>3</td></tr>
<tr><td>2</td><td>2(2)+1</td><td>5</td></tr>
<tr><td>3</td><td>2(3)+1</td><td>7</td></tr></table>
<p>Pattern: y increases by 2 each time x increases by 1. That's the <strong>rate of change</strong> (slope).</p>"""

# Now rebuild the HTML
import re

with open("/tmp/math-deploy/lesson-plans.html", "r") as f:
    content = f.read()

# Add new CSS for teaching guides
new_css = """
        /* Teaching Guide Styles */
        .expand-btn { display: flex; align-items: center; gap: 8px; width: 100%;
                     padding: 12px 16px; background: linear-gradient(135deg, #E8F0FE, #F0F4FF);
                     border: 2px solid #C2D6F2; border-radius: 10px; cursor: pointer;
                     font-family: inherit; font-size: 0.95em; font-weight: 700;
                     color: #1F4E79; transition: all 0.2s; margin: 6px 0; text-align: left; }
        .expand-btn:hover { background: #D6E4F0; border-color: #2E75B6; transform: translateX(3px); }
        .expand-btn .arrow { transition: transform 0.2s; font-size: 0.8em; }
        .expand-btn.open .arrow { transform: rotate(90deg); }
        .expand-content { display: none; padding: 15px; margin: 0 0 10px;
                        border: 1px solid #e8e8e8; border-radius: 0 0 10px 10px;
                        background: #fafbfc; font-size: 0.93em; line-height: 1.7; }
        .expand-content.open { display: block; }
        .expand-content h4 { color: #1F4E79; margin: 14px 0 8px; font-size: 1.05em; }
        .expand-content h4:first-child { margin-top: 0; }
        .expand-content p { margin: 6px 0; }
        .expand-content ol, .expand-content ul { margin: 8px 0; padding-left: 24px; }
        .expand-content li { margin: 4px 0; }

        .concept-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
                       gap: 10px; margin: 12px 0; }
        .concept-card { padding: 14px; border-radius: 10px; text-align: center; font-size: 0.92em; }
        .concept-card.blue { background: #E8F0FE; border: 1px solid #C2D6F2; }
        .concept-card.green { background: #E8F5E9; border: 1px solid #C8E6C9; }
        .concept-card.orange { background: #FFF3E0; border: 1px solid #FFE0B2; }
        .concept-card.red { background: #FFEBEE; border: 1px solid #FFCDD2; }
        .concept-icon { font-size: 1.5em; margin-bottom: 4px; }

        .example-box { background: white; border-left: 4px solid #2E75B6; border-radius: 8px;
                      padding: 14px; margin: 12px 0; box-shadow: 0 1px 4px rgba(0,0,0,0.06); }
        .example-title { font-weight: 800; color: #2E75B6; margin-bottom: 8px; font-size: 0.95em; }

        .mistake-card { margin: 10px 0; padding: 12px; border-radius: 8px;
                       background: #FFF8F0; border: 1px solid #FFE0CC; }
        .mistake-wrong { color: #C62828; font-weight: 700; margin-bottom: 4px; }
        .mistake-fix { color: #2E7D32; }

        .discussion-q { padding: 10px 14px; margin: 6px 0; background: #F3E5F5;
                       border-radius: 8px; border-left: 3px solid #9C27B0; font-weight: 600; }

        .simple-table { width: 100%; border-collapse: collapse; margin: 10px 0; font-size: 0.92em; }
        .simple-table th { background: #E8F0FE; color: #1F4E79; padding: 8px 12px;
                          text-align: left; border-bottom: 2px solid #C2D6F2; }
        .simple-table td { padding: 8px 12px; border-bottom: 1px solid #eee; }

        .tip { background: #FFFDE7; padding: 8px 12px; border-radius: 6px;
              border-left: 3px solid #FDD835; margin: 8px 0; font-size: 0.92em; }

        @media (max-width: 600px) { .concept-grid { grid-template-columns: 1fr 1fr; } }
"""

content = content.replace(
    "@media (max-width: 600px) { .diff-box { grid-template-columns: 1fr; } }",
    "@media (max-width: 600px) { .diff-box { grid-template-columns: 1fr; } }" + new_css
)

# Add the teaching data as JS and update the template
teaching_js = "const teachingData = {\n"
for s, data in sorted(TEACHING.items()):
    if any(data.values()):
        teaching_js += f"  {s}: {{\n"
        for key, val in data.items():
            escaped = val.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')
            teaching_js += f"    {key}: `{escaped}`,\n"
        teaching_js += "  },\n"
teaching_js += "};\n"

teaching_js += """
function renderTeaching(sessionNum) {
    const t = teachingData[sessionNum];
    if (!t) return '';
    let html = '<div class="lesson-section"><h3>📚 Teaching Guide (Expandable)</h3>';
    
    const sections = [
        {key:'concepts', icon:'🧠', label:'Key Concepts & Explanations'},
        {key:'examples', icon:'✍️', label:'Worked Examples (show on TV/whiteboard)'},
        {key:'whiteboard', icon:'🖊️', label:'Whiteboard Script'},
        {key:'mistakes', icon:'⚠️', label:'Common Student Mistakes'},
        {key:'discussion', icon:'🗣️', label:'Discussion Questions'},
    ];
    
    sections.forEach(sec => {
        if (t[sec.key]) {
            const id = 'teach_' + sessionNum + '_' + sec.key;
            html += `<button class="expand-btn" onclick="toggleExpand('${id}')">
                <span class="arrow">▶</span> ${sec.icon} ${sec.label}
            </button>
            <div class="expand-content" id="${id}">${t[sec.key]}</div>`;
        }
    });
    
    html += '</div>';
    return html;
}

function toggleExpand(id) {
    const el = document.getElementById(id);
    const btn = el.previousElementSibling;
    el.classList.toggle('open');
    btn.classList.toggle('open');
}
"""

# Inject teaching JS before the video data
content = content.replace("const videoData =", teaching_js + "\nconst videoData =")

# Update template to include teaching guide after the video section
content = content.replace(
    "${renderVideos(l.s)}\n        <div class=\"lesson-section\"><h3>📖 Direct Instruction</h3>",
    "${renderVideos(l.s)}\n        ${renderTeaching(l.s)}\n        <div class=\"lesson-section\"><h3>📖 Direct Instruction</h3>"
)

with open("/tmp/math-deploy/lesson-plans.html", "w") as f:
    f.write(content)

print(f"✅ Added detailed teaching guides for {sum(1 for s,d in TEACHING.items() if any(d.values()))} sessions")
print("   Expandable sections: Concepts, Worked Examples, Whiteboard Script, Common Mistakes, Discussion Questions")
