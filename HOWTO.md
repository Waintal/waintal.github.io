# How to use this website

Everything lives in this folder, which is a git repository. The site is rebuilt and published automatically
on GitHub Pages (https://waintal.github.io) about a minute after each `git push`.

## 0. Once: install Hugo
```sh
brew install hugo
```

## 1. See the site on your computer
```sh
cd waintal.github.io
hugo server
```
Open http://localhost:1313. The page refreshes by itself every time you save a file. Stop with Ctrl-C.

## 2. Write a blog post
```sh
hugo new content blog/2026-10-15-my-title.md
```
This creates `content/blog/2026-10-15-my-title.md`. Open it and write Markdown below the header:
```markdown
---
title: "My title"
date: 2026-10-15
description: "One sentence shown in the list of posts."
draft: true         # remove this line (or set false) when the post is ready
---
Some text, a [link](https://arxiv.org), an equation $E = mc^2$ or

$$ H = \sum_{ij} t_{ij} c^\dagger_i c_j $$

![a figure](/img/blog/my-figure.png)
```
- Drafts are visible with `hugo server -D` but are not published.
- Images: put them in `static/img/blog/` and use `/img/blog/name.png` in the post.

## 3. Publish
```sh
git add -A
git commit -m "New post: my title"
git push
```
Check progress in the "Actions" tab of the GitHub repository.

## 4. Other common edits
| What | Where |
|---|---|
| Add a paper | `data/publications.yaml` (newest first), or ask Claude: "update my publications" |
| Add a talk / video | `data/talks.yaml` (`featured: true` to show it on the home page) |
| Home page text, research cards | `content/_index.md` |
| Research, Projects, Join us, Bio pages | `content/research.md`, `projects.md`, `join.md`, `bio.md` |
| Name, email, links, menu | `hugo.yaml` |
| Colors, fonts, spacing | `static/css/site.css` |

To check for new papers automatically: `python3 scripts/update_publications.py` (it only prints suggestions).
After adding papers by hand, run `python3 scripts/renumber_publications.py` to sort and renumber the list.
