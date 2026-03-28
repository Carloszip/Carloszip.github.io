---
layout: default
lang: en
---

# 📢 Updates

<div class="news-feed">
  {% assign posts_en = site.posts | where: "lang", "en" %}
  {% for post in posts_en %}
    <article class="news-card">
      <span class="news-date">{{ post.date | date: "%m/%d/%Y" }}</span>
      <h3 class="news-title"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
      <p>{{ post.content | strip_html | truncatewords: 25 }}</p>
    </article>
  {% else %}
    <p>There are no updates yet.</p>
  {% endfor %}
</div>