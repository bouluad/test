#!/bin/bash

HARBOR_HOST="your-harbor-hostname"
PROJECT_NAME="your-project-name"
REPO_NAME="your-repository-name"

# Set Harbor authentication credentials
USERNAME="your-username"
PASSWORD="your-password"

# Get the current week number
current_week=$(date +%V)

# Make a request to the Harbor API to retrieve the tags
response=$(curl -s -u "$USERNAME:$PASSWORD" "https://$HARBOR_HOST/api/repositories/$PROJECT_NAME/$REPO_NAME/tags")

# Parse the JSON response to extract the tags
tags=$(echo "$response" | jq -r '.[].name')

# Find the tag that contains the current week number
matching_tag=""
for tag in $tags; do
  if [[ $tag == *"$current_week"* ]]; then
    matching_tag=$tag
    break
  fi
done

# Print the tag
if [ -n "$matching_tag" ]; then
  echo "Tag containing the current week number ($current_week): $matching_tag"
else
  echo "No tag found for the current week number."
fi
