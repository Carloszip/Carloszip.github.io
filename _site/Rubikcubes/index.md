# Mi colección
¡Bienvenido a mi colección de cubos! De momento tengo **{{ site.data.cubos | size }}**:

<div class="cubes-grid">
  {% for cubo in site.data.cubos %}
    <div class="cube-card">
      <div class="cube-img-wrapper">
        <img src="{{ cubo.image | relative_url }}" alt="{{ cubo.name_es }}" class="cube-img">
      </div>
      <div class="cube-info">
        <h3 class="cube-title">{{ cubo.name_es }}</h3>
        <p class="cube-desc">{{ cubo.desc_es }}</p>
      </div>
    </div>
  {% endfor %}
</div>