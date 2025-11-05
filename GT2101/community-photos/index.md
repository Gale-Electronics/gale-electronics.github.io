---
title: Community Photos
layout: bare
permalink: /GT2101/community-photos/
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

# Community Photos

<p class="lede">
  Real-world examples of the <strong>Gale GS401</strong> loudspeakers and <strong>GT2101</strong> turntables, photographed by owners and restorers around the world.  
  Each submission is displayed at full resolution with contributor credit, date, and restoration details where available.  
  To share your own setup, email <a href="mailto:vintagegaleuk@gmail.com">vintagegaleuk@gmail.com</a>.
</p>

<div class="gallery">

  <!-- Example submission (duplicate as needed) -->
  <figure>
    <a href="#com-2">
      <img src="/GT2101/community-photos/GT2101.jpg"
           alt="Gale GT2101 turntable with Quad electronics in a London listening room, submitted by John S.">
    </a>
    <figcaption>
      GT2101 turntable paired with Quad 405 and ESLs — John S. (London, 2024). Full motor service and custom acrylic lid restoration.
    </figcaption>
  </figure>

</div>

<!-- Lightbox targets (match the IDs above) -->
<a href="#" class="lightbox" id="com-1">
  <img src="/GT2101/community-photos/GT2101.jpg"
       alt="gt2101">
  <span class="close" aria-label="Close">×</span>
</a>

<p class="lede" style="margin-top:1.2rem">
  <em>To submit your photographs, email <a href="mailto:vintagegaleuk@gmail.com">vintagegaleuk@gmail.com</a> with your name, date, model, and restoration notes.  
  All images © their respective contributors and archived for educational reference.</em>
</p>
