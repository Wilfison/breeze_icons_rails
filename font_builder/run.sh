#!/usr/bin/env bash

# clear svg colors
if [ ! -d "./dist" ]; then
  mkdir ./dist && python3 clear_svgs.py
fi

grunt --verbose webfont &&
  rm -rf ../assets/fonts &&
  mkdir ../assets/fonts &&
  cp "../docs/_Breeze Icons.scss" ../assets/stylesheets/_breeze-icons.scss &&
  cp -f ../docs/breeze-icons.ttf ../assets/fonts &&
  rm "../docs/_Breeze Icons.scss" &&
  mv ../docs/index.html.html ../docs/index.html
