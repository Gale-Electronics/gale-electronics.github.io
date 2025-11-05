---
title: Manuals & Literature
layout: bare
permalink: /GS401/manuals-literature/
nav_exclude: true
---

<h1>Manuals &amp; Literature</h1>
<p>A home for <strong>factory manuals, period write-ups, service notes, and contemporary research</strong> related to the <strong>Gale GS401</strong>.</p>

<div class="notice">
  <strong>Under construction</strong><br>
  We’re cleaning scans and extracting searchable text. When available, we’ll post accessible HTML summaries alongside original scans.
</div>

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
      <a href="{{ f.path }}" class="card" data-name="{{ f.name | downcase }}" download>
        <img class="thumb" src="{{ f.path }}" alt="{{ caption }}" loading="lazy" decoding="async">
        <div class="meta">
          <span class="label">{{ caption }}</span>
          <span class="chip">Download JPG</span>
        </div>
      </a>
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

  .notice{
    background:#fff3cd;border:1px solid #ffeeba;border-radius:.5rem;padding:1rem;margin:1.2rem 0;
  }

  .controls{display:flex;gap:8px;align-items:center;margin:10px 0 16px}
  .filter{flex:1;display:flex}
  .filter input{width:100%;padding:10px 12px;border:1px solid var(--border);border-radius:10px;background:#fff;font-size:14px}
  .count{font-size:.9rem;color:var(--muted)}

  .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:14px}
  .card{
    display:block;text-decoration:none;color:inherit;background:var(--card);
    border:1px solid var(--border);border-radius:12px;overflow:hidden;box-shadow:var(--shadow);
    transition:transform .15s ease, box-shadow .2s ease;
  }
  .card:hover{transform:translateY(-2px);box-shadow:0 10px 26px rgba(0,0,0,.10)}
  .thumb{width:100%;aspect-ratio:4/3;object-fit:cover;display:block}
  .meta{
    display:flex;align-items:center;justify-content:space-between;gap:10px;
    padding:10px 12px;font-size:14px;border-top:1px solid var(--border)
  }
  .label{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  .chip{font-size:.78rem;color:#0b1b3a;background:#e9f0ff;border:1px solid #d6e3ff;padding:.15rem .45rem;border-radius:999px;white-space:nowrap}

  .cards4{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin:1rem 0}
  .hole{background:#fff;border:1px dashed #ccc;border-radius:10px;padding:1rem;min-height:120px}

  .footnote{margin-top:1rem;color:var(--muted)}
</style>

<script>
  (function(){
    var q = document.getElementById('q');
    var grid = document.getElementById('grid');
    if(!grid) return;
    var cards = Array.prototype.slice.call(grid.querySelectorAll('.card'));
    var count = document.getElementById('count');

    function updateCount(){
      var visible = cards.filter(function(c){ return c.style.display !== 'none'; }).length;
      if(count){ count.textContent = visible + ' of ' + cards.length; }
    }
    function filter(){
      var term = (q.value || '').trim().toLowerCase();
      cards.forEach(function(c){
        var name = (c.getAttribute('data-name') || '').toLowerCase();
        c.style.display = name.indexOf(term) !== -1 ? '' : 'none';
      });
      updateCount();
    }
    if(q){ q.addEventListener('input', filter); }
    updateCount();
  })();
</script>
