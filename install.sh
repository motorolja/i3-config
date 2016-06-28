#!/bin/bash

# Get current directory, assumed to be where the config files are
CONFIG_DIR=${PWD}

# Create a symlink of the config directory to where i3 looks for the config
ln -s "$CONFIG_DIR" "$HOME/.config/i3"
