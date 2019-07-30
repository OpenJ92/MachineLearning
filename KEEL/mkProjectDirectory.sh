#!/bin/bash

name=$1;zip=$2;txt=$3;path=$4;

mkdir $path$name;
mkdir $path$name/Data;
mkdir $path$name/Data/Visual;
mkdir $path$name/Data/Markdown;
mv $dat $path$name/Data/$zip;
mv $txt $path$name/Data/$txt;
cp -r Helper/ $path$name/Helper/;
cd $path$name; touch __init__.py; unzip Data/$zip -d Data/;
touch Data/transform_config.json
