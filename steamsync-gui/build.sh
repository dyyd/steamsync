#!/bin/bash

docker run -v "$(pwd):/src/" cdrx/pyinstaller-windows "EXT=.exe python build.py"
docker run -v "$(pwd):/src/" cdrx/pyinstaller-linux "python build.py"