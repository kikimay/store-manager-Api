# store-manager-Api
This repository holds the API endpoints for the store-manager app.


[![Maintainability](https://api.codeclimate.com/v1/badges/362aef5811d9653097c6/maintainability)](https://codeclimate.com/github/kikimay/store-manager-Api/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/362aef5811d9653097c6/test_coverage)](https://codeclimate.com/github/kikimay/store-manager-Api/test_coverage)
[![Build Status](https://travis-ci.org/kikimay/store-manager-Api.svg?branch=development)](https://travis-ci.org/kikimay/store-manager-Api)
[![codecov](https://codecov.io/gh/kikimay/store-manager-Api/branch/development/graph/badge.svg)](https://codecov.io/gh/kikimay/store-manager-Api)

 http://www.apache.org/licenses/LICENSE-2.0






# STORE-MANAGER-API

store manager api is a store management application. It allows an admin user manage inventory and prevents a user from selling products that are out of stock.
## Getting Started

These instructions will guid you on how to deploy this system locally. For live systems, you will need to consult deployment notes of flask systems for that.

To get started first you need a machine that can run on Python3 and handle postgres database.

### Prerequisites

You will need these installed first before we go any further.

- [Python3.6](https://www.python.org/downloads/release/python-365/)

- [Virtual Environment](https://virtualenv.pypa.io/en/stable/installation/)


For Virtual Environment, you can install like this after Installing Python3:

```
pip install virtualenv
```
```
pip install virtualenvwrapper
```


## Installation and Running


### Installing

Clone the repository below

```
git clone -b development https://github.com/kikimay/STORE-MANAGER-API.git
```

Create a virtual environment

```
    virtualenv venv --python=python3.6
```

Activate virtual environment

```
    source venv/bin/activate
```

Install required Dependencies

```
    pip install -r requirements.txt
```



### Running

Start the flask server on your command prompt:

    First you need to ``` cd ``` to your project root directory

Then:

```
    python run.py
```

With the server running, paste this in your browser's address bar:

```
    localhost:5000/
```

This is the welcome page.



## Running the tests

This repository contains tests to test the functionality of the API.

To run these tests, run the following command:

### Running all tests.

These tests test the ``` sales Class and products Class

In the project's root directory, with the virtual environment running, run this command:

```
pytest
```





# Endpoints Available

|    #  | Method | Endpoint                          | Description                           |
|-------| ------ | --------------------------------- | ------------------------------------- | |    1  | POST   | /api/v1/add_product               | Create a new  product_item            |
|    2  | GET    | /api/v1/products                  | Retrieve all products                 |
|    3  | GET    | /api/v1/product/<int:product_id>  | Retrieve a specific product by id     |
|    4  | DELETE | /api/v1/products/<int:product_id> | Delete a specific product by  id      |
|    5  | PUT    | /api/v1/product/<int:product_id>  |Update a specific product by  id       |
|    6  | POST   | /api/v1/make_sale                 | make a sale                           |
|    7  | GET    | /api/v1/sales                     | Retrieve all sales                    |
|    8  | GET    | /api/v1/sales/<int:sale_id>       | Retrieve a specific sale              |
|                   
|   
 
  *find postman documentation here https://web.postman.co/collections/5645063-c67c3435-303f-48c9-b890-b405e0036463?workspace=2b9a9d79-a360-41c8-850a-bba4b93c2b59
 

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [pip](https://pypi.org/project/pip/) - Dependency Management


## Authors

* **Maryn Mwirigi** -  - [Kikimay](https://github.com/kikimay)


## License

This project is licensed under the Apache License 
  http://www.apache.org/licenses/LICENSE-2.0

