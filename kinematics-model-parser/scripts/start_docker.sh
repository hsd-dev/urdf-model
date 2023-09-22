#!/bin/bash

# TODO: is this always needed?
# check if exists and is running -- else script fails
docker container stop urdf-toolchain
docker container rm urdf-toolchain

docker run -it --name urdf-toolchain --net host -p 5500:5500 -d urdf-toolchain:latest

docker exec -it -d urdf-toolchain  /bin/bash -c "flask --app app run --host 0.0.0.0 --port 5500"

docker exec -it urdf-toolchain /bin/bash -c \
    ". /app/kinematic_components_web_app/static/moveit2_ws/install/setup.sh \
        && ros2 run kinematics_model_generator batch_model_generator.py \
            ./static/moveit2_ws/src/urdf-model/kinematics-model-parser/kinematics_model_generator/config/component_list.yaml \
            ./static/moveit2_ws/src/urdf-model/kinematics-model-parser/kinematics_model_generator/models"