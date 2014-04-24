#!/bin/bash

if [[ $#>0 ]]; then
	#statements
	file_name="$1"
	file_path="/home/jiahuixing/bugreport/"
	echo "file_name=$file_path$file_name"
	adb bugreport > "$file_path$file_name"
	echo "Done."
else
	echo "Pls input file name."
fi