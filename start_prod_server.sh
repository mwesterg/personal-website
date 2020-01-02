#!/bin/bash


source $PWD/prod_env/bin/activate && python3 manage.py runserver 192.168.0.21:8000

