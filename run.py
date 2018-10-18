from app import create_app 

CONFIG_TYPE = 'development' 
app = create_app(CONFIG_TYPE)

if __name__ == '__main__': 
    app.run()