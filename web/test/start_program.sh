#!/bin/bash

# This script is used to start the web server.
#node_check = which node > /dev/null
#sc_check = which tsc > /dev/null
node_check = type -P node
sc_check = type -P tsc

if node_check && tsc_check;
   then
        echo "Node and TypeScript are installed"
        if [ -f selectionView/selectionView.ts ]; then
            echo "File selectionView.ts exists"
            tsc selectionView/selectionView.ts
            firefox selectionView/selectionView.html
        else
            echo "File selectionView.ts does not exist. Stopping process"
            exit 1
        fi
        
   else
        echo "Node and TypeScript are not installed. Stopping process"
        exit 1
fi