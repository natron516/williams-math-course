/* Scratch Pad — mini drawing canvas for any problem card */
(function(){
  const CSS = `
    .sp-btn { position:absolute; top:10px; right:10px; width:34px; height:34px; border-radius:50%;
              background:#F3E5F5; border:2px solid #E0D0E8; cursor:pointer; display:flex;
              align-items:center; justify-content:center; font-size:1.1em; z-index:10;
              transition:all 0.15s; box-shadow:0 1px 4px rgba(0,0,0,0.06); }
    .sp-btn:hover { background:#E8DEF8; transform:scale(1.1); }
    .sp-btn.active { background:#C06C84; border-color:#C06C84; }
    .sp-btn.active::after { content:'✏️'; }
    .sp-btn::after { content:'✏️'; }
    .sp-overlay { display:none; position:relative; margin:8px 0 4px; border-radius:12px; overflow:hidden;
                  border:2px solid #E8DEF8; background:#FDFBFF; }
    .sp-overlay.open { display:block; }
    .sp-toolbar { display:flex; gap:6px; padding:6px 10px; background:#FAF5F7; border-bottom:1px solid #f0e0e6;
                  align-items:center; flex-wrap:wrap; }
    .sp-toolbar button { padding:4px 10px; border-radius:6px; border:1.5px solid #E0D0E8; background:white;
                         font-size:0.75em; font-weight:700; font-family:'Nunito',sans-serif; cursor:pointer;
                         color:#6B4460; transition:all 0.1s; }
    .sp-toolbar button:hover { background:#F3E5F5; }
    .sp-toolbar button.active { background:#C06C84; color:white; border-color:#C06C84; }
    .sp-toolbar .sp-color { width:22px; height:22px; border-radius:50%; border:2px solid #ddd;
                            cursor:pointer; transition:transform 0.1s; }
    .sp-toolbar .sp-color:hover { transform:scale(1.15); }
    .sp-toolbar .sp-color.active { border-color:#333; border-width:3px; }
    .sp-canvas { display:block; width:100%; touch-action:none; cursor:crosshair; }
  `;

  const style = document.createElement('style');
  style.textContent = CSS;
  document.head.appendChild(style);

  const COLORS = ['#333','#C06C84','#1565C0','#2E7D32','#E65100'];
  const SIZES = [{label:'S',w:2},{label:'M',w:4},{label:'L',w:7}];

  function initCard(card, idx) {
    card.style.position = 'relative';

    // Toggle button
    const btn = document.createElement('div');
    btn.className = 'sp-btn';
    btn.title = 'Scratch Pad';
    card.insertBefore(btn, card.firstChild);

    // Overlay
    const overlay = document.createElement('div');
    overlay.className = 'sp-overlay';

    // Toolbar
    const toolbar = document.createElement('div');
    toolbar.className = 'sp-toolbar';

    let currentColor = COLORS[0];
    let currentSize = SIZES[1].w;
    let isEraser = false;

    // Colors
    COLORS.forEach((c,i) => {
      const dot = document.createElement('div');
      dot.className = 'sp-color' + (i===0?' active':'');
      dot.style.background = c;
      dot.onclick = () => {
        toolbar.querySelectorAll('.sp-color').forEach(d=>d.classList.remove('active'));
        dot.classList.add('active');
        currentColor = c;
        isEraser = false;
        toolbar.querySelector('.sp-eraser')?.classList.remove('active');
      };
      toolbar.appendChild(dot);
    });

    // Sizes
    SIZES.forEach((s,i) => {
      const b = document.createElement('button');
      b.textContent = s.label;
      if(i===1) b.classList.add('active');
      b.onclick = () => {
        toolbar.querySelectorAll('.sp-size').forEach(x=>x.classList.remove('active'));
        b.classList.add('active');
        currentSize = s.w;
      };
      b.className += ' sp-size';
      toolbar.appendChild(b);
    });

    // Eraser
    const eraser = document.createElement('button');
    eraser.textContent = '🧹 Eraser';
    eraser.className += ' sp-eraser';
    eraser.onclick = () => {
      isEraser = !isEraser;
      eraser.classList.toggle('active', isEraser);
    };
    toolbar.appendChild(eraser);

    // Clear
    const clear = document.createElement('button');
    clear.textContent = '🗑 Clear';
    clear.onclick = () => {
      const c2 = canvas.getContext('2d');
      c2.clearRect(0,0,canvas.width,canvas.height);
    };
    toolbar.appendChild(clear);

    overlay.appendChild(toolbar);

    // Canvas
    const canvas = document.createElement('canvas');
    canvas.className = 'sp-canvas';
    canvas.height = 200;
    overlay.appendChild(canvas);

    // Insert overlay after card-head (or at start of card-body)
    const cardBody = card.querySelector('.card-body');
    if (cardBody) {
      cardBody.insertBefore(overlay, cardBody.firstChild);
    } else {
      card.appendChild(overlay);
    }

    // Toggle
    btn.onclick = () => {
      overlay.classList.toggle('open');
      btn.classList.toggle('active');
      if (overlay.classList.contains('open') && canvas.width < 10) {
        resizeCanvas();
      }
    };

    function resizeCanvas() {
      const w = overlay.clientWidth;
      canvas.width = w;
      canvas.height = 200;
    }

    // Drawing logic
    let drawing = false;
    let lastX, lastY;
    const ctx = canvas.getContext('2d');
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';

    function getPos(e) {
      const r = canvas.getBoundingClientRect();
      const t = e.touches ? e.touches[0] : e;
      return [t.clientX - r.left, t.clientY - r.top];
    }

    function down(e) {
      drawing = true;
      [lastX, lastY] = getPos(e);
      e.preventDefault();
    }
    function move(e) {
      if (!drawing) return;
      const [x,y] = getPos(e);
      ctx.beginPath();
      ctx.moveTo(lastX, lastY);
      ctx.lineTo(x, y);
      if (isEraser) {
        ctx.globalCompositeOperation = 'destination-out';
        ctx.lineWidth = currentSize * 4;
      } else {
        ctx.globalCompositeOperation = 'source-over';
        ctx.strokeStyle = currentColor;
        ctx.lineWidth = currentSize;
      }
      ctx.stroke();
      [lastX, lastY] = [x, y];
      e.preventDefault();
    }
    function up() { drawing = false; }

    canvas.addEventListener('mousedown', down);
    canvas.addEventListener('mousemove', move);
    canvas.addEventListener('mouseup', up);
    canvas.addEventListener('mouseleave', up);
    canvas.addEventListener('touchstart', down, {passive:false});
    canvas.addEventListener('touchmove', move, {passive:false});
    canvas.addEventListener('touchend', up);

    // Resize observer
    new ResizeObserver(() => {
      if (overlay.classList.contains('open')) resizeCanvas();
    }).observe(overlay);
  }

  // Init all cards on page load
  function init() {
    document.querySelectorAll('.card').forEach((card, i) => initCard(card, i));
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
