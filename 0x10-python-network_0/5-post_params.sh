#!/bin/bash
# A variable email must be sent with the value test@gmail.com
# A variable subject must be sent with the value I will always be here for PLD
curl -s "$1" -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
