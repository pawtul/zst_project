#! /bin/bash

sudo docker inspect --format '{{ .State.Pid }}' "$@"
