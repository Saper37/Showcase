#!/bin/bash
sudo docker stop myapp-client-1 myapp-middle-1 myapp-middle_last-1 myapp-server-1 && sudo docker rm -f myapp-client-1 myapp-middle-1 myapp-middle_last-1 myapp-server-1 && sudo docker image rm client middle middle_last server && sudo docker network rm myapp_testnetwork
