---
title: Marketing & Publicity
layout: bare
permalink: /marketing/
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

# Marketing & Publicity

<p class="lede">
  Adverts, brochures, press coverage, and show photography — archived at full resolution with captions and dates where known. Click any image to view full-screen.
</p>

<div class="gallery">

  <!-- EXAMPLE ITEM — duplicate this block per image -->
  <figure>
    <a href="#mkt-1">
      <img src="/marketing/401-ad-uk-1974.jpg" alt="GS401 chrome-ended magazine advert, UK (c.1974)">
    </a>
    <figcaption>GS401 magazine advert (UK, c.1974). Source: scan from original press clipping.</figcaption>
  </figure>

  <!-- Add more <figure> blocks as needed -->

</div>

<!-- LIGHTBOX TARGETS: one per image, match the href id -->
<a href="#" class="lightbox" id="mkt-1">
  <img src="/marketing/Gale-GT2101-Blue2.jpg" alt="GS401 chrome-ended magazine advert, enlarged">
  <span class="close" aria-label="Close">×</span>
</a>
<a href="#" class="lightbox" id="mkt-1">
  <img src="/marketing/Gale_GT2101_Publicity_Photo_DCA_Studio.jpg" alt="GS401 chrome-ended magazine advert, enlarged">
  <span class="close" aria-label="Close">×</span>
</a>
<a href="#" class="lightbox" id="mkt-1">
  <img src="/marketing/Radio_Gijutsu_Aug1976_Cartridge_Guide.jpg" alt="GS401 chrome-ended magazine advert, enlarged">
  <span class="close" aria-label="Close">×</span>
</a>
<a href="#" class="lightbox" id="mkt-1">
  <img src="/marketing/Radio_Gijutsu_Aug1976_GT2101_Feature.jpg" alt="GS401 chrome-ended magazine advert, enlarged">
  <span class="close" aria-label="Close">×</span>
</a>

<p class="lede" style="margin-top:1.2rem">
  <em>Images are archived for historical scholarship and commentary. Contact us for credits, corrections, or rights queries.</em>
</p>
