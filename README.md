# TESC - Quick search tool

> A tool to monitor TESC-related KPIs.

## Build Setup

``` bash
# setup a virtual environment 
virtualenv venv
cd venv/Scripts/
activate

# install `Python` dependencies
cd ..
cd ..
pip install requirements.txt

# install `node.js` dependencies
cd client/
npm install

# build for production with minification
npm run build

# start the `Flask` development server (the instructions below apply to Windows)
# for more details consult the flask documentation at 
# http://flask.pocoo.org/docs/0.12/quickstart/
cd..
set FLAS_APP=app.py
set FLASK_DEBUG=1
flask run

# open http://localhost:5000 in your broswer
```

For more details, feel free to drop me a line at `m.a.constantin@uvt.nl`.