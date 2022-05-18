#!/bin/bash
# A header variable X-HolbertonSchool-User-Id must be sent with the value 98
curl -H "X-HolbertonSchool-User-Id: 98" -sX GET "$1"
