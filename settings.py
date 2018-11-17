# script to instruct API on how it should perform, to configure behavior of our API

MONGO_URI = 'mongodb://localhost:27017/eve_course'


RESOURCE_METHODS = ['GET','POST','DELETE']


# set the DOMAIN, where you design your API surface

# we want to define a schema against which every single document coming into our people endpoint will be validated
schema = {
    'firstname': {'type':'string'},
    'lastname': {'type':'string'},
}

# every key in this dictionary is an endpoint and value is another dictionary where you configure your endpoint behavior
DOMAIN = {
    'people': {
        'schema' : schema    #the schema for the people endpoint is previously defined schema
    }
}