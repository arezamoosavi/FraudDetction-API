#!/bin/sh

set -o errexit
set -o nounset


docker-compose exec web python data_check.py
