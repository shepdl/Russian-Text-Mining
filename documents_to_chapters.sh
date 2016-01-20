#!/bin/bash

target_dir="$2"
mkdir -p $target_dir
for in_file in $(find $1 -name "*.htm" -type f)
do
    directory_base=dirname $in_file
    file_output_directory=basename $in_file
    target_path=$target_dir/$directory_base/$file_output_directory
    mkdir -p $target_path
    # echo "Extracting chapters from $in_file to $target_path"
    python documents_to_chapters.py $in_file $target_path
done
                
