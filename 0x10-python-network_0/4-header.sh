#!/bin/bash
# A header variable X-HolbertonSchool-User-Id must be sent with the value 98
curl -s -X GET "$1" -H "X-School-User-Id: 98"
