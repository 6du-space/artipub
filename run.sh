#!/usr/bin/env sh

cd $(dirname "$0")/dist

docker-compose up -d
