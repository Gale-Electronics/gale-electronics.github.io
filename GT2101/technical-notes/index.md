---
title: GT2101 — Technical Notes
layout: bare
nav_order: 9
permalink: /GT2101/technical-notes/
---

# GT2101 Technical Notes

Reference notes for diagnosing and restoring the **Gale GT2101**.

<ul>
{% assign notes = site.pages 
  | where_exp: "p", "p.path contains 'GT2101/technical-notes/'" 
  | where_exp: "p", "p.url != page.url" 
  | sort: "nav_order" %}
{% for p in notes %}
  <li><a href="{{ p.url }}">{{ p.title }}</a></li>
{% endfor %}
</ul>
