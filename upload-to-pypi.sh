#!/bin/bash

rm -r dist
python setup.py bdist_wheel sdist
twine upload dist/*
