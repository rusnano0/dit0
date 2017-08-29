# Just a personal project for learning Django

### TESTING THE API AND RETRIEVING JSON
It is easy to test the API even throught the browser, because of the options
provided by Django Rest Framework.
#### Item API Endpoints
###### GET array of items
```
http://127.0.0.1:8000/api/items/
```
Example output
```
[
    {
        "id": 1,
        "title": "Test Item Name",
        "price": 0,
        "asset_bundle": 1,
        "owner": 1,
        "created": "2017-08-29T19:26:49.577713Z",
        "updated": "2017-08-29T19:26:49.577713Z"
    },
    {
        "id": 2,
        "title": "Second Test item",
        "price": 500,
        "asset_bundle": 1,
        "owner": 1,
        "created": "2017-08-29T22:41:41.341401Z",
        "updated": "2017-08-29T22:41:41.341401Z"
    }
]
```
###### GET one item (by primary key)
```
http://127.0.0.1:8000/api/items/1/
```
Example output
```
{
    "id": 1,
    "title": "Test Item Name",
    "price": 0,
    "asset_bundle": 1,
    "owner": {
        "id": 1,
        "username": "admin",
        "email": "rusnano0@gmail.com"
    },
    "created": "2017-08-29T19:26:49.577713Z",
    "updated": "2017-08-29T19:26:49.577713Z"
}
```
###### POST (Create) one item
```
http://127.0.0.1:8000/api/items
```
#### Asset-Bundles API Endpoints
###### GET Asset-Bundles List 
```
http://127.0.0.1:8000/api/asset-bundles
```
Example Output
```
[
    {
        "id": 1,
        "salt": "xybc123",
        "kind": "image",
        "base_url": "http://CDN.com/uploads/",
        "owner": 1,
        "created": "2017-08-29T01:33:59.159746Z"
    },
    {
        "id": 2,
        "salt": "qdgj44xf",
        "kind": "image",
        "base_url": "http://cdn.com/uploads/",
        "owner": 1,
        "created": "2017-08-29T21:33:26.118787Z"
    }
]
```
###### GET one Asset-Bundle Details (by primary key)
```
http://127.0.0.1:8000/api/asset-bundles/1/
```
Example output:
```
{
    "id": 1,
    "salt": "xybc123",
    "kind": "image",
    "base_url": "http://CDN.com/uploads/",
    "owner": {
        "id": 1,
        "username": "admin",
        "email": "rusnano0@gmail.com"
    },
    "asset_urls": [
        {
            "original": "http://CDN.com/uploads/image/xybc123_original.jpeg"
        },
        {
            "large": "http://CDN.com/uploads/image/xybc123_large.jpeg"
        },
        {
            "small": "http://CDN.com/uploads/image/xybc123_small.jpeg"
        }
    ],
    "created": "2017-08-29T01:33:59.159746Z",
    "updated": "2017-08-29T01:33:59.160245Z"
}
```

### Current Models
1. Profile
2. AssetBundle
3. Asset
4. Item
5. Comment
6. Like

### Notes on CDN storage
The assets will probably be stored on some CDN as this example:<br />
```http://CDN.com/uploads/{ab_kind}/{ab_salt}_{a_kind}.{a_extension}```<br />
where ab_kind, ab_salt are AssetBundle -> kind, salt<br />
where a_kind, a_extension are Asset -> kind, extension
<br /><br />

So the Asset Model has a method ```full_url``` to generate the urls<br />
Example: 
```
http://CDN.com/uploads/image/xybc123_small.jpeg
http://CDN.com/uploads/image/xybc123_large.jpeg
http://CDN.com/uploads/image/xybc123_original.jpeg
```

In the Admin there will be Preview Images in the Assets section, when the
```CDN_BASE_URL = "http://CDN.com/uploads/"``` will be set to the real version of a CDN.
