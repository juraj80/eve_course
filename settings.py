# script to instruct API on how it should perform, to configure behavior of our API

# mongo connection string to local instance
# see http://docs.mongodb.com/manual/reference/connection-string/
MONGO_URI = 'mongodb://localhost:27017/eve_course'

# global methods allowed at the resource (collection) endpoint, to allow clients to write, edit or delete
RESOURCE_METHODS = ['GET','POST','DELETE']
# global methods allowed at the document (item) endpoint
ITEM_METHODS = ['GET','PATCH','PUT','DELETE']

# if False, we need to add an if match header every single time we perform an edit operation on a document
IF_MATCH = False

# PATCH - to edit document
# PUT - to replace document
# DELETE - to delete document

# set the DOMAIN, where you design your API surface

# we want to define a schema against which every single document coming into our people endpoint will be validated
people_schema = {
    'firstname': {'type':'string'},
    'lastname': {'type':'string'},
}

# every key in this dictionary is an endpoint and value is another dictionary where you configure your endpoint behavior
DOMAIN = {
    'people': {
        'schema' : people_schema    #the schema for the people endpoint is previously defined schema
    },
    'works':{                       #we want this endpoint to be read only, so we overwrite the global setting
        'resource_methods': ['GET'],
        'item_methods': ['GET']
    }

}