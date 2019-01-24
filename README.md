# Test django filter

## Installation

Create virtual environment with python 3.6
Install requirements:
    pip install -r requirements/requirements.txt

## Admin User and DB

user: fake@gmail.com
password: x

The DB is an sqlite3 included in the repository.
So no user or pass to access it, straight away working.

## Requests

http  http://localhost:9999/api/v1/activejobs/
http  http://localhost:9999/api/v1/activejobs/?post_category=Telecom
http  http://localhost:9999/api/v1/activejobs/?post_subcategory=Network

