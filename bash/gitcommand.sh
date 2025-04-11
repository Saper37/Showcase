#!/bin/bash

git_found = type -P git
if git_found;
then
    echo "Git is installed. Following files staged"
    echo git diff --staged --name-only
else
    echo "Git is not installed. Stopping process"
    exit 1
fi


