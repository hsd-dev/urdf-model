# urdf-model

## Installation

Use docker container to simplify setting up the toolchain:
```
git clone git@github.com:ipa-hsd/urdf-model.git
cd urdf-model
docker build  -t urdf-toolchain
```

## Usage

Start the docker container which starts the kinematic language server and the kinematic component database
```
. ./kinematics-model-parser/scripts/start_docker.sh urdf-toolchain:latest urdf-toolchain
```
