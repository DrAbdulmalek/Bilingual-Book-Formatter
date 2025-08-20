#!/bin/bash
# Bilingual Book Formatter v2.3 - Upload Script
# This script automates the process of uploading the project to GitHub

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}Bilingual Book Formatter v2.3 - Upload Script${NC}"
echo "=============================================="

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo -e "${RED}Git is not installed. Please install git first.${NC}"
    exit 1
fi

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo -e "${YELLOW}GitHub CLI (gh) is not installed. Releases will need to be created manually.${NC}"
fi

# Get project details
PROJECT_NAME="Bilingual-Book-Formatter"
VERSION="v2.3"
REPO_DIR=$(pwd)
GITHUB_USER="DrAbdulmalek"
GITHUB_TOKEN="$GITHUB_TOKEN"  # Use environment variable

# Validate GITHUB_TOKEN
if [ -z "$GITHUB_TOKEN" ]; then
    echo -e "${RED}Error: GITHUB_TOKEN environment variable is not set. Please set it before running this script.${NC}"
    echo -e "${YELLOW}Example: export GITHUB_TOKEN='your-pat-here'${NC}"
    exit 1
fi

# Check if we're in the right directory
if [[ ! -f "app.py" ]] || [[ ! -f "bilingual_book_formatter.py" ]]; then
    echo -e "${RED}Please run this script from the project root directory.${NC}"
    exit 1
fi

# Initialize git if not already initialized
if [ ! -d ".git" ]; then
    git init
    git config --global --add safe.directory ${REPO_DIR}
    git remote add origin https://${GITHUB_TOKEN}@github.com/${GITHUB_USER}/${PROJECT_NAME}.git
else
    # Update remote URL to include PAT
    git remote set-url origin https://${GITHUB_TOKEN}@github.com/${GITHUB_USER}/${PROJECT_NAME}.git
fi

# Get current branch name (default to 'main' or 'master')
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "master")
if [ "$CURRENT_BRANCH" = "HEAD" ]; then
    CURRENT_BRANCH="master"
fi
if [ "$CURRENT_BRANCH" != "main" ] && [ "$CURRENT_BRANCH" != "master" ]; then
    echo -e "${YELLOW}Renaming branch to main${NC}"
    git branch -m main
    CURRENT_BRANCH="main"
fi

# Check if there are changes to commit
if git diff-index --quiet HEAD -- 2>/dev/null; then
    echo -e "${YELLOW}No changes to commit.${NC}"
else
    # Add all files
    git add .
    
    # Commit with a message
    COMMIT_MESSAGE="Release ${VERSION}: Enhanced features with EPUB support, improved GUI, and API enhancements"
    git commit -m "${COMMIT_MESSAGE}"
    echo -e "${GREEN}Committed changes with message: ${COMMIT_MESSAGE}${NC}"
fi

# Check if remote has commits
REMOTE_COMMITS=$(git ls-remote origin ${CURRENT_BRANCH} | wc -l)
if [ "$REMOTE_COMMITS" -eq 0 ]; then
    # No remote commits, push directly
    echo "No remote commits found. Pushing to remote repository on branch ${CURRENT_BRANCH}..."
    git push -u origin ${CURRENT_BRANCH}
else
    # Pull remote changes to avoid conflicts
    echo "Pulling remote changes with rebase..."
    if ! git pull --rebase origin ${CURRENT_BRANCH} 2>/dev/null; then
        echo -e "${YELLOW}Pull failed due to conflicts. Do you want to force push? (y/n)${NC}"
        read -r FORCE_PUSH
        if [ "$FORCE_PUSH" = "y" ] || [ "$FORCE_PUSH" = "Y" ]; then
            echo -e "${YELLOW}Force pushing to remote repository...${NC}"
            git push -f origin ${CURRENT_BRANCH}
        else
            echo -e "${RED}Aborting push due to conflicts. Please resolve conflicts manually with 'git pull origin main' and merge changes.${NC}"
            exit 1
        fi
    else
        # Push to remote
        echo "Pushing to remote repository on branch ${CURRENT_BRANCH}..."
        git push -u origin ${CURRENT_BRANCH}
    fi
fi

# Check if tag exists remotely
if git ls-remote --tags origin | grep -q "refs/tags/${VERSION}$"; then
    echo -e "${YELLOW}Tag ${VERSION} already exists on remote. Do you want to delete and recreate it? (y/n)${NC}"
    read -r DELETE_TAG
    if [ "$DELETE_TAG" = "y" ] || [ "$DELETE_TAG" = "Y" ]; then
        echo "Deleting remote tag ${VERSION}..."
        git push origin --delete "${VERSION}"
        echo "Creating tag for version ${VERSION}..."
        git tag -a "${VERSION}" -m "Bilingual Book Formatter ${VERSION}" -f
        git push origin "${VERSION}"
    else
        echo -e "${YELLOW}Skipping tag creation since it already exists.${NC}"
    fi
else
    echo "Creating tag for version ${VERSION}..."
    git tag -a "${VERSION}" -m "Bilingual Book Formatter ${VERSION}"
    git push origin "${VERSION}"
fi

# Create a release (if gh CLI is available)
if command -v gh &> /dev/null; then
    echo "Creating GitHub release..."
    # Check if gh is authenticated
    if ! gh auth status &> /dev/null; then
        echo "Authenticating gh CLI with token..."
        gh auth login --with-token <<< "${GITHUB_TOKEN}"
    fi
    # Check if release already exists
    if gh release view "${VERSION}" &> /dev/null; then
        echo -e "${YELLOW}Release ${VERSION} already exists. Do you want to delete and recreate it? (y/n)${NC}"
        read -r DELETE_RELEASE
        if [ "$DELETE_RELEASE" = "y" ] || [ "$DELETE_RELEASE" = "Y" ]; then
            echo "Deleting existing release ${VERSION}..."
            gh release delete "${VERSION}" --yes
            echo "Creating new release ${VERSION}..."
            gh release create "${VERSION}" \
                --title "Bilingual Book Formatter ${VERSION}" \
                --notes "$(cat <<RELEASE_NOTES
## What's New in v2.3

### Major Features
- **Full EPUB Support**: Create EPUB documents with embedded images
- **Enhanced GUI**: Advanced PyQt6 interface with content preview
- **Improved API**: Better error handling and file validation
- **Performance Optimization**: Multiprocessing for large documents
- **Image Processing**: WEBP conversion and duplicate detection

### Technical Improvements
- Configurable image positioning (center, left, right)
- Dynamic font selection based on language
- Google Drive integration for cloud storage
- DeepL translation integration
- Comprehensive error handling

### Usage
```bash
# Command line
python bilingual_book_formatter.py --lang1 english.docx --lang2 arabic.doc
x --output output

# GUI
python bilingual_book_formatter.py --gui

# API
curl -X POST "http://localhost:8000/process/" \
     -F "lang1_file=@english.docx" \
     -F "lang2_file=@arabic.docx" \
     -F "output_format=docx" \
     -F "api_key=your_secret_key"
```

### System Requirements
- Python 3.8+
- 4GB RAM minimum (8GB recommended for large documents)
- 500MB disk space

### Installation
```bash
pip install -r requirements.txt
```
RELEASE_NOTES
)" \
                --target ${CURRENT_BRANCH}
        else
            echo -e "${YELLOW}Skipping release creation since it already exists.${NC}"
        fi
    else
        echo "Creating new release ${VERSION}..."
        gh release create "${VERSION}" \
            --title "Bilingual Book Formatter ${VERSION}" \
            --notes "$(cat <<RELEASE_NOTES
## What's New in v2.3

### Major Features
- **Full EPUB Support**: Create EPUB documents with embedded images
- **Enhanced GUI**: Advanced PyQt6 interface with content preview
- **Improved API**: Better error handling and file validation
- **Performance Optimization**: Multiprocessing for large documents
- **Image Processing**: WEBP conversion and duplicate detection

### Technical Improvements
- Configurable image positioning (center, left, right)
- Dynamic font selection based on language
- Google Drive integration for cloud storage
- DeepL translation integration
- Comprehensive error handling

### Usage
```bash
# Command line
python bilingual_book_formatter.py --lang1 english.docx --lang2 arabic.docx --output output

# GUI
python bilingual_book_formatter.py --gui

# API
curl -X POST "http://localhost:8000/process/" \
     -F "lang1_file=@english.docx" \
     -F "lang2_file=@arabic.docx" \
     -F "output_format=docx" \
     -F "api_key=your_secret_key"
```

### System Requirements
- Python 3.8+
- 4GB RAM minimum (8GB recommended for large documents)
- 500MB disk space

### Installation
```bash
pip install -r requirements.txt
```
RELEASE_NOTES
)" \
            --target ${CURRENT_BRANCH}
    fi
else
    echo -e "${YELLOW}GitHub CLI not found. Creating release using curl...${NC}"
    curl -H "Authorization: token ${GITHUB_TOKEN}" \
         -H "Accept: application/vnd.github.v3+json" \
         https://api.github.com/repos/${GITHUB_USER}/${PROJECT_NAME}/releases \
         -d "{\"tag_name\":\"${VERSION}\",\"name\":\"Bilingual Book Formatter ${VERSION}\",\"body\":\"$(cat <<RELEASE_NOTES
## What's New in v2.3

### Major Features
- **Full EPUB Support**: Create EPUB documents with embedded images
- **Enhanced GUI**: Advanced PyQt6 interface with content preview
- **Improved API**: Better error handling and file validation
- **Performance Optimization**: Multiprocessing for large documents
- **Image Processing**: WEBP conversion and duplicate detection

### Technical Improvements
- Configurable image positioning (center, left, right)
- Dynamic font selection based on language
- Google Drive integration for cloud storage
- DeepL translation integration
- Comprehensive error handling
RELEASE_NOTES
)\",\"draft\":false,\"prerelease\":false}"
fi

echo -e "${GREEN}Upload completed successfully!${NC}"
echo "Project is now available at: https://github.com/${GITHUB_USER}/${PROJECT_NAME}"
