#!/bin/bash

# GREEN="\033[32m"
# NO_COLOR="\033[0m" 

# if [ ! -d .venv ]; then 
#     python3 -m venv .venv
# else 
#     echo -e "$GREEN [info] .venv already exists $NO_COLOR"
#     pip3 freeze > requirements.txt
#     flask run --debug 
# fi

waitress-serve --host 0.0.0.0 --call app:create_app