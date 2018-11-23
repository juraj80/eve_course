from app import MyBasicAuth


people_schema = {
    # A dict defining the actual data structure being handled by the resource.
    # Enables data validation.
    'firstname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 30,
    },

    'lastname': {
        'type': 'string',
        'maxlength': 50,
        'required': True,
        'unique': True,  # doesn't apply for bulk inserts
    },

    'middle_name': {
        'dependencies': ['firstname', 'lastname', 'location.address']
        # the field itself is not required, but if you provide a middle name
        # you also must provide the first name and last name, otherwise the field
        # would be rejected
    },

    'born': {'type': 'datetime'},

    # This field is added by app.add_age(). We still need to add it
    # to the schema definition, or ti won't be returned to clients.
    #    'age' : {'readonly' : True},  # clients can't write or overwrite it
    'age': {
        'type': 'int',
        # Make sure clients don't try to write to it.
        'readonly': True,
        #'isodd': True,
        # 'coerce': int   # converts passed value to integer
    },
    # 'role' is a list, and can only contain values from 'allowed'.
    'role': {
        'type': 'list',
        'allowed': ['author', 'contributor', 'copy'],
        'default': ['author']
    },
    # 'location' is a subdocument (a dict).
    'location': {
        'type': 'dict',
        #       'required': True,
        'schema': {
            'address': {'type': 'string'},
            'city': {'type': 'string', 'required': True}
        },
    },
    # this only works when app.MyValidator is used, as it brings support
    # for validating a field of type 'email'.
    'email': {
        'type': 'email'
        #        'regex': r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    },
    # 'prop1': {
    #     'anyof_type': ['integer', 'float'],  # example of *of-rules typesaver
    #     'anyof': [{'min': 0, 'max': 10}, {'min': 100, 'max': 110}]
    #     # example of *of-rules from http://docs.python-cerberus.org/en/stable/validation-rules.html#of-rules
    #
    # }
}



people = {
    # A class with the authorization logic for the endpoint. If not provided
    # the eventual general purpose auth class will be used.
    'authentication': MyBasicAuth,
    # When False, this option disables HATEOAS for the resource.
    # Defaults to True
    'hateoas': False,
    # 'pagination' : True,
    # 'allowed_filters': ['lastname'],
    # 'sorting': True,
    # 'projection': True,
    # 'datasource' : {'projection':{'lastname':0}}, # every request sent
    'schema': people_schema  # the schema for the people endpoint is previously defined schema
},

