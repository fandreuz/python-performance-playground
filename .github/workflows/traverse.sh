#!/bin/bash

function traverse() {
for file in "$1"/*
do
    if [ ! -d "${file}" ] ; then
        if [ "${file: -6}" == ".ipynb" ] ; then
            black "$file"

            jupyter nbconvert --to notebook --execute "$file" --output "$file"
            jupyter nbconvert --to markdown "$file" --output README.md
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
