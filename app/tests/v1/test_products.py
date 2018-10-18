from app import create_app
import pytest
from flask import json
#from app import create_app
from app.api.V1.views.products import Products

config = 'TESTING'
app = create_app(config)


sample_product=[
    {"name":"phones", "price":"abc",    "image":"image"},
    {"name":"phones", "price":"-200",   "image":"image"},
    {"name":"123", "price":"200",   "image":"image"},
    {"name":"", "price":"200",  "image":"image"},
    {"name":"phones", "price":"",   "image":"image"},
    {"name":"phones", "price":"200",    "image":""},
    {"name":"phones", "price":"200",    "image":"image"}
]



sample_product_updates=[
    {"price":"300", "image":"image1"},
    {"price":"-300",    "image":"image1"},
    {"price":"abc", "image":"image1"},
    {"price":"300", "image":""},
    {"price":"",    "image":"image1"},
    {"price":"300", "image":"image1"},
    {"price":"",    "image":""}
]




'''-------------------------------------------------------------------------------------------------------------------------------'''

#GET ALL products TESTS


def test_products_retrive_all():
    result=app.test_client()
    response= result.get('/products',content_type='application/json')
    assert(response.status_code==404)

'''-------------------------------------------------------------------------------------------------------------------------------'''

#ADD product TESTS


def test_product_price_not_digit():
    result=app.test_client()
   
    response= result.post('/api/v1/add_product', data=sample_product[0] ,content_type='application/json')
    assert(response.status_code==404)

def test_product_price_not_digit1():
    result=app.test_client()
   
    response= result.post('/api/v1/add_product', data=sample_product[1] ,content_type='application/json')
    assert(response.status_code==400)

def test_products_product_name_not_str():
    result=app.test_client()
   
    response= result.post('/api/v1/add_product', data=sample_product[2] ,content_type='application/json')
    assert(response.status_code==400)

def test_products_product_name_empty():
    result=app.test_client()
   
    response= result.post('/api/v1/add_product', data=sample_product[3] ,content_type='application/json')
    assert(response.status_code==400)

def test_products_price_empty():
    result=app.test_client()
   
    response= result.post('/api/v1/add_product', data=sample_product[4] ,content_type='application/json')
    assert(response.status_code==400)

def test_product_image_empty():
    result=app.test_client()
    
    response= result.post('/api/v1/add_product', data=sample_product[5] ,content_type='application/json')
    assert(response.status_code==400)

def test_product_successfully():
    result=app.test_client()
   
    response= result.post('/api/v1/add_product', data=json.dumps(sample_product[6]) ,content_type='application/json')
    json.loads(response.data)
    assert(response.status_code==201)

'''-------------------------------------------------------------------------------------------------------------------------------'''

#GET SPECIFIC product TESTS


def test_get_product_negative_identifier():
    result=app.test_client()
    response= result.get('/api/v1/product/-1' ,content_type='application/json')
    assert(response.status_code == 404)

def test_get_product_not_added():
    result=app.test_client()
    response= result.get('/api/v1/products/100' ,content_type='application/json')
    assert(response.status_code == 404)

def test_get_product_successfully():
    result=app.test_client()
    response= result.get('/api/v1/products/1' ,content_type='application/json')
    assert(response.status_code == 200)

'''-------------------------------------------------------------------------------------------------------------------------------'''

#UPDATE product TESTS

#FIND product TESTS

def test_update_product_nonexistent():
    result=app.test_client()
    
    response= result.put('/api/v1/products/100', data=sample_product_updates[0] ,content_type='application/json')
    assert(response.status_code==400)

def test_products_update_price_not_digit():
    result=app.test_client()
   
    response= result.put('/api/v1/add_product', data=sample_product_updates[1] ,content_type='application/json')
    assert(response.status_code==405)

def test_products_update_price_not_digit1():
    result=app.test_client()
   
    response= result.put('/api/v1/products/1', data=sample_products_updates[2] ,content_type='application/json')
    assert(response.status_code==400)

def test_update_products_none():
    result=app.test_client()
    
    response= result.put('/api/v1/products/1', data=json.dumps(sample_product_updates[6]) ,content_type='application/json')
    assert(response.status_code==406)

def test_update_product_price_only_successfully():
    result=app.test_client()
   
    response= result.put('/api/v1/products/1', data=json.dumps(sample_products_updates[3]) ,content_type='application/json')
    assert(response.status_code==200)


def test_update_product_both_successfully():
    result=app.test_client()
   
    response= result.put('/api/v1/products/1', data=json.dumps(sample_product_updates[5]) ,content_type='application/json')
    assert(response.status_code==200)

'''-------------------------------------------------------------------------------------------------------------------------------'''


