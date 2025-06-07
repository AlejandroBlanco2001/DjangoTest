#!/bin/bash

cd /app/task

# Prepare the migrations
python manage.py makemigrations tasksmanagement

# Run the migrations
python manage.py migrate

# Start the server
python manage.py runserver 0.0.0.0:8000