#!/bin/bash

# Exit in case of error
set -e

python autogenerate_table.py

sudo -u postgres PGPASSWORD=${PG_PASSWORD?Variable not set} psql -h localhost -f ddl_${PG_DB?Variable not set}.sql

python import_first_data.py