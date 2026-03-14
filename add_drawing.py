#!/usr/bin/env python3
"""Add drawing canvas capability to all 'show your work' areas across all HTML files."""

import os, re

BASE = "/tmp/math-deploy"

# The drawing canvas component - injected as a shared script
DRAWING_SCRIPT = '''<script>
// Drawing Canvas System
(function() {
    let canvasId = 0;
    
    // Replace all work-area textareas with hybrid draw+type areas
    document.querySelectorAll('.work-area').forEach(ta => {
        const id = 'canvas_' + (canvasId++);
        const wrapper = document.createElement('div');
        wrapper.className = 'work-wrapper';
        wrapper.style.cssText = 'margin:8px 0 5px 42px; width:calc(100% - 42px);';
        
        wrapper.innerHTML = `
            <div class="work-tabs">
                <button class="work-tab active" onclick="switchWorkTab(this,'draw')">✏️ Draw</button>
                <button class="work-tab" onclick="switchWorkTab(this,'type')">⌨️ Type</button>
                <div class="draw-tools" id="tools_${id}">
                    <button class="tool-btn active" onclick="setTool(this,'${id}','pen')" title="Pen">🖊️</button>
                    <button class="tool-btn" onclick="setTool(this,'${id}','eraser')" title="Eraser">🧽</button>
                    <input type="color" value="#333333" onchange="setColor('${id}',this.value)" 
                           style="width:28px;height:28px;border:none;border-radius:4px;cursor:pointer;" title="Color"/>
                    <select onchange="setSize('${id}',this.value)" style="padding:2px 4px;border-radius:4px;border:1px solid #ddd;font-size:0.8em;">
                        <option value="2">Fine</option>
                        <option value="3" selected>Medium</option>
                        <option value="5">Thick</option>
                    </select>
                    <button class="tool-btn" onclick="undoDraw('${id}')" title="Undo">↩️</button>
                    <button class="tool-btn" onclick="clearCanvas('${id}')" title="Clear All">🗑️</button>
                </div>
            </div>
            <div class="draw-panel" id="drawPanel_${id}">
                <canvas id="${id}" width="600" height="160" 
                        style="width:100%;border:1.5px solid #e0e0e0;border-radius:8px;
                               background:white;touch-action:none;cursor:crosshair;"></canvas>
            </div>
            <div class="type-panel" id="typePanel_${id}" style="display:none;">
                <textarea class="work-area-text" placeholder="Type your work here..."
                          style="width:100%;min-height:80px;border:1.5px solid #e0e0e0;border-radius:8px;
                                 padding:10px;font-family:Nunito,sans-serif;font-size:0.9em;resize:vertical;
                                 outline:none;color:#444;"></textarea>
            </div>
        `;
        
        ta.parentNode.replaceChild(wrapper, ta);
        
        // Initialize canvas
        setTimeout(() => initCanvas(id), 50);
    });
    
    // Canvas state storage
    window._canvasState = {};
    
    window.initCanvas = function(id) {
        const canvas = document.getElementById(id);
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        
        // Set actual pixel size based on display size
        const rect = canvas.getBoundingClientRect();
        canvas.width = rect.width * 2;
        canvas.height = rect.height * 2;
        ctx.scale(2, 2);
        
        const state = {
            drawing: false,
            tool: 'pen',
            color: '#333333',
            size: 3,
            history: [],
            ctx: ctx,
            canvas: canvas,
            lastX: 0, lastY: 0
        };
        window._canvasState[id] = state;
        
        // Save initial blank state
        saveHistory(id);
        
        // Pointer events (works with touch, pencil, and mouse)
        canvas.addEventListener('pointerdown', e => startDraw(e, id));
        canvas.addEventListener('pointermove', e => draw(e, id));
        canvas.addEventListener('pointerup', e => endDraw(e, id));
        canvas.addEventListener('pointerleave', e => endDraw(e, id));
        
        // Prevent scroll while drawing
        canvas.addEventListener('touchstart', e => e.preventDefault(), {passive: false});
        canvas.addEventListener('touchmove', e => e.preventDefault(), {passive: false});
    };
    
    function getPos(e, canvas) {
        const rect = canvas.getBoundingClientRect();
        return {
            x: (e.clientX - rect.left),
            y: (e.clientY - rect.top)
        };
    }
    
    window.startDraw = function(e, id) {
        const s = window._canvasState[id];
        s.drawing = true;
        const pos = getPos(e, s.canvas);
        s.lastX = pos.x;
        s.lastY = pos.y;
        s.ctx.beginPath();
        s.ctx.moveTo(pos.x, pos.y);
    };
    
    window.draw = function(e, id) {
        const s = window._canvasState[id];
        if (!s.drawing) return;
        const pos = getPos(e, s.canvas);
        
        s.ctx.lineWidth = s.tool === 'eraser' ? s.size * 4 : s.size;
        s.ctx.lineCap = 'round';
        s.ctx.lineJoin = 'round';
        s.ctx.strokeStyle = s.tool === 'eraser' ? '#ffffff' : s.color;
        s.ctx.globalCompositeOperation = s.tool === 'eraser' ? 'destination-out' : 'source-over';
        
        // Use pressure for Apple Pencil if available
        if (e.pressure && e.pressure > 0 && e.pressure < 1) {
            s.ctx.lineWidth *= (0.5 + e.pressure);
        }
        
        s.ctx.lineTo(pos.x, pos.y);
        s.ctx.stroke();
        s.ctx.beginPath();
        s.ctx.moveTo(pos.x, pos.y);
        s.lastX = pos.x;
        s.lastY = pos.y;
    };
    
    window.endDraw = function(e, id) {
        const s = window._canvasState[id];
        if (s.drawing) {
            s.drawing = false;
            s.ctx.globalCompositeOperation = 'source-over';
            saveHistory(id);
        }
    };
    
    function saveHistory(id) {
        const s = window._canvasState[id];
        const imgData = s.canvas.toDataURL();
        s.history.push(imgData);
        if (s.history.length > 20) s.history.shift(); // limit memory
    }
    
    window.undoDraw = function(id) {
        const s = window._canvasState[id];
        if (s.history.length > 1) {
            s.history.pop();
            const img = new Image();
            img.onload = () => {
                s.ctx.clearRect(0, 0, s.canvas.width/2, s.canvas.height/2);
                s.ctx.drawImage(img, 0, 0, s.canvas.width/2, s.canvas.height/2);
            };
            img.src = s.history[s.history.length - 1];
        }
    };
    
    window.clearCanvas = function(id) {
        const s = window._canvasState[id];
        s.ctx.clearRect(0, 0, s.canvas.width/2, s.canvas.height/2);
        saveHistory(id);
    };
    
    window.setTool = function(btn, id, tool) {
        window._canvasState[id].tool = tool;
        btn.parentElement.querySelectorAll('.tool-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const canvas = document.getElementById(id);
        canvas.style.cursor = tool === 'eraser' ? 'cell' : 'crosshair';
    };
    
    window.setColor = function(id, color) {
        window._canvasState[id].color = color;
    };
    
    window.setSize = function(id, size) {
        window._canvasState[id].size = parseInt(size);
    };
    
    window.switchWorkTab = function(btn, mode) {
        const wrapper = btn.closest('.work-wrapper');
        wrapper.querySelectorAll('.work-tab').forEach(t => t.classList.remove('active'));
        btn.classList.add('active');
        
        const drawPanel = wrapper.querySelector('[id^="drawPanel_"]');
        const typePanel = wrapper.querySelector('[id^="typePanel_"]');
        const tools = wrapper.querySelector('[id^="tools_"]');
        
        if (mode === 'draw') {
            drawPanel.style.display = 'block';
            typePanel.style.display = 'none';
            tools.style.display = 'flex';
            // Resize canvas on show
            const canvasEl = drawPanel.querySelector('canvas');
            if (canvasEl && window._canvasState[canvasEl.id]) {
                const rect = canvasEl.getBoundingClientRect();
                if (rect.width > 0) {
                    // Don't resize if already initialized properly
                }
            }
        } else {
            drawPanel.style.display = 'none';
            typePanel.style.display = 'block';
            tools.style.display = 'none';
        }
    };
})();
</script>'''

DRAWING_CSS = '''<style>
.work-wrapper { position: relative; }
.work-tabs { display: flex; align-items: center; gap: 4px; margin-bottom: 6px; }
.work-tab { padding: 6px 14px; border: 1.5px solid #e0e0e0; border-radius: 8px 8px 0 0;
            background: #f5f5f5; cursor: pointer; font-family: 'Nunito', sans-serif;
            font-size: 0.85em; font-weight: 600; color: #888; transition: all 0.2s; border-bottom: none; }
.work-tab.active { background: white; color: #2E75B6; border-color: #2E75B6; }
.draw-tools { display: flex; align-items: center; gap: 6px; margin-left: auto;
              padding: 3px 8px; background: #f8f9fa; border-radius: 8px; }
.tool-btn { background: none; border: 1.5px solid transparent; padding: 3px 6px;
            border-radius: 6px; cursor: pointer; font-size: 1em; transition: all 0.2s; }
.tool-btn.active { border-color: #2E75B6; background: #e8f0fe; }
.tool-btn:hover { background: #e8e8e8; }
.draw-panel canvas { display: block; }
@media (max-width: 600px) {
    .draw-tools { flex-wrap: wrap; gap: 4px; }
    .work-tabs { flex-wrap: wrap; }
}
</style>'''

def add_drawing_to_file(filepath):
    """Add drawing canvas capability to an HTML file."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Skip if already has drawing canvas
    if '_canvasState' in content:
        return False
    
    # Skip if no work areas
    if 'work-area' not in content:
        return False
    
    # Add CSS before closing </style> or before </head>
    if '</style>' in content:
        # Add before the last </style>
        idx = content.rfind('</style>')
        content = content[:idx] + DRAWING_CSS.replace('<style>', '').replace('</style>', '') + content[idx:]
    elif '</head>' in content:
        content = content.replace('</head>', DRAWING_CSS + '</head>')
    
    # Add script before closing </body>
    if '</body>' in content:
        content = content.replace('</body>', DRAWING_SCRIPT + '\n</body>')
    elif '</html>' in content:
        content = content.replace('</html>', DRAWING_SCRIPT + '\n</html>')
    else:
        content += DRAWING_SCRIPT
    
    with open(filepath, 'w') as f:
        f.write(content)
    return True

# Process all HTML files
count = 0
for folder in ['worksheets', 'quizzes', 'tests']:
    folder_path = os.path.join(BASE, folder)
    if not os.path.exists(folder_path):
        continue
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith('.html'):
            filepath = os.path.join(folder_path, filename)
            if add_drawing_to_file(filepath):
                count += 1
                print(f"  ✏️ {filename}")
            else:
                print(f"  ⏭️  {filename} (skipped — no work areas or already done)")

print(f"\n✅ Added drawing canvas to {count} files")
