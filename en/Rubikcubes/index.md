# My collection
Welcome to my cube collection! At this moment, I have **{{ site.data.cubos | size }}** cubes:

<div class="cubes-grid">
  {% for cubo in site.data.cubos %}
    <div class="cube-card">
      <div class="cube-img-wrapper">
        <img src="{{ cubo.image | relative_url }}" alt="{{ cubo.name_en }}" class="cube-img">
      </div>
      <div class="cube-info">
        <h3 class="cube-title">{{ cubo.name_en }}</h3>
        <p class="cube-desc">{{ cubo.desc_en }}</p>
      </div>
    </div>
  {% endfor %}
</div>