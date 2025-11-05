---
title: Design by DCA
layout: bare
permalink: /GT2101/design-by-DCA/
---

<style>
  :root{
    --paper:#f7f5ee; --card:#fff; --border:#e0dacb; --ink:#111; --muted:#6b6b6b;
    --radius:14px; --shadow:0 4px 18px rgba(0,0,0,.06);
  }
  body{background:var(--paper);color:var(--ink);font-family:system-ui,-apple-system,Segoe UI,Roboto,Ubuntu,"Helvetica Neue",Arial,sans-serif;margin:20px}
  h1{font-size:2rem;margin:.2rem 0 .8rem}
  p.lede{color:var(--muted);line-height:1.6;max-width:760px}

  .gallery{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px;margin:1.6rem 0}
  figure{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);
         box-shadow:var(--shadow);overflow:hidden;margin:0}
  figure a{display:block}
  img{width:100%;height:auto;display:block}
  .thumb{cursor:zoom-in}
  figcaption{padding:.6rem .8rem;color:var(--muted);font-size:.9rem;line-height:1.4}

  /* CSS-only lightbox */
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

# Design by DCA

<p class="lede">
  In the mid-1970s, <strong>Ira Gale</strong> engaged <strong>DCA Design Consultants</strong>, led by founder <strong>Derek Carter</strong>, to realise a radical vision for a transparent, suspended record player that fused precision engineering with modernist form. 
  The collaboration produced the <strong>Gale GT2101</strong> — layered perspex over stainless-steel pods, plus a separate cylindrical control tower housing the speed electronics and LED display. 
  This page preserves a studio portrait of the DCA team alongside high-resolution product photographs that document the language and craft of this partnership.
</p>

<div class="gallery">

  <!-- Team photo (add your actual team image path if different) -->
  <figure>
    <a href="#img-team">
      <img class="thumb" src="/GT2101/gallery/DCA_Team_black-and-white.jpg"
           alt="DCA Design Consultants team, black-and-white studio portrait">
    </a>
    <figcaption>DCA Design Consultants — black-and-white studio portrait from the GT2101 era.</figcaption>
  </figure>

  <figure>
    <a href="#img-ct">
      <img class="thumb" src="/GT2101/gallery/GT2101_Control-Tower_front-buttons.jpg"
           alt="GT2101 control tower front view with red and green buttons">
    </a>
    <figcaption>Cylindrical control tower of the GT2101, showing the red and green power switches on its brushed-steel front panel.</figcaption>
  </figure>

  <figure>
    <a href="#img-top">
      <img class="thumb" src="/GT2101/gallery/GT2101_Turntable_topdown_with-control-tower.jpg"
           alt="Top-down view of the GT2101 turntable with control tower and coiled connection cable">
    </a>
    <figcaption>Top-down view of the GT2101 turntable with its external control tower connected by a coiled cable, displaying the LED speed readout.</figcaption>
  </figure>

  <figure>
    <a href="#img-34">
      <img class="thumb" src="/GT2101/gallery/GT2101_Turntable_three-quarter-angle.jpg"
           alt="Three-quarter angled view of the GT2101 turntable">
    </a>
    <figcaption>Three-quarter angle revealing the acrylic layer construction and stainless-steel isolation pods supporting the floating platter assembly.</figcaption>
  </figure>

  <figure>
    <a href="#img-side">
      <img class="thumb" src="/GT2101/gallery/GT2101_Turntable_side-profile_with-control-tower.jpg"
           alt="Side profile of GT2101 with control tower">
    </a>
    <figcaption>Side profile showing the GT2101 turntable and its companion control tower — a striking combination of engineering precision and industrial design.</figcaption>
  </figure>

  <figure>
    <a href="#img-detail">
      <img class="thumb" src="/GT2101/gallery/GT2101_Turntable_right-side_detail-arm-base.jpg"
           alt="Right side close-up of GT2101 tonearm and acrylic plinth structure">
    </a>
    <figcaption>Close-up of the right side, highlighting the tonearm base and layered acrylic/steel plinth structure that defined the GT2101’s distinctive form.</figcaption>
  </figure>

</div>

<!-- Lightbox targets -->
<a href="#" class="lightbox" id="img-team">
  <img src="/GT2101/gallery/DCA_Team_black-and-white.jpg" alt="DCA team portrait, enlarged">
  <span class="close" aria-label="Close">×</span>
</a>

<a href="#" class="lightbox" id="img-ct">
  <img src="/GT2101/gallery/GT2101_Control-Tower_front-buttons.jpg" alt="GT2101 control tower, enlarged">
  <span class="close" aria-label="Close">×</span>
</a>

<a href="#" class="lightbox" id="img-top">
  <img src="/GT2101/gallery/GT2101_Turntable_topdown_with-control-tower.jpg" alt="GT2101 top-down with control tower, enlarged">
  <span class="close" aria-label="Close">×</span>
</a>

<a href="#" class="lightbox" id="img-34">
  <img src="/GT2101/gallery/GT2101_Turntable_three-quarter-angle.jpg" alt="GT2101 three-quarter angle, enlarged">
  <span class="close" aria-label="Close">×</span>
</a>

<a href="#" class="lightbox" id="img-side">
  <img src="/GT2101/gallery/GT2101_Turntable_side-profile_with-control-tower.jpg" alt="GT2101 side profile with control tower, enlarged">
  <span class="close" aria-label="Close">×</span>
</a>

<a href="#" class="lightbox" id="img-detail">
  <img src="/GT2101/gallery/GT2101_Turntable_right-side_detail-arm-base.jpg" alt="GT2101 right-side detail at arm base, enlarged">
  <span class="close" aria-label="Close">×</span>
</a>

<p class="lede" style="margin-top:1.4rem">
  <em>Photographs © Gale Electronics Archive / DCA Design Consultants — preserved as part of the GT2101 documentation set.</em>
</p>
