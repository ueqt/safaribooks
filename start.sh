#!/bin/bash
set -e
python index.py
python all.py
node epub
node indexall