from app import create_app
import pytest
from flask import json
#from app import create_app
from app.api.V1.views.sales import sales

config = 'TESTING'
app = create_app(config)




#SALE INPUT FOR TESTS

sample_sale=[{
            
            
                            
                            "product":"tv",
                            "quantity":"abc",
                            "total":"200"
                            },
                            
            
           
             
            
            
                            {
                            "product":"123",
                            "quantity":"4",
                             "total":"200"
                            },
                            
           
          
            
            
            
              
                            {
                            "product":"",
                            "quantity":"4",
                             "total":"200"
                            },
                            
            
            
            
             
                            {
                            "product":"tv",
                            "quantity":"",
                             "total":"200"
                            },
                            
            
            
             
                            {
                            "product":"tv",
                            "quantity":"4",
                             "total":""
                            },
                            
            
             
            
                            {
                            "product":"tv",
                            "quantity":"4",
                             "total":"200"
                            },
                           
            
            
           
             
                            {
                            "product":"",
                            "quantity":"",
                             "total":""
                            },
            
            
             
                            {
                            "product":"tv",
                            "quantity":"4",
                             "total":"200"
                            }]
                            
        








'''-------------------------------------------------------------------------------------------------------------------------------'''

#GET ALL SALES TESTS


def test_sales_retrive_all():
    result=app.test_client()
    
    response= result.get('/api/v1/sales',content_type='application/json')
    assert(response.status_code==500)

'''-------------------------------------------------------------------------------------------------------------------------------'''

#ADD SALE TESTS


def test_sale_quantity_not_digit():
    result=app.test_client()
   
    response= result.post('/api/v1/add_sale', data=json.dumps(sample_sale[0]) ,content_type='application/json')
    assert(response.status_code==404)
    

def test_sales_product_name_not_str():
    result=app.test_client()
   
    response= result.post('/api/v1/add_sale', data=json.dumps(sample_sale[1]) ,content_type='application/json')
    assert(response.status_code==404)
    

def test_sales_product_name_empty():
    result=app.test_client()
    
    response= result.post('/api/v1/add_sale', data=json.dumps(sample_sale[2]) ,content_type='application/json')
    assert(response.status_code==404)
    

def test_sales_quantity_empty():
    result=app.test_client()
   
    response= result.post('/api/v1/add_sale', data=json.dumps(sample_sale[3]) ,content_type='application/json')
    assert(response.status_code==404)
    

def test_sales_Total_paid_empty():
    result=app.test_client()
    
    response= result.post('/api/v1/add_sale', data=json.dumps(sample_sale[4]) ,content_type='application/json')
    assert(response.status_code==404)
    


def test_sales_sale_items_empty():
    result=app.test_client()
    
    response= result.post('/api/v1/add_sale', data=json.dumps(sample_sale[6]) ,content_type='application/json')
    assert(response.status_code==404)
    

'''def test_add_sales_successfully():
    result=app.test_client()
    response= result.post('/api/v1/add_sale', data=json.dumps(sample_sale[7]) ,content_type='application/json')
    json.loads(response.data)
    assert(response.status_code==201)'''
    

'''-------------------------------------------------------------------------------------------------------------------------------'''

#GET SPECIFIC SALE TESTS


def test_get_sale_negative_identifier():
    result=app.test_client()
    
    response= result.get('/api/v1/sales/-1' ,content_type='application/json')
    assert(response.status_code == 404)


def test_get_sale_not_created():
    result=app.test_client()
   
    response= result.get('/api/v1/sales/100' ,content_type='application/json')
    assert(response.status_code == 500)

def test_get_sale_successfully():
    result=app.test_client()
   
    response= result.get('/api/v1/sales/1' ,content_type='application/json')
    assert(response.status_code == 500)
