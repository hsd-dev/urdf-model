#!/bin/bash


# read the component list YAML file and return JSON
component_list=$(python3 -c \
    "import json
import sys;
import yaml;
from pathlib import Path;
print(json.dumps(yaml.safe_load(Path('$1').read_text())))" \
| jq -c '.components[]')

apt-get install tree
# Loop through each component and extract keys
echo "$component_list" | while IFS= read -r component; do
    repo=$(echo $component | jq '.repo')
    repo=${repo//\"/}
    branch=$(echo "$component" | jq -r '.branch')
    version=$(echo "$component" | jq -r '.version')
    package=$(echo "$component" | jq -r '.package')
    urdf=$(echo "$component" | jq -r '.urdf')

    echo "Repo: $repo"
    echo "Branch: $branch"
    echo "Version: $version"
    echo "Package: $package"
    echo "URDF: $urdf"

    repo_name=${repo//\"/}
    repo_name=$(basename "$repo_name")
    echo "--------------------------------"

    cd $2   # cd into parent directory

    git clone --single-branch --branch $branch $repo \
        && cd $repo_name \
        && git reset --hard $version

    # delete all folders inside repo, except the target description package
    # this is to avoid building unncessary packages and installing unecessary deps in the process
    if [ -d "$package" ]; then
        find ./ -mindepth 1 ! -regex "^./$package\(/.*\)?" -delete

        # multiple packages might be on the component list from the same repo
        # won't be able to clone the repo again, if it alread exists
        cd $2
        find ./ -type d -name $package -exec mv -t $2 {} +
        rm -r $repo_name
    fi
done
