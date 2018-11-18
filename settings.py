# script to instruct API on how it should perform, to configure behavior of our API

# X_DOMAINS = None # this tells our Eve instance that it should not accept the requests coming from web pages
                   # which are not in the same domains as the server, which is usually not the case

X_DOMAINS = '*'    # if you have public server, you want to accept incoming requests from anybody

X_DOMAINS_RE = ['^http://sub-\d{3}\.example\.com$'] # we only accepting requests from http://sub-\d  or  \.example\.com
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