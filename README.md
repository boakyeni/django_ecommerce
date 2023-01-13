## Django Ecommerce

This is the backend for an ecommerce website implemented with techiniques of a test-first approach and DRF (Django Rest Framework). It is ready to be integrated with front-end framework of choice, but personally I like to integrate with Next.js. Features include a recommendation engine and product variance selection.

## Tips 
Here are some helpful command line scripts for automating workflow:\
- To convert .csv to .json, replace 'my.csv' with input filename and 'my.json' with output filename:\
    `cat my.csv | python -c 'import csv, json, sys; print(json.dumps([dict(r) for r in csv.DictReader(sys.stdin)]))' | > my.json`\
At this point the file is proper json, however not formatted for django. To format for django open the file click command + shift + H, if using vscode deselect all files not to be edited and replace the following:
   * <"web_id"> with <"fields": { "web_id> including quotes and excluding angle brackets
   * <},> with <}},> 
   * finally the ending curly bracket shouldbe doubled, so add an extra <}> before the final closing square bracket
 A script automating this is coming soon.

Running commands with Docker example:
`docker-compose exec web python manage.py load-fixtures`



### Setup
Chromedriver is needed for unit tests. Download for your specific version of Google Chrome at https://chromedriver.chromium.org/downloads

Start virtual enviroment
`source venv/bin/activate`

To get test database\
`python3 manage.py load-fixtures`






