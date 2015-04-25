#!/bin/bash
. /usr/bin/virtualenvwrapper.sh
mkvirtualenv -p $(which python2) vcopernicus
pip install -r vcopernicus/requirements.txt
