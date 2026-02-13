#!/bin/bash

FILENAME=$1
TEMPFILE=/tmp/extracor-shell-output

if [[ -f "$FILENAME" ]]; then
    echo "File $FILENAME exists and is a regular file."
else
    echo "File $FILENAME does not exist or is not a regular file."
    exit
fi

if [[ $(file $FILENAME | awk -F " " '{print $2}') == "gzip" || $(file $FILENAME | awk -F " " '{print $2}') == "zlib" ]]; then

  count=1

  while [[ $(file $FILENAME | grep -o gzip) == "gzip"  || $(file $FILENAME | grep -o zlib) == "zlib" ]]; do
        echo "Extraction $count"
        gzip -d --stdout $FILENAME > $TEMPFILE
        if [ -s "$TEMPFILE" ]; then
                cp $TEMPFILE $FILENAME
        else
                echo "Something broke"
                break
        fi
        ((count++))
  done

  echo "Done (maybe?)"
else
  echo "Not a compressed file"
fi
