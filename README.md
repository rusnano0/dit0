### TESTING THE API AND RETRIEVING JSON
It is easy to test the API even throught the browser, because of the options
provided by Django Rest Framework.

GET array of items
```
http://127.0.0.1:8000/api/items/
```
GET one item (by primary key)
```
http://127.0.0.1:8000/api/items/1/
```
POST (Create) one item
```
http://127.0.0.1:8000/api/items
```