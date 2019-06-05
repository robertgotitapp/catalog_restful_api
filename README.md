# Catalog Restful API

## Project Description

This is the restful api that provided simple CRUD actions for Catalog application. The documentation of the API being 
supported can be viewed through this URL: https://robertgotitapp.docs.apiary.io/#

## Built With

Python==3.7.3 <br />
Flask==1.0.2 <br />
Flask-JWT==0.3.2 <br />
Flask-RESTful==0.3.7 <br />
Flask-SQLAlchemy==2.4.0 <br />
marshmallow==2.19.2 <br />
mysql-connector==2.2.9 <br />
pytest==4.5.0 <br />
pytest-cov==2.7.1 <br />
SQLAlchemy==1.3.3 <br />
Werkzeug==0.15.4 <br />
virtualenv==16.5.0 <br />

## Prerequisites

Install MySQL 5.7 on your runtime environment <br />

## Configuration

```virtualenv venv --python=python3``` Create the virtual environment inside catalog_restful_api folder <br />

```source venv/bin/activate``` Activate the virtual environment instance <br />

```pip install -e .``` Install the package required and setup for the unittest for the api <br />

## Running Instruction

```python run.py``` Run the project <br />

```pytest -v``` Run the unittest with detail description <br />

```pytest --cov=app``` Run the unittest with coverage <br />

## Authors
Robert
