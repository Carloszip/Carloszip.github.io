---
layout: default
lang: es
---

# 📢 Novedades

<div class="news-feed">
  {% assign posts_es = site.posts | where: "lang", "es" %}
  {% for post in posts_es %}
    <article class="news-card">
      <span class="news-date">{{ post.date | date: "%d/%m/%Y" }}</span>
      <h3 class="news-title"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
      <p>{{ post.content | strip_html | truncatewords: 25 }}</p>
    </article>
  {% else %}
    <p>Aún no hay novedades en español.</p>
  {% endfor %}
</div>