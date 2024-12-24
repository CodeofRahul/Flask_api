# Flask_api


## Command Prompt (CMD) shortcuts:

```
- To create directory/Folder = `mkdir <name>`
- To remove directory/Folder = `rmdir <name>`
- To create file = `type nul > app.py`
- to create file using CMD/Powershell : `type <filename> (type template.py)`

```

## Venv shortcuts:


- To create environment = `conda create -p flask_env -y`
- To check available envs = `conda env list`
- To check available envs = `conda info --envs`
- To activate environment = `conda activate flask_env`
- To install requirements.txt = `pip install -r requirements.txt`


## Package related shortcuts

- To check install packages = `pip list`
- To check detailed about package = `pip show package_name`
- To install package = `pip install package_name`
- To uninstall package = `pip uninstall package_name`
- To check python installed version = `python --version`

## Git Command

- To add all file = `git add .`
- 
- To add any particular file = `git add <file_name>`
- 
- To commit = `git commit -m "commit message"`
- 
- To push the code = `git push origin main`

## most common HTTP methods

**GET** : The GET method is used to retrieve data on a server. Clients can use the GET method to access all of the resources of a given type, or they can use it to access a specific resource. For instance, a GET request to the `/products` endpoint of an e-commerce API would return all of the products in the database, while a GET request to the `/products/123` endpoint would return the specific product with an `ID` of `123`. GET requests typically do not include a request body, as the client is not attempting to create or update data.

**POST** : The POST method is used to create new resources. For instance, if the manager of an e-commerce store wanted to add a new product to the database, they would send a POST request to the `/products` endpoint. Unlike GET requests, POST requests typically include a request body, which is where the client specifies the attributes of the resource to be created. For example, a POST request to the `/products` endpoint might have a request body that looks like this:

```API
{
  "name": "Sneakers",
  "color": "blue",
  "price": 59.95,
  "currency": "USD"
}
```

**PUT** : The PUT method is used to replace an existing resource with an updated version. This method works by replacing the entire resource (i.e., the specific product located at the `/products/123` endpoint) with the data that is included in the request’s body. This means that any fields or properties not included in the request body are deleted, and any new fields or properties are added.

**PATCH** : The PATCH method is used to update an existing resource. It is similar to PUT, except that PATCH enables clients to update specific properties on a resource—without overwriting the others. For instance, if you have a product resource with fields for `name`, `brand`, and `price`, but you only want to update the `price`, you could use the PATCH method to send a request that only includes the new value for the `price` field. The rest of the resource would remain unchanged. This behavior makes the PATCH method more flexible and efficient than PUT.

**DELETE** : The DELETE method is used to remove data from a database. When a client sends a DELETE request, it is requesting that the resource at the specified URL be removed. For example, a DELETE request to the `/products/123` endpoint will permanently remove the product with an `ID` of `123` from the database. Some APIs may leverage authorization mechanisms to ensure that only clients with the appropriate permissions are able to delete resources.

**Which HTTP methods are safe?**<br>
GET is the most commonly used safe method, but the HEAD method—which is used to retrieve only the headers of a resource—is also safe.



## docs

- API Glossary : https://www.postman.com/api-glossary/
- Flask api docs : https://flask.palletsprojects.com/en/stable/api/
- Flask user guide : https://flask.palletsprojects.com/en/stable/
- Flask restful docs : https://flask-restful.readthedocs.io/en/latest/
- Jinja docs : https://jinja.palletsprojects.com/en/stable/
- Template Designer Documentation : https://jinja.palletsprojects.com/en/stable/templates/
- Jinja2 docs : https://www.devdoc.net/python/jinja-2.10.1-doc/


## How to access

- After starting the server, access the endpoints using a web browser or a tool like Postman:
- For restaurant information: `http://127.0.0.1:5000/restaurant`
- For menu items: `http://127.0.0.1:5000/menu/Wings`