#!/bin/bash

rm -f fips-399.txt
rm -f fips-4??.txt

awk -F _ -f - fips-all.txt << 'EOF'

{ 
  for (i = $2; i <= $3; i++) {
    f = sprintf ("fips-%03d.txt",  i);
    printf "%s_%02d_%02d_%s_%s_%s_%s_%s_%s_%s\n", 
           $1, i, i, $4, $5, $6, $7, $8, $9, $10 >>f; }}
EOF


