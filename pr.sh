#!/bin/bash

# Your GitHub personal access token
TOKEN="YOUR_TOKEN"

# Source organization (where you forked from)
SOURCE_ORG="orga1"

# Target organization (where you want to send the PR)
TARGET_ORG="orga2"

# List of repositories you want to create pull requests for in orga2
REPO_LIST=("repo1" "repo2" "repo3")

# Loop through each repository and create a pull request
for REPO in "${REPO_LIST[@]}"; do
  # Create a new branch for the pull request
  NEW_BRANCH_NAME="pull-request-to-$SOURCE_ORG"
  git clone "https://github.com/$TARGET_ORG/$REPO.git"
  cd "$REPO"

  # Add the original repository (orga1) as a remote
  git remote add upstream "https://github.com/$SOURCE_ORG/$REPO.git"

  # Fetch the latest changes from the original repository
  git fetch upstream

  # Create a new branch based on the latest changes from the original repository
  git checkout -b "$NEW_BRANCH_NAME" upstream/main

  # Make changes to the code in the repository
  # ...

  # Commit the changes
  git add .
  git commit -m "Changes for pull request to $SOURCE_ORG from $TARGET_ORG"

  # Push the changes to your fork in orga2
  git push origin "$NEW_BRANCH_NAME"

  # Create a pull request
  curl -X POST -H "Authorization: token $TOKEN" \
    -d '{"title":"Pull Request Title","head":"'$TARGET_ORG':'$NEW_BRANCH_NAME'","base":"main"}' \
    "https://api.github.com/repos/$SOURCE_ORG/$REPO/pulls"

  cd ..
  rm -rf "$REPO"
done
