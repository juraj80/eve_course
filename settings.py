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


#EMBEDDING = False # is True by default on global level

# PATCH - to edit document
# PUT - to replace document
# DELETE - to delete document

# set the DOMAIN, where you design your API surface

# we want to define a schema against which every single document coming into our people endpoint will be validated
people_schema = {
    'firstname': {
        'type':'string',
        'minlength':1,
        'maxlength':30,
    },

    'lastname': {
        'type':'string',
        'maxlength':50,
        'required': True,
        'unique': True,   # doesn't apply for bulk inserts
    },

    'middle_name': {
      'dependencies' : ['firstname','lastname', 'location.address'] # the field itself is not required, but if you provide a middle name
                                                                    # you also must provide the first name and last name, otherwise the field
                                                                    # would be rejected
    },

    'born': {'type' : 'datetime'},
#    'age' : {'readonly' : True},  # clients can't write or overwrite it
    'age': {
        'type': 'integer',
        'isodd' : True,
        # 'coerce': int   # converts passed value to integer
    },
    'role' : {
        'type': 'list',
        'allowed': ['author','contributor','copy'],
        'default': ['author']
    },
    'location': {
        'type' : 'dict',
 #       'required': True,
        'schema' : {
            'address': {'type':'string'},
            'city':{'type':'string','required': True}
        },
    },
    'email': {
        'type': 'email'
#        'regex': r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    },
    'prop1' : {
        'anyof_type': ['integer', 'float'],  # example of *of-rules typesaver
        'anyof': [{'min': 0,'max': 10}, {'min': 100, 'max': 110}] # example of *of-rules from http://docs.python-cerberus.org/en/stable/validation-rules.html#of-rules

    }
}

works_schema = {
    'title': {
        'type' : 'string',
        'required' : True,
    },
    'description' : {
        'type' : 'string',
    },
    'owner' : {
        'type' : 'objectid',
        'required' : True,
        # referential integrity constraint: value must exist in the
        # 'people' collection. Since we aren't declaring a 'field' key,
        # will default to 'people._id'.
        'data_relation': {
            'resource' : 'people',
            #make the owner embeddable with  ?embedded={"owner":1}
            'embeddable' : True # it will be ignored, because of embedding at resource level is turned off
        },
    },
}

# every key in this dictionary is an endpoint and value is another dictionary where you configure your endpoint structure
DOMAIN = {
    'people': {
        'schema' : people_schema    #the schema for the people endpoint is previously defined schema
    },
    'works':{
        'embedding': False,  # at resource level embedding is turned off, so works can't be embedded
        'schema' : works_schema
        # 'resource_methods': ['GET'], #we want this endpoint to be read only, so we overwrite the global setting
        # 'item_methods': ['GET']
    }

}