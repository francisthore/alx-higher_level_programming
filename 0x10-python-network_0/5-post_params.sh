#!/bin/bash
# sends a post request with parameters
curl -s -X POST --data "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
