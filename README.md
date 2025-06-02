# Static Site Generator

A simple and powerful static site generator built with Python that converts Markdown files into a beautiful static website.

## Features

- Converts Markdown to HTML
- Supports custom templates
- Handles static assets (images, CSS, etc.)
- Supports nested directories
- Markdown features supported:
  - Headers (H1-H6)
  - Bold and italic text
  - Code blocks
  - Blockquotes
  - Ordered and unordered lists
  - Links and images
  - Inline code

## Directory Structure

```
.
├── content/          # Your Markdown content files
├── static/           # Static assets (images, CSS, etc.)
├── docs/            # Output directory for generated site
├── src/             # Source code
└── template.html    # HTML template for pages
```

## Setup

1. Ensure you have Python 3.x installed
2. Clone this repository
3. Create your content structure:
   - Place Markdown files in the `content/` directory
   - Add static assets in the `static/` directory
   - Customize `template.html` as needed

## Usage

### Building the Site

Run the build script:

```bash
python3 src/main.py "/your-base-path/"
```

Replace `/your-base-path/` with your desired base URL path (e.g., "/static-site-generator/").

### Development Server

To preview your site locally:

```bash
cd docs && python3 -m http.server 8888
```

Then visit `http://localhost:8888` in your browser.

## Template Format

The `template.html` file should include these placeholders:
- `{{ Title }}` - Will be replaced with the page title
- `{{ Content }}` - Will be replaced with the page content
