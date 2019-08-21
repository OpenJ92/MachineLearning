#!/bin/bash

name=$1;zip=$2;txt=$3;path=$4;

mkdir $path$name;
mkdir $path$name/Data;
mkdir $path$name/Experiments;
mkdir $path$name/Data/Visual;
mkdir $path$name/Data/Markdown;
mv $zip $path$name/Data/$zip;
mv $txt $path$name/Data/$txt;
cp columns.py $path$name/columns.py
cp hyperparameters.py $path$name/hyperparameters.py
cp -r MasterHelper/ $path$name/Helper/;
cd $path$name; touch __init__.py; unzip Data/$zip -d Data/;
