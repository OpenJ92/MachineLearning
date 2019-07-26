#!/bin/bash

name=$1;dat=$2;txt=$3;path=$4;

mkdir $path$name;
mkdir $path$name/Data;
mkdir $path$name/Data/Visual;
mv $dat $path$name/Data/$dat;
mv $txt $path$name/Data/$txt;
cp -r Helper/ $path$name/Helper/;
cd $path$name; touch __init__.py; unzip Data/$dat -d Data/;
