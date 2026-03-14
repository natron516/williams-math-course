#!/usr/bin/env python3
"""Add YouTube video links to each lesson in lesson-plans.html"""

import re

# Video mapping: session number -> list of (title, youtube_id, channel)
VIDEOS = {
    1: [
        ("Acute, Right & Obtuse Angles", "4ZyTVTGVPgE", "Khan Academy"),
        ("Math Antics — Angles & Degrees", "4r_j10jtavU", "Math Antics"),
    ],
    2: [
        ("Supplementary & Complementary Angles", "TzT_HtojVOU", "Math Antics"),
        ("Vertical Angles", "WN2E-KMuXoE", "Math Antics"),
    ],
    3: [
        ("Triangles", "oQeK4LyKLHw", "Math Antics"),
        ("Polygons", "ZJnKPl99fTs", "Math Antics"),
    ],
    4: [
        ("Perimeter", "AAY1bsazcgM", "Math Antics"),
    ],
    5: [
        ("Area (Rectangles & Triangles)", "xCdxURXMdFY", "Math Antics"),
    ],
    6: [
        ("Area (Parallelograms & Trapezoids)", "SEXLRQol970", "Khan Academy"),
        ("Composite Shapes Area", "5UIbpphAz-U", "FrysMath"),
    ],
    7: [
        ("Circles: Circumference & Area", "5cbFN2wOUFY", "Math Antics"),
    ],
    8: [
        ("Circles: Circumference & Area", "5cbFN2wOUFY", "Math Antics"),
    ],
    9: [
        ("Area of Composite Shapes", "L8W3ch_Zrmk", "Math Turtle"),
        ("Composite Shapes Review", "5UIbpphAz-U", "FrysMath"),
    ],
    10: [
        ("Volume", "-05rNRCHkhQ", "Math Antics"),
    ],
    11: [
        ("Volume (Cylinders)", "-05rNRCHkhQ", "Math Antics"),
        ("Surface Area", "kSj_Wo5hdVU", "Math Antics"),
    ],
    12: [],  # Test day
    13: [
        ("What Is Algebra?", "NybHckSEQBI", "Math Antics"),
        ("Evaluating Expressions", "52tpYl2tTqk", "Math Antics"),
    ],
    14: [
        ("Combining Like Terms", "y7GwRJOIohM", "Math Antics"),
    ],
    15: [
        ("Order of Operations", "dAgfnK528RA", "Math Antics"),
    ],
    16: [
        ("Solving Equations Part 1 (+/−)", "l3XzepN03KQ", "Math Antics"),
    ],
    17: [
        ("Solving Equations Part 2 (×/÷)", "Qyd_v3DGzTM", "Math Antics"),
    ],
    18: [
        ("Solving Equations Part 1", "l3XzepN03KQ", "Math Antics"),
        ("Solving Equations Part 2", "Qyd_v3DGzTM", "Math Antics"),
    ],
    19: [
        ("Solving 2-Step Equations", "LDIiYKYvvdA", "Math Antics"),
    ],
    20: [
        ("Basic Inequalities", "mgHO-bsCDrA", "Math Antics"),
        ("Inequalities in Algebra", "RyesLifeUBw", "Math Antics"),
    ],
    21: [],  # Test day
    22: [
        ("Graphing on the Coordinate Plane", "3JqndcNQPYs", "Math Antics"),
    ],
    23: [
        ("Basic Linear Functions", "MXV65i9g1Xg", "Math Antics"),
        ("Graphing on Coordinate Plane", "3JqndcNQPYs", "Math Antics"),
    ],
    24: [],  # Final test day
}

# Read the lesson-plans.html
with open("/tmp/math-deploy/lesson-plans.html", "r") as f:
    content = f.read()

# Add a video property to each lesson object in the JS
# We need to add a 'vid' field to each lesson and update the template

# Build video data as JS
vid_entries = []
for s in range(1, 25):
    vids = VIDEOS.get(s, [])
    if vids:
        items = ",".join([f'{{t:"{t}",id:"{vid}",ch:"{ch}"}}' for t, vid, ch in vids])
        vid_entries.append(f"{s}:[{items}]")

vid_js = "{" + ",".join(vid_entries) + "}"

# Add video section CSS
video_css = """
        .video-section { margin-top: 10px; }
        .video-card { display: flex; align-items: center; gap: 12px; padding: 10px 14px;
                     margin: 8px 0; background: #FFF0F0; border-radius: 10px;
                     border: 1px solid #FFCDD2; text-decoration: none; color: #333;
                     transition: all 0.2s; cursor: pointer; }
        .video-card:hover { background: #FFE0E0; transform: translateX(4px);
                          box-shadow: 0 2px 8px rgba(244,67,54,0.15); }
        .video-thumb { width: 80px; height: 45px; border-radius: 6px; background: #000;
                      position: relative; overflow: hidden; flex-shrink: 0; }
        .video-thumb img { width: 100%; height: 100%; object-fit: cover; }
        .video-play { position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%);
                     color: white; font-size: 1.4em; text-shadow: 0 1px 3px rgba(0,0,0,0.5); }
        .video-info h4 { font-size: 0.95em; color: #C62828; }
        .video-info p { font-size: 0.78em; color: #888; margin-top: 2px; }
"""

# Inject CSS
content = content.replace(
    "@media (max-width: 600px) { .diff-box { grid-template-columns: 1fr; } }",
    "@media (max-width: 600px) { .diff-box { grid-template-columns: 1fr; } }" + video_css
)

# Add video data and rendering to the JS
video_render_js = f"""
const videoData = {vid_js};

function renderVideos(sessionNum) {{
    const vids = videoData[sessionNum];
    if (!vids || vids.length === 0) return '';
    let html = '<div class="lesson-section"><h3>🎬 Video Examples</h3><div class="video-section">';
    html += '<p style="font-size:0.85em;color:#888;margin-bottom:8px;">Play these on the TV during direct instruction or as warm-up:</p>';
    vids.forEach(v => {{
        html += `<a class="video-card" href="https://www.youtube.com/watch?v=${{v.id}}" target="_blank">
            <div class="video-thumb">
                <img src="https://img.youtube.com/vi/${{v.id}}/mqdefault.jpg" alt="" loading="lazy"/>
                <span class="video-play">▶</span>
            </div>
            <div class="video-info">
                <h4>${{v.t}}</h4>
                <p>${{v.ch}} · YouTube</p>
            </div>
        </a>`;
    }});
    html += '</div></div>';
    return html;
}}
"""

# Inject video JS before the lessons array
content = content.replace("const lessons = [", video_render_js + "\nconst lessons = [")

# Update the lesson template to include videos after warm-up
content = content.replace(
    '<div class="lesson-section"><h3>📖 Direct Instruction</h3>',
    '${renderVideos(l.s)}\n        <div class="lesson-section"><h3>📖 Direct Instruction</h3>'
)

with open("/tmp/math-deploy/lesson-plans.html", "w") as f:
    f.write(content)

print("✅ Added YouTube video links to all 24 lesson plans")
print(f"   {sum(len(v) for v in VIDEOS.values())} total videos across {sum(1 for v in VIDEOS.values() if v)} sessions")
