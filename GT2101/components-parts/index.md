---
title: Components & Parts
layout: bare
permalink: /GT2101/components-parts/
---

<style>
  :root{
    --paper:#f7f5ee; --card:#fff; --border:#e0dacb; --ink:#111; --muted:#6b6b6b;
    --radius:14px; --shadow:0 4px 18px rgba(0,0,0,.06);
  }
  body{background:var(--paper);color:var(--ink);margin:20px;font-family:system-ui,-apple-system,Segoe UI,Roboto,Ubuntu,"Helvetica Neue",Arial,sans-serif}
  h1{font-size:2rem;margin:.2rem 0 .8rem}
  p.lede{color:var(--muted);line-height:1.6;max-width:none;width:100%;hyphens:auto;overflow-wrap:anywhere}

  /* Gallery grid */
  .gallery{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px;margin:1.6rem 0}
  figure{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);
         box-shadow:var(--shadow);overflow:hidden;margin:0}
  figure a{display:block}
  img{width:100%;height:auto;display:block}
  figcaption{padding:.6rem .8rem;color:var(--muted);font-size:.9rem;line-height:1.4}

  /* Lightbox (CSS only) */
  .lightbox{
    position:fixed; inset:0; display:none; align-items:center; justify-content:center;
    background:rgba(0,0,0,.85); z-index:9999; padding:10px;
  }
  .lightbox img{
    max-width:96vw; max-height:92vh; width:auto; height:auto; border-radius:12px;
    box-shadow:0 10px 30px rgba(0,0,0,.5);
  }
  .lightbox:target{display:flex}
  .lightbox .close{
    position:fixed; top:12px; right:14px; color:#fff; text-decoration:none; font-size:28px;
    line-height:1; padding:6px 10px; border-radius:8px; background:rgba(0,0,0,.3)
  }

  @media (max-width:720px){
    body{margin:14px}
    h1{font-size:1.6rem}
  }
</style>

# Components & Parts

<p class="lede">
  PCB layouts, populated boards, motor assemblies, looms, connectors, and detail shots — archived at full resolution for repair and reference.
  Click any image to view full-screen. Where possible, captions note board names, revisions, and locations within the GT2101 system.
</p>

<div class="gallery">

  <!-- EXAMPLES — duplicate a <figure> for each image you upload. 
       Update src/alt/caption and add a matching lightbox below. -->

  <figure>
    <a href="#cp-1">
      <img src="/GT2101/components-parts/Main_Control_PCB_Main_Control_PCB_1.jpg"
           alt="GT2101 main control PCB, top view with controller ICs and trimmers visible">
    </a>
    <figcaption>Main Control PCB — top view. Controller ICs, trim pots, and edge connector.</figcaption>
  </figure>

  <figure>
    <a href="#cp-2">
      <img src="/GT2101/components-parts/Main_Control_PCB_Layout_Main_Control_PCB_Layout_1.jpg"
           alt="Unpopulated layout of the GT2101 main control PCB showing copper traces and silkscreen">
    </a>
    <figcaption>Main Control PCB — bare layout / copper trace reference.</figcaption>
  </figure>

  <figure>
    <a href="#cp-3">
      <img src="/GT2101/components-parts/Digital_Display_PCB_Digital_Display_PCB_1.jpg"
           alt="Digital display PCB with LED readout module and driver chips">
    </a>
    <figcaption>Digital Display PCB — LED readout and driver stage.</figcaption>
  </figure>

  <figure>
    <a href="#cp-4">
      <img src="/GT2101/components-parts/GaleTTmotSchem_GaleTTmotSchem_1.jpg"
           alt="Motor drive schematic page for the GT2101, showing hall sensor and commutation stages">
    </a>
    <figcaption>Motor drive schematic — Hall sensor / commutation stages.</figcaption>
  </figure>

  <figure>
    <a href="#cp-5">
      <img src="/GT2101/components-parts/GaleTTbackplane_GaleTTbackplane_1.jpg"
           alt="GT2101 backplane board with multi-way connectors and harness attachment points">
    </a>
    <figcaption>Backplane board — interconnects and harness attachment points.</figcaption>
  </figure>

  <figure>
    <a href="#cp-6">
      <img src="/GT2101/components-parts/gale_gt2101_parts_gale_gt2101_parts_1.jpg"
           alt="Assorted GT2101 parts laid out: fasteners, spacers, connectors, and small hardware">
    </a>
    <figcaption>Assorted hardware — fasteners, spacers, connectors.</figcaption>
  </figure>

</div>

<!-- LIGHTBOX TARGETS (IDs must match the hrefs above) -->
<a href="#" class="lightbox" id="cp-1">
  <img src="/GT2101/components-parts/Main_Control_PCB_Main_Control_PCB_1.jpg"
       alt="GT2101 main control PCB, full-resolution top view">
  <span class="close" aria-label="Close">×</span>
</a>

<a href="#" class="lightbox" id="cp-2">
  <img src="/GT2101/components-parts/Main_Control_PCB_Layout_Main_Control_PCB_Layout_1.jpg"
       alt="GT2101 main control PCB bare layout, full-resolution trace reference">
  <span class="close" aria-label="Close">×</span>
</a>

<a href="#" class="lightbox" id="cp-3">
  <img src="/GT2101/components-parts/Digital_Display_PCB_Digital_Display_PCB_1.jpg"
       alt="Digital display PCB with LED readout module and drivers, full-resolution">
  <span class="close" aria-label="Close">×</span>
</a>

<a href="#" class="lightbox" id="cp-4">
  <img src="/GT2101/components-parts/GaleTTmotSchem_GaleTTmotSchem_1.jpg"
       alt="GT2101 motor drive schematic page, full-resolution">
  <span class="close" aria-label="Close">×</span>
</a>

<a href="#" class="lightbox" id="cp-5">
  <img src="/GT2101/components-parts/GaleTTbackplane_GaleTTbackplane_1.jpg"
       alt="GT2101 backplane board, full-resolution">
  <span class="close" aria-label="Close">×</span>
</a>

<a href="#" class="lightbox" id="cp-6">
  <img src="/GT2101/components-parts/gale_gt2101_parts_gale_gt2101_parts_1.jpg"
       alt="Assorted GT2101 small parts, full-resolution">
  <span class="close" aria-label="Close">×</span>
</a>

<p class="lede" style="margin-top:1.2rem">
  <em>Contributions welcome — please include board name, view (top/bottom), and any markings or revisions.  
  All images are preserved for restoration and research within the GT2101 archive.</em>
</p>
