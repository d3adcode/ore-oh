#!/bin/sh
# must be run in poetry shell

gunicorn statistics:app
