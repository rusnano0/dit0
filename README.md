### API URLS (JSON)
GET array of items
```
http://127.0.0.1:8000/api/items/
```
GET one item (by primary key)
```
http://127.0.0.1:8000/api/items/1/
```
POST one item
```
http://127.0.0.1:8000/api/items
//Example with required fields
{
	"title" : " Generated through API (POST)",
	"owner_id" : 1
}
```