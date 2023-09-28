#!/bin/bash

# TODO: is this always needed?
# check if exists and is running -- else script fails
# $1 = docker image name
# $2 = docker container name

docker container stop $2
docker container rm $2

docker run -it --name $2 --net host -p 5500:5500 -p 5008:5008 -d $1

docker exec -it -d $2  /bin/bash -c "source /app/kinematic_components_web_app/static/moveit2_ws/install/setup.bash; \
    flask --app app run --host 0.0.0.0 --port 5500"

docker exec -it -d $2 /bin/bash -c \
    "java -jar /ls/kinematics-model/de.fraunhofer.ipa.kinematics.xtext.parent/de.fraunhofer.ipa.kinematics.xtext.ide/target/de.fraunhofer.ipa.kinematics.xtext.ide-1.0.0-SNAPSHOT-ls.jar \
        -port 5008 -host 0.0.0.0"

docker exec -it $2 /bin/bash -c \
    ". /app/kinematic_components_web_app/static/moveit2_ws/install/setup.sh \
        && ros2 run kinematics_model_generator batch_model_generator.py \
            ./static/moveit2_ws/src/urdf-model/component_list.yaml \
            ./static/moveit2_ws/src/urdf-model/kinematics-model-parser/kinematics_model_generator/models"