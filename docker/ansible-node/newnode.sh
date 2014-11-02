#!/bin/bash

NODE="$1"
PORT="$2"

if [ -z "$PORT" ]
then
  PORT=40001
fi

docker run -d --name "$NODE" -h "$NODE" -p $PORT:22 myansible:node

