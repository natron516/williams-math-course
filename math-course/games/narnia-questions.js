// Narnia Math Relay — Full Question Bank (80 questions)
// Each game picks 20 at random (18 regular + 2 bonus), shuffled fresh every time.

const QUESTION_BANK = [
  // ── ADDITION & SUBTRACTION ─────────────────────────────────────
  {q:"🦁 <b>Mr. Tumnus's Parcels</b><br>Mr. Tumnus carried 14 parcels. He dropped 6 and went back for 3. How many did he arrive home with?", a:["11"], pts:10, hint:"14 − 6 + 3"},
  {q:"🐟 <b>Mrs. Beaver's Fish</b><br>Mrs. Beaver caught 23 fish on Monday and 17 on Tuesday. She gave 8 to the Beavers' neighbors. How many did she have left?", a:["32"], pts:10, hint:"23 + 17 − 8"},
  {q:"🏹 <b>Peter's Arrows</b><br>Peter had 45 arrows. He used 18 in battle and found 7 more on the field. How many does he have now?", a:["34"], pts:10, hint:"45 − 18 + 7"},
  {q:"🍎 <b>Lucy's Apples</b><br>Lucy picked 36 apples. Susan picked 28. They gave 15 to the dwarfs. How many apples remained?", a:["49"], pts:10, hint:"36 + 28 − 15"},
  {q:"🐻 <b>Talking Bears</b><br>There were 52 Talking Animals at the feast. 19 left early, then 8 more arrived. How many were there at the end?", a:["41"], pts:10, hint:"52 − 19 + 8"},
  {q:"⚔️ <b>Soldiers at the Gate</b><br>Cair Paravel had 64 guards. 27 went to patrol the forest. How many remained at the castle?", a:["37"], pts:10, hint:"64 − 27"},

  // ── MULTIPLICATION ─────────────────────────────────────────────
  {q:"🎅 <b>Father Christmas's Gifts</b><br>Father Christmas visited 9 villages and left 6 packages at each. How many packages total?", a:["54"], pts:10, hint:"9 × 6"},
  {q:"🕯️ <b>Lanterns in the Hall</b><br>The great hall had 8 rows of candles with 12 candles in each row. How many candles in all?", a:["96"], pts:10, hint:"8 × 12"},
  {q:"🐭 <b>The Mice</b><br>12 mice each chewed through 3 cords at the Stone Table. How many cord-chews total?", a:["36"], pts:10, hint:"12 × 3"},
  {q:"🏰 <b>Castle Stones</b><br>Each wall of Cair Paravel used 144 stones. There are 7 walls. How many stones total?", a:["1008"], pts:10, hint:"144 × 7"},
  {q:"🌲 <b>Trees in Lantern Waste</b><br>There are 15 rows of trees with 11 trees per row. How many trees?", a:["165"], pts:10, hint:"15 × 11"},
  {q:"🦌 <b>Reindeer Steps</b><br>Each of Father Christmas's 9 reindeer took 14 steps per second. How many steps per second total?", a:["126"], pts:10, hint:"9 × 14"},

  // ── DIVISION ───────────────────────────────────────────────────
  {q:"🐟 <b>The Beaver's Barrels</b><br>72 trout divided equally among 9 barrels. How many per barrel?", a:["8"], pts:10, hint:"72 ÷ 9"},
  {q:"🍞 <b>Bread for the Army</b><br>240 loaves of bread shared equally among 8 battalions. How many loaves per battalion?", a:["30"], pts:10, hint:"240 ÷ 8"},
  {q:"💎 <b>Sharing the Treasure</b><br>The four Pevensies split 84 gold coins equally. How many coins each?", a:["21"], pts:10, hint:"84 ÷ 4"},
  {q:"🏹 <b>Arrows in Bundles</b><br>126 arrows packed into bundles of 7. How many bundles?", a:["18"], pts:10, hint:"126 ÷ 7"},
  {q:"🌙 <b>Night Watch</b><br>48 guards split into groups of 6 for night watch. How many groups?", a:["8"], pts:10, hint:"48 ÷ 6"},

  // ── FRACTIONS ──────────────────────────────────────────────────
  {q:"🔢 <b>Fraction Review</b><br>There are 20 students. ¾ remembered their homework. How many remembered?", a:["15"], pts:10, hint:"20 × 3 ÷ 4"},
  {q:"🍰 <b>Mr. Tumnus's Cakes</b><br>Mr. Tumnus baked 24 cakes and set out ¾ for Lucy. How many cakes?", a:["18"], pts:10, hint:"24 × 3 ÷ 4"},
  {q:"🍯 <b>Honey Jars</b><br>The Beavers had 40 jars of honey. They used ½ of them for the feast. How many jars did they use?", a:["20"], pts:10, hint:"40 ÷ 2"},
  {q:"🎁 <b>Gift Boxes</b><br>Susan had 36 gift boxes. She wrapped ⅔ of them. How many did she wrap?", a:["24"], pts:10, hint:"36 × 2 ÷ 3"},
  {q:"🍎 <b>The Orchard</b><br>The orchard had 60 trees. ¼ were apple trees. How many apple trees?", a:["15"], pts:10, hint:"60 ÷ 4"},
  {q:"🌊 <b>Dawn Treader Supplies</b><br>The ship carried 80 barrels of water. They used ⅜ on the voyage. How many barrels used?", a:["30"], pts:10, hint:"80 × 3 ÷ 8"},

  // ── PERCENTAGES ────────────────────────────────────────────────
  {q:"💯 <b>Percentage Review</b><br>80 items on sale. 25% are sold out. How many are sold out?", a:["20"], pts:10, hint:"80 ÷ 4"},
  {q:"💰 <b>Edmund's Gold Coins</b><br>King Edmund had 200 gold coins and gave 15% to the Talking Animals. How many did he give?", a:["30"], pts:10, hint:"200 × 0.15"},
  {q:"🛡️ <b>Battle Ready</b><br>Aslan's army had 500 soldiers. 40% carried shields. How many carried shields?", a:["200"], pts:10, hint:"500 × 0.40"},
  {q:"🌿 <b>Narnian Forest</b><br>A forest has 300 trees. 30% are oak trees. How many oak trees?", a:["90"], pts:10, hint:"300 × 0.30"},
  {q:"🐴 <b>Talking Horses</b><br>There are 120 horses in Narnia. 75% are Talking Horses. How many Talking Horses?", a:["90"], pts:10, hint:"120 × 0.75"},

  // ── PERIMETER ──────────────────────────────────────────────────
  {q:"📐 <b>Perimeter Review</b><br>A rectangle is 15 feet long and 10 feet wide. What is its perimeter?", a:["50","50 feet","50ft"], pts:10, hint:"2 × (15 + 10)"},
  {q:"🏰 <b>Cair Paravel Courtyard</b><br>King Peter's courtyard: 40 ft long, 25 ft wide. How many feet of wall surround it?", a:["130","130 feet","130ft"], pts:10, hint:"2 × (40 + 25)"},
  {q:"🌳 <b>The Garden Wall</b><br>Lucy's garden is a square with sides of 8 feet each. What is the perimeter?", a:["32","32 feet","32ft"], pts:10, hint:"4 × 8"},
  {q:"⛵ <b>The Docks</b><br>The Narnian dock is a rectangle 22 meters long and 9 meters wide. What is its perimeter?", a:["62","62 meters","62m"], pts:10, hint:"2 × (22 + 9)"},
  {q:"🏕️ <b>Aslan's Camp</b><br>The camp boundary forms a rectangle 35 ft long and 20 ft wide. How long is the fence around it?", a:["110","110 feet","110ft"], pts:10, hint:"2 × (35 + 20)"},

  // ── AREA ───────────────────────────────────────────────────────
  {q:"📏 <b>Area Review</b><br>A square garden has sides of 9 feet. What is its area?", a:["81","81 sq ft","81 square feet"], pts:10, hint:"9 × 9"},
  {q:"🌸 <b>Aslan's Royal Garden</b><br>A perfect square with each side 12 feet. What is the area?", a:["144","144 sq ft","144 square feet"], pts:10, hint:"12 × 12"},
  {q:"🗺️ <b>The Throne Room</b><br>The throne room is 18 feet long and 14 feet wide. What is its area?", a:["252","252 sq ft","252 square feet"], pts:10, hint:"18 × 14"},
  {q:"🌾 <b>Narnian Wheat Field</b><br>A wheat field is 25 meters long and 16 meters wide. What is its area?", a:["400","400 sq m","400 square meters"], pts:10, hint:"25 × 16"},
  {q:"🏰 <b>The Map Room</b><br>A rectangular map room is 11 ft by 9 ft. What is its area?", a:["99","99 sq ft","99 square feet"], pts:10, hint:"11 × 9"},

  // ── UNIT CONVERSION ────────────────────────────────────────────
  {q:"📏 <b>Unit Conversion</b><br>A bookshelf is 3 feet tall. How many inches? (1 ft = 12 in)", a:["36","36 inches"], pts:10, hint:"3 × 12"},
  {q:"⚔️ <b>Reepicheep's Sword</b><br>Reepicheep is 9 inches tall. His sword is 1 foot long. How many inches longer is the sword?", a:["3","3 inches"], pts:10, hint:"12 − 9"},
  {q:"🏹 <b>The Arrow's Length</b><br>An arrow is 2 feet long. How many inches is that?", a:["24","24 inches"], pts:10, hint:"2 × 12"},
  {q:"🌊 <b>Voyage Distance</b><br>The Dawn Treader sailed 5 miles. How many feet is that? (1 mile = 5,280 feet)", a:["26400","26,400","26400 feet"], pts:10, hint:"5 × 5,280"},
  {q:"🕰️ <b>The Long Winter</b><br>The White Witch's winter lasted 3 years. How many months is that?", a:["36","36 months"], pts:10, hint:"3 × 12"},
  {q:"⏱️ <b>Battle Duration</b><br>The Battle of Beruna lasted 2 hours. How many minutes is that?", a:["120","120 minutes"], pts:10, hint:"2 × 60"},

  // ── TIME ───────────────────────────────────────────────────────
  {q:"⏰ <b>Time Review</b><br>A movie starts at 2:15 PM and runs 1 hour 45 minutes. What time does it end?", a:["4:00","4:00 pm","4 pm","4:00 PM"], pts:10, hint:"2:15 + 1:45"},
  {q:"🌅 <b>Morning Feast</b><br>The feast began at 9:30 AM and lasted 2 hours 15 minutes. What time did it end?", a:["11:45","11:45 am","11:45 AM"], pts:10, hint:"9:30 + 2:15"},
  {q:"🌙 <b>Night Voyage</b><br>The ship set sail at 6:00 PM and sailed for 3 hours 30 minutes. What time did it anchor?", a:["9:30","9:30 pm","9:30 PM"], pts:10, hint:"6:00 + 3:30"},
  {q:"🏰 <b>The Council</b><br>The royal council started at 10:45 AM and ended at 1:15 PM. How long did it last?", a:["2 hours 30 minutes","2.5 hours","2h 30m","150 minutes"], pts:10, hint:"1:15 PM − 10:45 AM"},

  // ── MULTI-STEP ─────────────────────────────────────────────────
  {q:"🔢 <b>Multi-Step Problem</b><br>5 boxes of pencils. Each box: 4 packs. Each pack: 12 pencils. Total pencils?", a:["240"], pts:10, hint:"5 × 4 × 12"},
  {q:"🕯️ <b>Candles for the Feast</b><br>6 tables, each needing 4 candelabras, each holding 8 candles. How many candles total?", a:["192"], pts:10, hint:"6 × 4 × 8"},
  {q:"📦 <b>Supply Crates</b><br>7 ships each carry 5 crates. Each crate holds 9 bags of grain. How many bags total?", a:["315"], pts:10, hint:"7 × 5 × 9"},
  {q:"🌿 <b>Herb Garden</b><br>Lucy planted 4 rows of herbs. Each row has 6 plants. Each plant produces 3 vials of cordial. How many vials total?", a:["72"], pts:10, hint:"4 × 6 × 3"},
  {q:"💎 <b>Treasure Rooms</b><br>Cair Paravel has 3 treasure rooms. Each room has 8 chests. Each chest holds 25 gems. How many gems total?", a:["600"], pts:10, hint:"3 × 8 × 25"},

  // ── DIVISION WITH REMAINDER ────────────────────────────────────
  {q:"🔢 <b>Division Review</b><br>46 students split into groups of 5. How many complete groups, and how many left over?", a:["9 groups, 1 left over","9 groups 1 left over","9r1","9 remainder 1"], pts:10, hint:"46 ÷ 5"},
  {q:"🍎 <b>Apples in Baskets</b><br>50 apples packed into baskets of 7. How many full baskets, and how many apples left over?", a:["7 baskets, 1 left over","7r1","7 remainder 1","7 baskets 1 left"], pts:10, hint:"50 ÷ 7"},
  {q:"⚔️ <b>Sword Bundles</b><br>75 swords bundled in groups of 8. How many full bundles, and how many swords left over?", a:["9 bundles, 3 left over","9r3","9 remainder 3","9 bundles 3 left"], pts:10, hint:"75 ÷ 8"},

  // ── WORD PROBLEMS (MIXED) ──────────────────────────────────────
  {q:"🐴 <b>Hwin's Journey</b><br>Hwin the horse travels 12 miles per hour. How far does she travel in 3 hours?", a:["36","36 miles"], pts:10, hint:"12 × 3"},
  {q:"🌊 <b>Dawn Treader Speed</b><br>The Dawn Treader sails 15 miles per hour. How far in 4 hours?", a:["60","60 miles"], pts:10, hint:"15 × 4"},
  {q:"💰 <b>Market Day</b><br>Peter bought a shield for 45 coins and a sword for 78 coins. He paid with 150 coins. How much change did he get?", a:["27","27 coins"], pts:10, hint:"150 − 45 − 78"},
  {q:"🏹 <b>Susan's Practice</b><br>Susan shot 12 arrows each day for 6 days. She hit the target 58 times. How many times did she miss?", a:["14"], pts:10, hint:"(12 × 6) − 58"},
  {q:"🍞 <b>Feeding the Army</b><br>Each soldier eats 3 loaves per day. There are 24 soldiers. How many loaves are needed for 5 days?", a:["360"], pts:10, hint:"3 × 24 × 5"},
  {q:"🌿 <b>Cordial Doses</b><br>Lucy's cordial heals 1 person per drop. She has 2 bottles with 45 drops each. She's already used 12 drops. How many people can she still heal?", a:["78"], pts:10, hint:"(2 × 45) − 12"},
  {q:"🐐 <b>Mr. Tumnus's Steps</b><br>Mr. Tumnus walks 8 steps per minute on his goat legs. How many steps in 15 minutes?", a:["120"], pts:10, hint:"8 × 15"},
  {q:"🏰 <b>Tower Stairs</b><br>Each tower at Cair Paravel has 36 steps. There are 4 towers. How many steps total?", a:["144"], pts:10, hint:"36 × 4"},
  {q:"💫 <b>Stars in the Sky</b><br>Ramandu counted stars in 6 groups of 13. How many stars total?", a:["78"], pts:10, hint:"6 × 13"},
  {q:"🗡️ <b>Armory Inventory</b><br>The armory had 96 swords. 32 were given to new soldiers. Then 14 more were forged. How many swords now?", a:["78"], pts:10, hint:"96 − 32 + 14"},

  // ── BONUS QUESTIONS (pts:15) ───────────────────────────────────
  {q:"🍬 <b>BONUS ⭐ — Edmund's Turkish Delight</b><br>Room 1: 9 shelves × 12 boxes. Room 2: 6 shelves × 15 boxes. Room 3: 4 shelves × 18 boxes. Each box holds 8 pieces. Total pieces?", a:["1488"], pts:15, hint:"(9×12 + 6×15 + 4×18) × 8 = 270 × 8"},
  {q:"🐉 <b>BONUS ⭐ — Eustace's Dragon Hoard</b><br>8 rings @ 15 coins, 6 goblets @ 24, 12 bags @ 30, 4 necklaces @ 55, 9 swords @ 20. Grand total?", a:["1258","1,258"], pts:15, hint:"(8×15)+(6×24)+(12×30)+(4×55)+(9×20)"},
  {q:"🌊 <b>BONUS ⭐ — The Voyage East</b><br>The Dawn Treader sails 3 legs: 120 miles, 85 miles, 97 miles. Then returns halfway home. Total distance traveled?", a:["453","453 miles"], pts:15, hint:"120+85+97 = 302; return = 302÷2 = 151; 302+151"},
  {q:"🏰 <b>BONUS ⭐ — Castle Renovation</b><br>Cair Paravel has 5 wings. Each wing has 4 floors. Each floor has 8 rooms. Each room needs 3 windows. How many windows total?", a:["480"], pts:15, hint:"5 × 4 × 8 × 3"},
  {q:"💰 <b>BONUS ⭐ — Royal Treasury</b><br>The treasury has 4 chests. Chest 1: 125 coins. Chest 2: 250 coins. Chest 3: double chest 1. Chest 4: half of chest 2. Total coins?", a:["625"], pts:15, hint:"125 + 250 + (2×125) + (250÷2)"},
  {q:"⚔️ <b>BONUS ⭐ — Battle Supplies</b><br>Peter's army: 6 battalions × 24 soldiers each. Each soldier carries 3 weapons and 2 shields. How many total items carried?", a:["720"], pts:15, hint:"6×24 = 144 soldiers; 144 × (3+2) = 144 × 5"}
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
