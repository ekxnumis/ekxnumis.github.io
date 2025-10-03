---
layout: blog
title: "George III"
permalink: /blog/GeorgeIII/
slug: "GeorgeIII"
---

# {{ page.title }}

<p>Overview / introduction to George III coin studies.</p>

<ul>
{% assign cat = nil %}
{% for c in site.data.blog.categories %}
  {% if c.slug == page.slug %}
    {% assign cat = c %}
  {% endif %}
{% endfor %}

{% if cat and cat.children %}
  {% for child in cat.children %}
    <li><a href="{{ child.url }}">{{ child.title }}</a></li>
  {% endfor %}
{% else %}
  <li>No studies yet.</li>
{% endif %}
</ul>