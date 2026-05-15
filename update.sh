#!/bin/bash
MESSAGE=${1:-"Update portfolio content"}
git add .
git commit -m "$MESSAGE"
/Users/mukesh/Library/Python/3.9/bin/mkdocs gh-deploy --force
