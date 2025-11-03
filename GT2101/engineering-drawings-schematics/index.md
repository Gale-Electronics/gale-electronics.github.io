---
layout: bare   # or bare if you actually have _layouts/bare.html
title: GT2101 — Engineering Drawings & Schematics
permalink: /GT2101/engineering-drawings-schematics/
base: /GT2101/engineering-drawings-schematics/  # must be exact, case-sensitive, trailing slash
---

# {{ page.title }}

A living archive of the GT2101 motor stack: reverse-engineered schematics, board layouts, high-res photos and bench notes.  
Everything sits under `{{ page.base }}` and is organised by disk/board.

<style>
  html{scroll-behavior:smooth}
  h1{font-size:1.9rem;margin:.2em 0 .6em}
  h2{font-size:1.2rem;margin:1.4em 0 .6em}
  .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:14px}
  .card{background:#fff;border:1px solid #ddd;border-radius:10px;overflow:hidden;text-align:center;text-decoration:none;color:inherit}
  .card img{width:100%;aspect-ratio:4/3;object-fit:cover}
  .label{padding:6px 8px;font-size:14px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  .pdf{font-size:80px;line-height:1.2;padding:30px 0}
  .folders{display:flex;flex-wrap:wrap;gap:10px;margin:.6em 0 1.2em}
  .folders a{background:#fff;border:1px solid #ddd;border-radius:999px;padding:.35em .7em;text-decoration:none;color:#111;font-size:.95rem}
  details.debug{margin:1.5rem 0;padding:0.75rem;border:1px dashed #ccc;background:#fafafa}
  details.debug summary{cursor:pointer;font-weight:600}
  code.block{display:block;white-space:pre-wrap;font-family:ui-monospace, SFMono-Regular, Menlo, monospace}
</style>

{% assign allowed_exts = "jpg,jpeg,png,webp,pdf" | split: "," %}

{%- comment -%} Gather static files under page.base (safe-mode friendly) {%- endcomment -%}
{% assign under_base = "" | split: "" %}
{% for f in site.static_files %}
  {% if f.path contains page.base %}
    {% assign under_base = under_base | push: f %}
  {% endif %}
{% endfor %}

{%- comment -%} Build folder list from first segment after base {%- endcomment -%}
{% assign folder_marks = "" %}
{% for f in under_base %}
  {% assign rel = f.path | remove_first: page.base %}
  {% if rel contains "/" %}
    {% assign first = rel | split:"/" | first %}
    {% assign mark = first | append:"|" %}
    {% unless folder_marks contains mark %}
      {% assign folder_marks = folder_marks | append: mark %}
    {% endunless %}
  {% endif %}
{% endfor %}
{% assign folders = folder_marks | split:"|" | sort %}

{%- comment -%} Quick links {%- endcomment -%}
{% if folders.size > 0 %}
  <h2>Quick links</h2>
  <div class="folders">
    {% for folder in folders %}
      {% if folder != "" %}
        <a href="#{{ folder | slugify: 'pretty' }}">{{ folder | replace:'_',' ' }}</a>
      {% endif %}
    {% endfor %}
  </div>
{% endif %}

{%- comment -%} Root files (directly in base) {%- endcomment -%}
{% assign root_files = "" | split: "" %}
{% for f in under_base %}
  {% assign rel = f.path | remove_first: page.base %}
  {% unless rel contains "/" %}
    {% assign root_files = root_files | push: f %}
  {% endunless %}
{% endfor %}

{% if root_files.size > 0 %}
  <h2 id="root">Root</h2>
  <div class="grid">
    {% for f in root_files %}
      {% assign filename = f.path | split:"/" | last %}
      {% assign ext = filename | split:"." | last | downcase %}
      {% if allowed_exts contains ext %}
        {% assign name = filename | remove: "." | split: ext | first | replace:"_"," " %}
        {% if ext == "pdf" %}
          <a href="{{ f.path | relative_url }}" class="card" target="_blank" rel="noopener">
            <div class="pdf">📄</div><div class="label">{{ name }}</div>
          </a>
        {% else %}
          <a href="{{ f.path | relative_url }}" class="card" target="_blank" rel="noopener">
            <img src="{{ f.path | relative_url }}" alt="{{ name }}"><div class="label">{{ name }}</div>
          </a>
        {% endif %}
      {% endif %}
    {% endfor %}
  </div>
{% endif %}

{%- comment -%} Render each folder {%- endcomment -%}
{% for folder in folders %}
  {% if folder != "" %}
    {% assign folder_id = folder | slugify: 'pretty' %}
    <h2 id="{{ folder_id }}">{{ folder | replace:"_"," " }}</h2>
    <div class="grid">
      {% assign prefix = page.base | append: folder | append:"/" %}
      {% for f in under_base %}
        {% if f.path contains prefix %}
          {% assign filename = f.path | split:"/" | last %}
          {% assign ext = filename | split:"." | last | downcase %}
          {% if allowed_exts contains ext %}
            {% assign name = filename | remove: "." | split: ext | first | replace:"_"," " %}
            {% if ext == "pdf" %}
              <a href="{{ f.path | relative_url }}" class="card" target="_blank" rel="noopener">
                <div class="pdf">📄</div><div class="label">{{ name }}</div>
              </a>
            {% else %}
              <a href="{{ f.path | relative_url }}" class="card" target="_blank" rel="noopener">
                <img src="{{ f.path | relative_url }}" alt="{{ name }}">
                <div class="label">{{ name }}</div>
              </a>
            {% endif %}
          {% endif %}
        {% endif %}
      {% endfor %}
    </div>
  {% endif %}
{% endfor %}

---

<details class="debug">
  <summary>Diagnostics (click to expand)</summary>
  <p><strong>page.base</strong>: <code>{{ page.base }}</code></p>
  <p><strong>Counts</strong> — under_base: {{ under_base.size }}, folders: {{ folders.size }}, root_files: {{ root_files.size }}</p>
  <p><strong>All static files under base</strong>:</p>
  <code class="block">
{% for f in under_base -%}
{{ f.path }}
{% endfor -%}
  </code>
  <p><strong>Folder names detected</strong>:</p>
  <code class="block">
{% for folder in folders -%}
{{ folder }}
{% endfor -%}
  </code>
</details>
