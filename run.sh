#!/bin/sh
export FLASK_ENV=development
export FLASK_APP=run.py
cd core/static
yarn run css-build
cd ../..
flask run