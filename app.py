from redis import Redis
from eve import Eve

# separation of concerns!
from auth import MyBasicAuth
from validation import MyValidator
from callbacks import add_age, inject_signature

# app = Eve(validator=MyValidator,
#           redis=Redis(), auth=MyBasicAuth)  # we didn't set the host for the redis instance, it will connect to local host
app = Eve()

# custom route / if we had more than one custom endpoint we should move it to the separate file
@app.route('/hello')
def hello():
    """ A Eve instance is still a 100% Flask application """
    return 'Hello, world!'


# attach a callback function to GET requests.
app.on_fetched_item += inject_signature  # a new field is returned to the client, but since we injected it right after
# reading it from the db, it is not in the database

# attach a callback function to POST requests.
app.on_insert += add_age  # age will be permanent in our db
