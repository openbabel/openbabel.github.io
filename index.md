---
layout: splash
title: Open Babel - the chemistry toolbox
share: true
---

Open Babel is a chemical toolbox designed to speak the many languages of chemical data. It's an open, collaborative project allowing anyone to search, convert, analyze, or store data from molecular modeling, chemistry, solid-state materials, biochemistry, or related areas.

- Ready-to-use programs, and complete programmer's toolkit
- Read, write and convert over 110 chemical file formats
- Filter and search molecular files using SMARTS and other methods
- Supports molecular modeling, cheminformatics, bioinformatics
- Organic chemistry, inorganic chemistry, solid-state materials, nuclear chemistry
- Downloaded over 325,000 times and used by over 40 related projects
- How to cite Open Babel: The Open Babel and Pybel papers

<h2>News</h2>

<ul>
{% for post in site.posts limit:5 %}
  <li><span class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}"><strong>{{ post.date | date: "%B %d, %Y" }}:&nbsp;</strong></time></span>
<a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}
</ul>
