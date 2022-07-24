#!/bin/bash

function traverse() {
for file in "$1"/*
do
    if [ ! -d "${file}" ] ; then
        if [ "${file: -6}" == ".ipynb" ] ; then
            black "$file"

            python3 -m ipykernel install --user --name python3
            python3 -m jupyter nbconvert --to notebook --execute "$file" --output "$file"
            python3 -m jupyter nbconvert --to markdown "$file" --output README.md
        fi
    else
        traverse "${file}"
    fi
done
}

function main() {
    traverse "$1"
}

main "$1"
