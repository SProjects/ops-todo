#!/bin/bash
# Get BUMP_LEVEL env variable to determine which figure to update
NEW_VERSION=""

# Read the VERSION file
OLD_VERSION=`cat VERSION`

OIFS="$IFS"
IFS='.'
read -a LEVELS <<< "${OLD_VERSION}"
IFS="$OIFS"

MAJOR=${LEVELS[0]}
MINOR=${LEVELS[1]}
PATCH=${LEVELS[2]}

# Update SEMVAR figure
if [ "$BUMP_LEVEL" == "patch" ]; then
	PATCH="$(($PATCH + 1))"
elif [ "$BUMP_LEVEL" == "minor" ]; then
    MINOR="$(($MINOR + 1))"
else
    MAJOR="$(($MAJOR + 1))"
fi

NEW_VERSION=${MAJOR}.${MINOR}.${PATCH}

echo $NEW_VERSION > VERSION

TAG="v"${NEW_VERSION}

COMMIT_MESSAGE="Updates to version: "${TAG}

# Add and commit the tag
git add .
git commit -m "${COMMIT_MESSAGE}"
git tag -a -m "${COMMIT_MESSAGE}" "${TAG}"

# Push tag
git push origin --tags
