#!/bin/bash
# shows allowed methods by server
curl -s -i -X OPTIONS "$1" | sed -n '/^Allow:/ s/Allow: //p'
