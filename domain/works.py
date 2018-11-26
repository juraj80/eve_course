works_schema = {
    'title': {
        'type': 'string',
        'required': True,
    },
    'description': {
        'type': 'string',
    },
    'owner': {
        'type': 'objectid',
        'required': True,
        # referential integrity constraint: value must exist in the
        # 'people' collection. Since we aren't declaring a 'field' key,
        # will default to 'people._id' (or, more precisely, to whatever
        # ID_FIELD value is).
        'data_relation': {
            'resource': 'people',
            # make the owner embeddable with  ?embedded={"owner":1}
            # 'embeddable': True  # it will be ignored, because of embedding at resource level is turned off
        },
    },
}

works = {
    # 'embedding': False,  # at resource level embedding is turned off, so works can't be embedded
    'schema': works_schema
    # 'resource_methods': ['GET'], #we want this endpoint to be read only, so we overwrite the global setting
    # 'item_methods': ['GET']
}
