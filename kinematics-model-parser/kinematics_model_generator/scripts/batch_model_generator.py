#!/usr/bin/env python3

import json
from kinematics_model_generator import parse_urdf
from pathlib import Path
import requests
import sys
import yaml


def download_file(repo, branch, version, urdf):
    raw_repo = repo.replace('github', 'raw.githubusercontent').strip('/')
    repo_name = raw_repo.split('/')[-1]
    raw_file = raw_repo + '/' + version + '/' + urdf.replace(repo_name, '', 1)
    output = requests.get(raw_file).text
    
    return output


def get_model_file_name(rel_path_name):
    filename = rel_path_name.split('/')[-1].replace('urdf', 'kin')
    return filename


def generate_models(component_list, output_folder):
    for component in component_list['components']:
        urdf_str = download_file(component['repo'], component['branch'], component['version'], component['urdf'])
        model_filename=get_model_file_name(component['urdf'])
        output = output_folder.rstrip('/') + '/' + model_filename

        parse_urdf(urdf_str, None,
            output=output,
            repo=component['repo'],
            branch=component['branch'],
            version=component['version'],
            package=component['package'],
            distro='humble',
            category=component['category'],
            push_to_db=True)

if __name__ == "__main__":
    component_list_file = sys.argv[1]   # config/component_list.yaml
    output_folder = sys.argv[2]         # folder where the kinematic models should be stored
    component_list = yaml.safe_load(Path(component_list_file).read_text())
    generate_models(component_list, output_folder)
