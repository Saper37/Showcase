#! /bin/bash
echo "reset containers, images and networks"
sudo docker stop python-middle-1
sudo docker stop python-server-1
sudo docker stop  python-client-1
sudo docker network prune
sudo docker container prune
sudo docker image rm testclient testserver testmiddle
