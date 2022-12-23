## Django Ecommerce

This is the backend for an ecommerce website implemented with a test-first approach and DRF (Django Rest Framework). It is ready to be integrated with front-end framework of choice, but personally I like to integrate with Next.js.

## Tips 
Here are some helpful scripts for automating workflow:\
To convert .csv to .json, replace 'my.csv' with input filename and 'my.json' with output filename
: `cat my.csv | python -c 'import csv, json, sys; print(json.dumps([dict(r) for r in csv.DictReader(sys.stdin)]))' | > my.json`


### Setup
Chromedriver is needed for unit tests. Download for your specific version of Google Chrome at https://chromedriver.chromium.org/downloads





