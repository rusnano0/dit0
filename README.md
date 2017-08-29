# Just a personal project for learning Django

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

### Current Models
1. Profile
2. AssetBundle
3. Asset
4. Item
5. Comment
6. Like

### Notes
The assets will probably be stored on some CDN as this example:<br />
```http://CDN.com/uploads/{ab_kind}/{ab_salt}_{a_kind}.{a_extension}```<br />
where ab_kind, ab_salt are AssetBundle -> kind, salt<br />
where a_kind, a_extension are Asset -> kind, extension