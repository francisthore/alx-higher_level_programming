#!/bin/bash
# sends specific header as part of request
curl -s -X GET -H "X-School-User-Id: 98" "$1"
