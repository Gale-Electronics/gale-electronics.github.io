---
title: GT2101 Turntable
layout: default
---

# GT2101 Turntable

Upload images into this folder or any subfolder (e.g. `photographs-adverts/`) and they’ll appear below.

<div class="grid" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:14px">
{% assign files_all = site.static_files | where_exp: "f", "f.path contains page.dir" %}
{% assign images = files_all | where_exp: "f", "f.extname == '.jpg' or f.extname == '.jpeg' or f.extname == '.png' or f.extname == '.gif' or f.extname == '.webp'" %}
{% for f in images %}
  <a href="{{ f.path }}" class="card" style="border:1px solid #ddd;border-radius:10px;overflow:hidden;background:#fff;text-decoration:none">
    <img src="{{ f.path }}" alt="{{ f.name }}" style="width:100%;aspect-ratio:4/3;object-fit:cover">
    <div style="padding:8px 10px;font-size:14px;color:#222;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">{{ f.name }}</div>
  </a>
{% endfor %}
</div>

## Folders
- [Photographs & Adverts](/GT2101/photographs-adverts/)
- [Interviews & Provenance](/GT2101/interviews-provenance/)
