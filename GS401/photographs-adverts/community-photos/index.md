---
title: Community Photos
layout: bare
permalink: /GS401/photographs-adverts/community-photos/
---

<div class="wrap">
  <div class="toprow">
    <div class="back"><a href="/GS401/photographs-adverts/">&larr; Back to GS401 — Photographs & Adverts</a></div>
    <div class="hint">Images below are listed automatically from this folder. Use filenames to include credits (e.g. <code>1974-show__credit-jane-doe.jpg</code>).</div>
  </div>

  <h1>GS401 — Community Photos</h1>

  <div class="controls">
    <div class="filter">
      <input id="q" type="search" placeholder="Filter by file name… (e.g. 401A, chrome, living-room, jane doe)">
    </div>
    <div class="count" id="count"></div>
  </div>

  {% assign files = site.static_files | where_exp: "f", "f.path contains page.dir" %}
  {% assign images = "" | split: "" %}
  {% for f in files %}
    {% assign ext = f.extname | downcase %}
    {% if ext == '.jpg' or ext == '.jpeg' or ext == '.png' or ext == '.webp' or ext == '.gif' %}
      {%- assign rel = f.path | remove_first: page.dir -%}
      {%- unless rel contains '/' -%}  {# only files directly in this folder #}
        {% assign images = images | push: f %}
      {%- endunless -%}
    {% endif %}
  {% endfor %}
  {% assign images = images | sort: "name" %}

  <div class="grid" id="grid">
  {% if images.size == 0 %}
    <div class="empty">No images found yet. Add <code>.jpg</code>, <code>.png</code>, <code>.webp</code> or <code>.gif</code> files directly inside <code>{{ page.dir }}</code>.</div>
  {% else %}
    {% for f in images %}
      {% assign base = f.name | split: "." | first %}
      {% comment %} turn "my-photo__credit-jane-doe" into nice caption + credit {% endcomment %}
      {% assign parts = base | split: '__credit-' %}
      {% assign name_part = parts[0] %}
      {% assign credit_part = parts[1] | default: "" %}
      {% assign caption = name_part | replace: "-", " " | replace: "_", " " %}
      <a href="{{ f.path }}" class="card" data-name="{{ f.name | downcase }}">
        <img class="thumb" src="{{ f.path }}" alt="{{ caption }}" loading="lazy" decoding="async">
        <div class="meta">
          <span class="label">{{ caption }}</span>
          {% if credit_part != "" %}
            <span class="chip">© {{ credit_part | replace: "-", " " | replace: "_", " " }}</span>
          {% endif %}
        </div>
      </a>
    {% endfor %}
  {% endif %}
  </div>
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
  .wrap{max-width:var(--wrap);margin:22px auto;padding:0 16px}
  h1{font-size:1.9rem;margin:.3em 0 .8em}

  .toprow{display:flex;gap:12px;align-items:center;justify-content:space-between;margin-bottom:12px}
  .back a{color:var(--accent);text-decoration:none}
  .hint{font-size:.9rem;color:var(--muted)}

  .controls{display:flex;gap:8px;align-items:center;margin:10px 0 16px}
  .filter{flex:1;display:flex}
  .filter input{width:100%;padding:10px 12px;border:1px solid var(--border);border-radius:10px;background:#fff;font-size:14px}
  .count{font-size:.9rem;color:var(--muted)}

  .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:14px}
  .card{
    background:var(--card);
    border:1px solid var(--border);
    border-radius:12px;
    overflow:hidden;
    text-align:left;
    box-shadow:var(--shadow);
    transition:transform .15s ease, box-shadow .2s ease;
  }
  .card:hover{transform:translateY(-2px);box-shadow:0 10px 26px rgba(0,0,0,.10)}
  .thumb{width:100%;aspect-ratio:4/3;object-fit:cover;display:block}
  .meta{
    display:flex;align-items:center;justify-content:space-between;
    gap:10px;padding:10px 12px;font-size:14px;border-top:1px solid var(--border)
  }
  .label{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  .chip{
    font-size:.78rem;color:#0b1b3a;background:#e9f0ff;border:1px solid #d6e3ff;
    padding:.15rem .45rem;border-radius:999px;white-space:nowrap
  }
  .empty{padding:14px 12px;border:1px dashed var(--border);border-radius:10px;background:#fff}
</style>

<script>
  (function(){
    var q = document.getElementById('q');
    var grid = document.getElementById('grid');
    var cards = Array.prototype.slice.call(grid.querySelectorAll('.card'));
    var count = document.getElementById('count');

    function updateCount(){
      var visible = cards.filter(function(c){ return c.style.display !== 'none'; }).length;
      count.textContent = visible + ' of ' + cards.length;
    }
    function filter(){
      var term = (q.value || '').trim().toLowerCase();
      cards.forEach(function(c){
        var name = (c.getAttribute('data-name') || '').toLowerCase();
        c.style.display = name.indexOf(term) !== -1 ? '' : 'none';
      });
      updateCount();
    }
    var q = document.getElementById('q');
    if(q){ q.addEventListener('input', filter); }
    updateCount();
  })();
</script>
