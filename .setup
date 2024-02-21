#!/bin/bash
files=$(ls)

makeExecutable() {
    if [[ ! $1 == *"."* ]]; then
        $(chmod +x $1)
    fi
}

for file in $files
do
    makeExecutable $file
done