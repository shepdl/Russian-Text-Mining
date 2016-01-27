#!/bin/bash

in_dir=$1
out_dir=$2

if [ "$#" -ne 2 ] 
then 
    echo ""
    echo "  Usage: $0 input-folder-name output-folder-name"
    echo "  And make sure that output-folder-name does not exist or is empty!"
    echo ""

    exit
fi

mkdir -p $out_dir

for in_filename in $(find $in_dir -name "*.htm")
do
    echo $in_filename
    out_filename_pattern="$out_dir/$(python create_filename_pattern.py $in_filename)"
    counter=0
    $(cat $in_filename | python documents_to_chapters.py) | while read -d "|" in_chunk
    do
        echo $in_chunk | python remove_proper_names.py | ./mystem | python remove_stopwords.py > "$out_filename_pattern---$counter.txt"
        counter+=1
    done
done

mallet-2.0.7/bin/mallet --import-dir --input "$out_dir" --output "$out_dir.mallet" --keep-sequence --token-regex '[\p{L}\p{M}]+'

