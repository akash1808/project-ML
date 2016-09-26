#!/bin/bash
cat $1 | awk -F, '{print $1","$3","$4}' > $2
