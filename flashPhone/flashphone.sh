#!/bin/bash

if [[ $#>0 ]]; then
	#statements
	python ~/Python/flashPhone/flashphone.py "$1"
else
	python ~/Python/flashPhone/flashphone.py
fi
