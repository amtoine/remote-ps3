#!/usr/bin/env bash

source config/install.sh

if [ -d "$venv" ]; then
  $RM -rf "$venv"
else
  echo "$venv is not installed..."
fi

if [ -f "$bin/$exe" ]; then
  $RM "$bin/$exe"
else
  echo "$bin/$exe is not installed..."
fi

if [ -f "$exe" ]; then
  $RM "$exe"
else
  echo "$exe not built..."
fi
