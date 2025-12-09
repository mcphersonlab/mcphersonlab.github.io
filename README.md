# McPherson Lab Website

[![Deploy to GitHub Pages](https://github.com/mcphersonlab/mcphersonlab.github.io/actions/workflows/quarto-publish.yml/badge.svg)](https://github.com/mcphersonlab/mcphersonlab.github.io/actions/workflows/quarto-publish.yml)

This repository contains the source code for the McPherson Lab research website, built with [Quarto](https://quarto.org/) and deployed using GitHub Actions.

## Quick Start

To work with this website locally:

1. Install [Quarto](https://quarto.org/docs/get-started/)
2. Clone this repository
3. Run `quarto preview` to start a local development server
4. Edit the `.qmd` files to update content
5. Run `quarto render` to build the site

## Repository Structure

- `index.qmd` - Homepage
- `about.qmd` - About the group
- `research/` - Research areas and projects
- `publications/` - Publications and research posts
- `people/` - Group members and alumni
- `members.yml` - Organization member configuration for post synchronization
- `sync_member_posts.py` - Script for syncing member posts
- `_quarto.yml` - Quarto configuration
- `styles.css` - Custom CSS styling
- `misc/` - Documentation and license files

## Documentation

- [Full Documentation](misc/README.md) - Detailed information about the website structure
- [Member Sync Documentation](misc/MEMBER_SYNC_DOCS.md) - Documentation for the member publication synchronization system

## Deployment

The website is automatically deployed to GitHub Pages using GitHub Actions when changes are pushed to the main branch.

## License

MIT License - see [misc/LICENSE](misc/LICENSE) file for details.
