# StaticSiteGenerator

A Python-powered static site generator that converts Markdown content into fully styled, linkable HTML pages. Built as part of a Boot.dev project, this generator uses custom parsing logic, a recursive build pipeline, and supports GitHub Pages deployment.

## Features

- Converts `.md` files into static `.html` pages using a Jinja-style template
- Recursively processes content in nested directories
- Preserves directory structure from `content/` to `docs/` (for GitHub Pages)
- Supports Markdown features:
  - Headings
  - Bold, Italic, Code spans
  - Code blocks
  - Lists (ordered & unordered)
  - Blockquotes
  - Links and images
- Builds styles and assets into the `docs/` directory
- GitHub Pages-compatible with support for custom base paths

## Project Structure


