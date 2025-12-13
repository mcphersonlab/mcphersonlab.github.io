# Dimensions and Altmetric Badge Implementation

## Overview
This document describes the implementation of Dimensions and Altmetric citation metric badges for publications on the McPherson Lab website.

## Implementation Status: ✅ COMPLETE

### What Was Fixed
The publication listing now properly displays Dimensions and Altmetric badges next to each publication entry that has a DOI field.

### Changes Made

#### 1. CSS Layout Fix (`styles.css`)
Added proper grid layout for publication entries to ensure badges are positioned correctly:

```css
/* Publication listing layout */
.quarto-post.image-right {
  display: grid;
  grid-template-columns: 1fr auto auto;
  gap: 1.5rem;
  align-items: start;
  margin-bottom: 2rem;
  padding-bottom: 2rem;
  border-bottom: 1px solid #dee2e6;
}

.quarto-post.image-right .body {
  grid-column: 1;
}

.quarto-post.image-right .metadata {
  grid-column: 2;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  align-items: flex-end;
}

.quarto-post.image-right .thumbnail {
  grid-column: 3;
  width: 150px;
  flex-shrink: 0;
}

.listing-pub-metrics {
  margin-top: 0.5rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  align-items: flex-end;
}
```

#### 2. EJS Template (Already Correct)
The template at `_ejs/publications.ejs` already had the correct structure:

```ejs
<% if (item.doi) { %>
<div class="listing-pub-metrics">
    <div class="__dimensions_badge_embed__" data-doi="<%- item.doi %>" data-style="small_rectangle"></div>
    <div data-badge-type="donut" data-doi="<%- item.doi %>" data-condensed="true" class="altmetric-embed"></div>
</div>
<% } %>
```

#### 3. Script Loading (Already Correct)
External scripts are loaded in `_quarto.yml`:

```yaml
format:
  html:
    include-after-body:
      - text: |
          <script async src="https://badge.dimensions.ai/badge.js" charset="utf-8"></script>
          <script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
```

## Layout Structure

The publication entry now uses a 3-column grid layout:

```
┌────────────────────────────┬──────────────┬──────────────┐
│                            │              │              │
│  Publication Details       │   Badges     │  Thumbnail   │
│  - Title                   │   - Dims     │   Image      │
│  - Author                  │   - Alt      │              │
│  - Journal Info            │              │              │
│                            │              │              │
└────────────────────────────┴──────────────┴──────────────┘
     Column 1 (1fr)           Column 2      Column 3
                              (auto)        (auto, 150px)
```

## How to Use

To add badges to any publication, simply include the `doi` field in the publication's YAML front matter:

```yaml
---
title: "Your Publication Title"
author: ["Author Name"]
doi: 10.1038/nature12373  # Add DOI here
journ: "Journal Name"
issue: issue
page: page
year: 2024
---
```

The badges will automatically appear if:
1. The `doi` field is present and not empty
2. The external badge scripts can load (requires internet connection)
3. The DOI is valid and recognized by Dimensions/Altmetric

## Badge Appearance

### Dimensions Badge
- Style: Small rectangle
- Shows: Citation count
- Color: Blue gradient
- Position: Top of metrics area

### Altmetric Badge
- Style: Donut chart
- Shows: Attention score with colored segments representing different sources
- Position: Below Dimensions badge

## Testing

To verify the implementation:

1. Build the site: `quarto render`
2. View the publications page
3. Look for publications with DOI fields
4. Verify badges appear in the middle column between publication details and thumbnail

## Browser Compatibility

The badges are provided by external services and work in all modern browsers:
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)

## Troubleshooting

**Badges not appearing?**
1. Check that the publication has a `doi` field in its front matter
2. Verify the DOI is valid (format: 10.xxxx/xxxxx)
3. Check browser console for script loading errors
4. Ensure internet connection is available (badges load from external CDNs)

**Layout issues?**
1. Clear browser cache and hard reload
2. Verify `styles.css` is being loaded
3. Check that the grid layout CSS is not being overridden

## Files Modified

- `styles.css` - Added grid layout and badge positioning styles
- `publications/jacobkmcpherson-20250917_test/index.qmd` - Added test DOI for verification

## Files Already Correct (No Changes Needed)

- `_ejs/publications.ejs` - Badge HTML structure
- `_quarto.yml` - External script loading
