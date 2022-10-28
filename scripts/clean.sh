#!/usr/bin/env bash

source config/install.sh
source scripts/colors.sh

if [ -d "$venv" ]; then
  echo "${yellow}removing ${cyan}$venv${end}!"
  $RM -rf "$venv"
else
  echo "${cyan}$venv${end} is ${red}not installed${end}..."
fi

if [ -f "$bin/$exe" ]; then
  echo "${yellow}removing ${cyan}$bin/$exe${end}!"
  $RM "$bin/$exe"
else
  echo "${cyan}$bin/$exe${end} is ${red}not installed${end}..."
fi

if [ -f "$build/$exe" ]; then
  echo "${yellow}removing ${cyan}$build/$exe${end}!"
  $RM "$build/$exe"
else
  echo "${cyan}$build/$exe${end} is ${red}not built${end}..."
fi

if [ -d "$lib" ]; then
  echo "${yellow}removing ${cyan}$lib${end}!"
  $RM --recursive "$lib"
else
  echo "${cyan}$lib${end} is ${red}not built${end}..."
fi
