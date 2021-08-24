#!/bin/bash

for file in dbc_files/*.dbc; do
  ./blast-dbf/blast-dbf "$file" "${file%%.*}.dbf"
  echo "$file converted to dbf"
done
