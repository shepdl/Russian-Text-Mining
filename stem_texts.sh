for in_filename in proper-name-test/*.txt
do
    out_filename="stemmed-texts/$(basename $in_filename)"
    ../mystem $in_filename > $out_filename
done
