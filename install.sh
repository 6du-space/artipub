#!/usr/bin/env sh

cd $(dirname "$0")

if ! hash pipenv 2>/dev/null; then
pip3 install pipenv -i https://mirrors.aliyun.com/pypi/simple/
fi

if [ ! -f "Pipfile.lock" ]; then
pipenv install
fi

pipenv run ./make.py
