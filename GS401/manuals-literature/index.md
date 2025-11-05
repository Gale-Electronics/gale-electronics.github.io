---
title: Manuals & Literature
layout: bare
permalink: /GS401/manuals-literature/
nav_exclude: true
---

<h1>Manuals &amp; Literature</h1>
<p>A home for <strong>factory manuals, period write-ups, service notes, and contemporary research</strong> related to the <strong>Gale GS401</strong>.</p>

<h2>Available Scans</h2>

<div class="controls">
  <div class="filter">
    <input id="q" type="search" placeholder="Filter by file name… (e.g. spec, owners, service)" aria-label="Filter scans">
  </div>
  <div class="count" id="count"></div>
</div>

<div class="grid" id="grid">
  {% assign files = site.static_files | where_exp: "f", "f.path contains page.dir" %}
  {% assign images = "" | split: "" %}
  {% for f in files %}
    {% assign ext = f.extname | downcase %}
    {% if ext == '.jpg' or ext == '.jpeg' or ext == '.png' or ext == '.webp' or ext == '.gif' %}
      {%- assign rel = f.path | remove_first: page.dir -%}
      {%- unless rel contains '/' -%}
        {% assign images = images | push: f %}
      {%- endunless -%}
    {% endif %}
  {% endfor %}
  {% assign images = images | sort: "name" %}

  {% if images.size == 0 %}
    <div class="empty">No scans found yet. Add images directly inside <code>{{ page.dir }}</code> (e.g. <code>401-spec-sheet-front.jpg</code>, <code>401-spec-sheet-back.jpg</code>).</div>
  {% else %}
    {% for f in images %}
      {% assign base = f.name | split: "." | first %}
      {% assign caption = base | replace: "-", " " | replace: "_", " " %}
      <button class="card" data-src="{{ f.path }}" data-label="{{ caption }}">
        <img class="thumb" src="{{ f.path }}" alt="{{ caption }}" loading="lazy" decoding="async">
        <div class="meta">
          <span class="label">{{ caption }}</span>
          <span class="chip">Open</span>
        </div>
      </button>
    {% endfor %}
  {% endif %}
</div>

<h2>Coming soon</h2>
<ul>
  <li>Owner’s/Setup guide (searchable)</li>
  <li>Service adjustments</li>
  <li>Crossover theory overview</li>
  <li>Period adverts and reviews (with dates and sources)</li>
  <li>Provenance notes and interview excerpts</li>
</ul>

<div class="cards4">
  <div class="hole"><strong>Owner’s Guide</strong><br><small>Setup, care, transport</small></div>
  <div class="hole"><strong>Service Notes</strong><br><small>Checks, alignments, troubleshooting</small></div>
  <div class="hole"><strong>Period Articles</strong><br><small>Sourced, dated, credited</small></div>
  <div class="hole"><strong>Provenance</strong><br><small>Designers, production notes</small></div>
</div>

<p class="footnote"><small>All materials preserved for educational and historical reference. Rights remain with original authors.</small></p>

<!-- Lightbox -->
<div id="lightbox" aria-hidden="true">
  <button class="lb-close" aria-label="Close">&times;</button>
  <button class="lb-prev" aria-label="Previous">&#10094;</button>
  <figure class="lb-figure">
    <img id="lb-img" alt="">
    <figcaption id="lb-cap"></figcaption>
    <div class="lb-actions">
      <a id="lb-open" href="#" target="_blank" rel="noopener">Open full size</a>
      <a id="lb-download" href="#" download>Download</a>
    </div>
  </figure>
  <button class="lb-next" aria-label="Next">&#10095;</button>
</div>

<style>
  :root{
    --bg:#f7f5ee;
    --card:#ffffff;
    --border:#e5dfc9;
    --ink:#222;
    --muted:#666;
    --accent:#6e9fff; /* Gale blue */
    --shadow:0 6px 18px rgba(0,0,0,.06);
    --radius:14px;
    --wrap:1100px;
  }
  html,body{background:var(--bg);margin:0;padding:0;font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;color:var(--ink)}
  main, .page-content, body > div, body > section{max-width:var(--wrap);margin:22px auto;padding:0 16px}
  h1{font-size:1.9rem;margin:.3em 0 .8em}
  h2{font-size:1.2rem;margin:1.4rem 0 .6rem}

  .controls{display:flex;gap:8px;align-items:center;margin:10px 0 16px}
  .filter{flex:1;display:flex}
  .filter input{width:100%;padding:10px 12px;border:1px solid var(--border);border-radius:10px;background:#fff;font-size:14px}
  .count{font-size:.9rem;color:var(--muted)}

  .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px}
  .card{
    display:block;width:100%;text-align:left;background:var(--card);
    border:1px solid var(--border);border-radius:12px;overflow:hidden;box-shadow:var(--shadow);
    transition:transform .15s ease, box-shadow .2s ease; cursor:pointer;
  }
  .card:hover{transform:translateY(-2px);box-shadow:0 10px 26px rgba(0,0,0,.10)}
  .thumb{width:100%;aspect-ratio:4/3;object-fit:cover;display:block}
  .meta{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:10px 12px;font-size:14px;border-top:1px solid var(--border)}
  .label{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  .chip{font-size:.78rem;color:#0b1b3a;background:#e9f0ff;border:1px solid #d6e3ff;padding:.15rem .45rem;border-radius:999px;white-space:nowrap}

  .cards4{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin:1rem 0}
  .hole{background:#fff;border:1px dashed #ccc;border-radius:10px;padding:1rem;min-height:120px}
  .footnote{margin-top:1rem;color:var(--muted)}

  /* Lightbox */
  #lightbox{
    position:fixed; inset:0; display:none; align-items:center; justify-content:center;
    background:rgba(0,0,0,.85); z-index:9999; padding:24px;
  }
  #lightbox[aria-hidden="false"]{ display:flex; }
  .lb-figure{max-width:min(96vw,1200px); width:100%; text-align:center; color:#fff}
  #lb-img{max-width:100%; max-height:82vh; width:auto; height:auto; border-radius:8px; box-shadow:0 10px 30px rgba(0,0,0,.4)}
  #lb-cap{margin:.6rem 0 0; font-size:.95rem; color:#e8e8e8}
  .lb-actions{margin-top:.6rem; display:flex; gap:10px; justify-content:center}
  .lb-actions a{color:#fff; text-decoration:none; border:1px solid rgba(255,255,255,.5); padding:.35rem .6rem; border-radius:999px}
  .lb-close,.lb-prev,.lb-next{
    position:absolute; top:16px; background:none; border:none; color:#fff; font-size:32px; line-height:1; cursor:pointer; padding:.25rem .5rem;
  }
  .lb-close{ right:18px; }
  .lb-prev,.lb-next{ top:50%; transform:translateY(-50%); font-size:40px; }
  .lb-prev{ left:18px; }
  .lb-next{ right:18px; }
</style>

<script>
(function(){
  // filter + count
  var q = document.getElementById('q');
  var grid = document.getElementById('grid');
  var cards = Array.prototype.slice.call(grid.querySelectorAll('.card'));
  var count = document.getElementById('count');

  function updateCount(){
    var visible = cards.filter(function(c){ return c.style.display !== 'none'; }).length;
    if(count){ count.textContent = visible + ' of ' + cards.length; }
  }
  function filter(){
    var term = (q.value || '').trim().toLowerCase();
    cards.forEach(function(c){
      var name = (c.getAttribute('data-label') || c.textContent || '').toLowerCase();
      var data = (c.getAttribute('data-src') || '').toLowerCase();
      c.style.display = (name.indexOf(term) !== -1 || data.indexOf(term) !== -1) ? '' : 'none';
    });
    updateCount();
  }
  if(q){ q.addEventListener('input', filter); }

  // lightbox
  var lb = document.getElementById('lightbox');
  var lbImg = document.getElementById('lb-img');
  var lbCap = document.getElementById('lb-cap');
  var lbOpen = document.getElementById('lb-open');
  var lbDl = document.getElementById('lb-download');
  var btnClose = lb.querySelector('.lb-close');
  var btnPrev = lb.querySelector('.lb-prev');
  var btnNext = lb.querySelector('.lb-next');

  var i = -1; // current index

  function openAt(idx){
    i = idx;
    var c = cards[i];
    var src = c.getAttribute('data-src') || c.querySelector('img').src;
    var label = c.getAttribute('data-label') || c.querySelector('.label')?.textContent || '';
    lbImg.src = src;
    lbImg.alt = label;
    lbCap.textContent = label;
    lbOpen.href = src;      // open in new tab
    lbDl.href = src;        // optional download button
    lb.setAttribute('aria-hidden','false');
  }
  function closeLB(){ lb.setAttribute('aria-hidden','true'); lbImg.src=''; }

  function prev(){ if(cards.length){ openAt((i - 1 + cards.length) % cards.length); } }
  function next(){ if(cards.length){ openAt((i + 1) % cards.length); } }

  cards.forEach(function(c, idx){
    // store label for filtering convenience
    var labelEl = c.querySelector('.label');
    if(labelEl) c.setAttribute('data-label', labelEl.textContent.trim());
    c.addEventListener('click', function(){ openAt(idx); });
  });

  btnClose.addEventListener('click', closeLB);
  btnPrev.addEventListener('click', prev);
  btnNext.addEventListener('click', next);
  lb.addEventListener('click', function(e){ if(e.target === lb) closeLB(); });

  document.addEventListener('keydown', function(e){
    if(lb.getAttribute('aria-hidden') === 'true') return;
    if(e.key === 'Escape') closeLB();
    if(e.key === 'ArrowLeft') prev();
    if(e.key === 'ArrowRight') next();
  });

  updateCount();
})();
</script>
