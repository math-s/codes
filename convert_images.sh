#!/bin/bash

# This code converts all the files of a dir: PNG into JPG and JPG into PNG
# You must run it inside the dir
#
#
# Author: Matheus Silva
# matheus.andrade1996@gmail.com


for x in *.png 
do 
	if [ ! -e "${x%.*}.jpg" ]; then	
	convert "$x" "${x%.*}.jpg" ;
	echo "$(tput setaf 1)$(tput setab 7)${x%.*}.jpg created!$(tput sgr 0)"
	fi
done

for y in *.jpg 
do 
	if [ ! -e "${y%.*}.png" ]; then	
	convert "$y" "${y%.*}.png" ;
	echo "$(tput setaf 1)$(tput setab 7)${y%.*}.png created!$(tput sgr 0)"
	fi
done


