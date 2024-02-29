#!/usr/bin/bash
# Diplays body size of an http response
curl -sI "$1" | grep '^Content-Length' | awk  '{print $2}'