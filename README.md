# Chung-Wen Lin - Personal Webpage

This repository contains the source code for my personal and academic portfolio website.

🌐 **Live Site:** [https://lincw.github.io](https://lincw.github.io)

## About
This is a static website built with HTML, CSS, and a small amount of JavaScript, with Jekyll rendering the blog on GitHub Pages. It serves as a central hub for:
- Showcasing my projects and products (e.g., Immune Network)
- My professional profile and academic CV
- Research publications and selected video explainers
- My contact information

## Structure
- `index.html`: The main landing page featuring my projects.
- `profile.html`: My professional background, selected work, experience, and skills.
- `publications.html`: My research publications.
- `videos.html`: Four curated research paper and method explainers, with original studies and related portfolio work.
- `blog.html` and `_layouts/blog_post.html`: Blog index and post layout.
- `contact.html`: How to get in touch with me.
- `styles.css`: The styling for the entire website.
- `assets/`: Contains images and other static assets.

## Local preview

The Blog index and Markdown articles are Jekyll templates. Opening the source `blog.html` directly, or serving the repository with a plain static file server, leaves Liquid expressions such as `{{ site.baseurl }}` unresolved. This breaks its styles, links, and article list.

Use Ruby 3.3 and Bundler for the GitHub Pages dependency set. Ruby 4 is currently incompatible with its CommonMarker dependency, and macOS's system Ruby 2.6 is too old for its Nokogiri dependency. On macOS with Homebrew:

```sh
brew install ruby@3.3
export PATH="$(brew --prefix ruby@3.3)/bin:$PATH"
```

Then run from this directory:

```sh
bundle install
bundle exec jekyll serve --host 127.0.0.1
```

Open `http://127.0.0.1:4000/blog.html` to preview the rendered Blog. Use this server for all pages so navigation between static pages and the Blog works consistently. Stop the server with Ctrl+C.

To build without starting a server, use `bundle exec jekyll build`. The generated site is in `_site/`; point any other preview server at that directory, not the repository root. See the [GitHub Pages local testing guide](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll) for environment setup.

## Curating research explainers

Edit the static cards in `videos.html` to change the selection. Keep 3–5 videos that complement the software and research portfolio. Each card includes a topic, duration, short description, communication focus, original paper links, and related work where relevant. Use chapter links only when verified in the video description, and label preprints explicitly.

The initial selection was checked against the rendered YouTube descriptions and chapters on 15 October 2026. Descriptions summarise those sources; they are not a claim that every scientific conclusion has been independently reviewed. Related software links show a thematic connection, not necessarily software demonstrated in the video.

Video thumbnails link directly to YouTube; no embedded players, API keys, or automatic feed are needed. When changing navigation, update all top-level HTML pages and `_layouts/blog_post.html`.

`assets/site-avatar.jpg` is the public YouTube channel avatar, retrieved on 15 October 2026 and adopted as this website's avatar. It appears above the name in every page's sidebar and is also used as the browser tab icon.
