# Deployment Documentation

## GitHub Actions Workflows

This repository uses GitHub Actions to automatically build, deploy, and maintain the Quarto website.

## Primary Workflows

### 1. Render and Publish (`quarto-publish.yml`)

Builds and deploys the Quarto website to GitHub Pages.

**Triggers:**
- Push to `main` branch
- Pull requests to `main` (builds only, no deployment)
- Manual workflow dispatch

**Jobs:**
- **Build**: 
  - Checks out repository
  - Sets up Python 3.12 with pip caching
  - Installs dependencies from `requirements.txt`
  - Sets up Quarto with TinyTeX
  - Renders the Quarto project
  - Uploads artifacts (PR preview or Pages artifact)
  - Creates comprehensive build summary
  
- **Deploy** (main branch only):
  - Deploys built site to GitHub Pages
  - Creates deployment summary with site URL

**Features:**
- ✅ Python dependency caching for faster builds
- ✅ Timeout protection (15 min build, 10 min deploy)
- ✅ Enhanced summaries with markdown tables and links
- ✅ PR preview artifacts with 7-day retention
- ✅ Proper concurrency control
- ✅ Latest stable action versions

### 2. Sync Member Publications (`sync-member-posts.yml`)

Automatically synchronizes member publication posts.

**Triggers:**
- Daily at 6 AM UTC (scheduled)
- Manual workflow dispatch
- When `members.yml` or `sync_member_posts.py` is modified

**Features:**
- ✅ Python 3.12 with pip caching
- ✅ Automated git commits with proper bot identity
- ✅ Skip CI on sync commits to prevent workflow loops
- ✅ Enhanced summaries with publication counts
- ✅ Timeout protection (15 minutes)
- ✅ Efficient change detection

## Manual Workflow Execution

### Trigger a Build and Deploy:
1. Go to [Actions tab](../../actions)
2. Select "Render and Publish"
3. Click "Run workflow"
4. Choose the branch and click "Run workflow"

### Trigger Publication Sync:
1. Go to [Actions tab](../../actions)
2. Select "Sync Member Publications"
3. Click "Run workflow"

## Monitoring

- **Build Status**: Check the [Actions tab](../../actions) or the badge in README
- **Deployment URL**: Available in deployment job summary
- **Logs**: Full logs available for each workflow run

## Configuration

### Environment Variables
- `GITHUB_TOKEN`: Automatically provided by GitHub Actions

### Permissions
- **Render and Publish**: `contents: read`, `pages: write`, `id-token: write`
- **Sync Member Publications**: `contents: write`

### Timeouts
- Build job: 15 minutes
- Deploy job: 10 minutes
- Sync job: 15 minutes

## Optimization Features

1. **Caching**: Python dependencies are cached to speed up builds
2. **Concurrency**: Prevents multiple simultaneous deployments
3. **Conditional Execution**: Deploy only runs on main branch
4. **Compression**: PR artifacts use level 6 compression
5. **Skip CI**: Publication sync commits skip CI to prevent loops

## Troubleshooting

### Build Failures
Check the build summary in the Actions tab for detailed information about:
- Event type and branch
- Commit SHA
- Links to artifacts and logs

### Deployment Not Triggering
Ensure:
- You're pushing to the `main` branch
- The build job completed successfully
- No other deployment is in progress

### Publication Sync Issues
- Check the sync summary for details
- Verify `members.yml` is properly formatted
- Review logs for any API errors