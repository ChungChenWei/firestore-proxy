#!/bin/bash
image_name=firestore-proxy
container_name=firestore-proxy

mode=$1

if [[ $mode == "build" ]]; then
    docker rmi $(docker images | grep ${image_name} | awk '{print $3}')
    docker build -t ${image_name} .
    docker rmi $(docker images | grep none | awk '{print $3}')
fi

if [[ $mode == "run" ]]; then
    docker run -it --rm -d \
        -p 3000:3000 \
        -v $PWD/credential.json:/app/credential.json \
        --name ${container_name} \
        ${image_name}
fi

if [[ $mode == "dev" ]]; then
    docker run -it --rm \
        -p 3000:3000 \
        -v $PWD/src:/app \
        -v $PWD/credential.json:/app/credential.json \
        --name ${container_name} \
        ${image_name} /bin/bash
fi
