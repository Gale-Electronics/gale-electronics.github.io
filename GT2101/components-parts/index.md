---
title: "Components & Parts"
layout: bare
permalink: /GT2101/components-parts/
---

<style>
  :root{--paper:#f7f5ee;--card:#fff;--border:#e0dacb;--ink:#111;--muted:#6b6b6b;--radius:14px;--shadow:0 4px 18px rgba(0,0,0,.06)}
  body{background:var(--paper);color:var(--ink);margin:20px;font-family:system-ui,-apple-system,Segoe UI,Roboto,Ubuntu,"Helvetica Neue",Arial,sans-serif}
  h1{font-size:2rem;margin:.2rem 0 .8rem}
  p.lede{color:var(--muted);line-height:1.6;max-width:none;width:100%;hyphens:auto;overflow-wrap:anywhere}

  /* Gallery grid */
  .gallery{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px;margin:1.6rem 0}
  figure{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);box-shadow:var(--shadow);overflow:hidden;margin:0}
  figure a{display:block}
  img{width:100%;height:auto;display:block}
  figcaption{padding:.6rem .8rem;color:var(--muted);font-size:.9rem;line-height:1.4}

  /* Lightbox (CSS only) */
  .lightbox{position:fixed;inset:0;display:none;align-items:center;justify-content:center;background:rgba(0,0,0,.85);z-index:9999;padding:10px}
  .lightbox img{max-width:96vw;max-height:92vh;width:auto;height:auto;border-radius:12px;box-shadow:0 10px 30px rgba(0,0,0,.5)}
  .lightbox:target{display:flex}
  .lightbox .close{position:fixed;top:12px;right:14px;color:#fff;text-decoration:none;font-size:28px;line-height:1;padding:6px 10px;border-radius:8px;background:rgba(0,0,0,.3)}

  @media (max-width:720px){body{margin:14px}h1{font-size:1.6rem}}
</style>

# Components & Parts

<p class="lede">
  PCB layouts, populated boards, motor assemblies, looms, connectors, and detail shots, archived at full resolution for repair and reference.
  Click any image to view full-screen. Captions note board names, revisions, and GT2101 locations where known.
</p>

<div class="gallery">

  <figure>
    <a href="#cp-8">
      <img src="/GT2101/engineering-drawings-schematics/GT2101_Motor_Assembly_Cutaway_Labeled.jpg"
           alt="LED display module and front-panel assembly for GT2101">
    </a>
    <figcaption>LED Display, front-panel module and readout assembly.</figcaption>
  </figure>

  <figure>
    <a href="#cp-1">
      <img src="/GT2101/engineering-drawings-schematics/disk-1-display-interface/disk-1-3155ST.jpg"
           alt="Display Interface board (Disk 1, 3155ST), component side">
    </a>
    <figcaption>Display Interface — component side (Disk 1, 3155ST).</figcaption>
  </figure>

  <figure>
    <a href="#cp-2">
      <img src="/GT2101/engineering-drawings-schematics/disk-2ab-servo-motor-drive/disk-2-3272ST-underside.jpg"
           alt="Servo Motor Drive board (Disk 2, 3272ST), underside copper and solder">
    </a>
    <figcaption>Servo Motor Drive, underside copper/solder reference (Disk 2, 3272ST).</figcaption>
  </figure>

  <figure>
    <a href="#cp-3">
      <img src="/GT2101/engineering-drawings-schematics/disk-2ab-servo-motor-drive/disk-2-3272ST.jpg"
           alt="Servo Motor Drive board (Disk 2, 3272ST), component side with pass devices and connectors">
    </a>
    <figcaption>Servo Motor Drive, component side (Disk 2, 3272ST).</figcaption>
  </figure>

  <figure>
    <a href="#cp-4">
      <img src="/GT2101/engineering-drawings-schematics/disk-4-reference-oscillator/disk-4-3276ST.jpg"
           alt="Reference Oscillator board (Disk 4, 3276ST) with crystal and timing network">
    </a>
    <figcaption>Reference Oscillator, crystal/timing network (Disk 4, 3276ST).</figcaption>
  </figure>

  <figure>
    <a href="#cp-5">
      <img src="/GT2101/engineering-drawings-schematics/disk-5-power-supply/disk-5-3285NH.jpg"
           alt="Power Supply board (Disk 5, 3285NH) with rectifier and smoothing capacitors">
    </a>
    <figcaption>Power Supply, rectification and smoothing (Disk 5, 3285NH).</figcaption>
  </figure>

  <figure>
    <a href="#cp-6">
      <img src="/GT2101/engineering-drawings-schematics/disk-5-power-supply/disk-5-power-supply-3285NH.jpg"
           alt="Power Supply board variant (Disk 5, 3285NH), alternate layout">
    </a>
    <figcaption>Power Supply, alternate board photo (Disk 5, 3285NH).</figcaption>
  </figure>

  <figure>
    <a href="#cp-7">
      <img src="/GT2101/engineering-drawings-schematics/Turntable_LED.jpg"
           alt="LED display module and front-panel assembly for GT2101">
    </a>
    <figcaption>LED Display, front-panel module and readout assembly.</figcaption>
  </figure>

  <figure>
    <a href="#cp-9">
      <img src="/GT2101/engineering-drawings-schematics/top_PCB_Lifted_Showing_Vary_Speed_Adjuster.jpg"
           alt="LED display module and front-panel assembly for GT2101">
    </a>
    <figcaption>LED Display, front-panel module and readout assembly.</figcaption>
  </figure>

<figure>
  <a href="#cp-10">
    <img src="/GT2101/engineering-drawings-schematics/motor-overview/GT2101_Motor_Controller_PCB_Bottom.jpg"
         alt="GT2101 motor controller PCB — underside view showing copper traces and solder joints">
  </a>
  <figcaption>Motor controller PCB — underside copper and solder joints.</figcaption>
</figure>

<figure>
  <a href="#cp-11">
    <img src="/GT2101/engineering-drawings-schematics/motor-overview/GT2101_Motor_Controller_PCB_Top.jpg"
         alt="GT2101 motor controller PCB — top view with components, wiring and trimmers">
  </a>
  <figcaption>Motor controller PCB — top side with components, wiring and trimmers.</figcaption>
</figure>

<figure>
  <a href="#cp-12">
    <img src="/GT2101/engineering-drawings-schematics/motor-overview/GT2101_Motor_Stator_Internal_View.jpg"
         alt="GT2101 motor stator — internal view down the housing showing coil pack and bore">
  </a>
  <figcaption>Motor stator — internal view down the housing showing the coil pack.</figcaption>
</figure>


</div>

<!-- LIGHTBOX TARGETS -->
<a href="#" class="lightbox" id="cp-8">
  <img src="/GT2101/engineering-drawings-schematics/GT2101_Motor_Assembly_Cutaway_Labeled.jpg" alt="Power Supply board (Disk 5, 3285NH), full-resolution">
  <span class="close" aria-label="Close">×</span>
</a>

<a href="#" class="lightbox" id="cp-1">
  <img src="/GT2101/engineering-drawings-schematics/disk-1-display-interface/disk-1-3155ST.jpg" alt="Display Interface board (Disk 1, 3155ST), full-resolution">
  <span class="close" aria-label="Close">×</span>
</a>

<a href="#" class="lightbox" id="cp-2">
  <img src="/GT2101/engineering-drawings-schematics/disk-2ab-servo-motor-drive/disk-2-3272ST-underside.jpg" alt="Servo Motor Drive underside (Disk 2, 3272ST), full-resolution">
  <span class="close" aria-label="Close">×</span>
</a>

<a href="#" class="lightbox" id="cp-3">
  <img src="/GT2101/engineering-drawings-schematics/disk-2ab-servo-motor-drive/disk-2-3272ST.jpg" alt="Servo Motor Drive component side (Disk 2, 3272ST), full-resolution">
  <span class="close" aria-label="Close">×</span>
</a>

<a href="#" class="lightbox" id="cp-4">
  <img src="/GT2101/engineering-drawings-schematics/disk-4-reference-oscillator/disk-4-3276ST.jpg" alt="Reference Oscillator (Disk 4, 3276ST), full-resolution">
  <span class="close" aria-label="Close">×</span>
</a>

<a href="#" class="lightbox" id="cp-5">
  <img src="/GT2101/engineering-drawings-schematics/disk-5-power-supply/disk-5-3285NH.jpg" alt="Power Supply board (Disk 5, 3285NH), full-resolution">
  <span class="close" aria-label="Close">×</span>
</a>

<a href="#" class="lightbox" id="cp-6">
  <img src="/GT2101/engineering-drawings-schematics/disk-5-power-supply/disk-5-power-supply-3285NH.jpg" alt="Power Supply board variant (Disk 5, 3285NH), full-resolution">
  <span class="close" aria-label="Close">×</span>
</a>

<a href="#" class="lightbox" id="cp-7">
  <img src="/GT2101/engineering-drawings-schematics/Turntable_LED.jpg" alt="LED display module and front-panel assembly, full-resolution">
  <span class="close" aria-label="Close">×</span>
</a>

<a href="#" class="lightbox" id="cp-9">
  <img src="/GT2101/engineering-drawings-schematics/top_PCB_Lifted_Showing_Vary_Speed_Adjuster.jpg" alt="Power Supply board variant (Disk 5, 3285NH), full-resolution">
  <span class="close" aria-label="Close">×</span>
</a>

<a href="#" class="lightbox" id="cp-10">
  <img src="/GT2101/engineering-drawings-schematics/motor-overview/GT2101_Motor_Controller_PCB_Bottom.jpg"
       alt="GT2101 motor controller PCB underside, full-resolution">
  <span class="close" aria-label="Close">×</span>
</a>

<a href="#" class="lightbox" id="cp-11">
  <img src="/GT2101/engineering-drawings-schematics/motor-overview/GT2101_Motor_Controller_PCB_Top.jpg"
       alt="GT2101 motor controller PCB top, full-resolution">
  <span class="close" aria-label="Close">×</span>
</a>

<a href="#" class="lightbox" id="cp-12">
  <img src="/GT2101/engineering-drawings-schematics/motor-overview/GT2101_Motor_Stator_Internal_View.jpg"
       alt="GT2101 motor stator internal view, full-resolution">
  <span class="close" aria-label="Close">×</span>
</a>



<p class="lede" style="margin-top:1.2rem">
  <em>Contributions welcome — please include board name, view (top/bottom), and any markings or revisions. All images are preserved for restoration and research within the GT2101 archive.</em>
</p>
