#!/bin/bash

function traverse() {
for file in "$1"/*
do
    if [ ! -d "${file}" ] ; then
        if [ "${file: -6}" == ".ipynb" ] ; then
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
