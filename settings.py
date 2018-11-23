""" script to instruct API on how it should perform, to configure behavior of our API"""

from domain import DOMAIN


# X_DOMAINS = None # this tells our Eve instance that it should not accept the requests coming from web pages
# which are not in the same domains as the server, which is usually not the case

X_DOMAINS = '*'  # if you have public server, you want to accept incoming requests from anybody

X_DOMAINS_RE = ['^http://sub-\d{3}\.example\.com$']  # we only accepting requests from http://sub-\d  or  \.example\.com
# mongo connection string to local instance
# see http://docs.mongodb.com/manual/reference/connection-string/
MONGO_URI = 'mongodb://localhost:27017/eve_course'

# global methods allowed at the resource (collection) endpoint, to allow clients to write, edit or delete
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
# global methods allowed at the document (item) endpoint
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# IF_MATCH = False # if False, we need to add an if match header every single time we perform an edit operation on a document
# IF_MATCH = True
# ENFORCE_IF_MATCH = False # we let the client decide how the server should accept our edit request.
# ETAG = 'etag'
# DATE_CREATED = 'created'
# LAST_UPDATED = 'updated'

# EMBEDDING = False # is True by default on global level

# DATE_FORMAT = '%d %b %Y' # setting which allows us to change default rfc 1123 format for datetime string values

# QUERY_WHERE = 'find'
# QUERY_SORT = 'orderby'

# ALLOWED_FILTERS = ['*']  # to allow searching on all fields, by default
# ALLOWED_FILTERS = [] # to disable searching to  none fields
# ALLOWED_FILTERS = ['lastname'] # better to filter on endpoint level

# SORTING = False #to disable sorting on global level, by default is True globally

# MONGO_QUERY_BLACKLIST = ['$where','$regex'] # by default, to disable Javascript operators where and regex
# MONGO_QUERY_BLACKLIST = [] # to allow $where and $regex query operators

# PAGINATION = False
# QUERY_PAGE = 'section'
# MAX_QUERY_RESULT = 'max_results' # default settings is 25 documents per page
# PAGINATION_DEFAULT = 25
# PAGINATION_LIMIT = 50
# OPTIMIZE_PAGINATION_FOR_SPEED = True  # is disabled by default, on big collections can greatly improve performance but lacks of accuracy

# PROJECTION = False # to disable projections on all endpoints
# QUERY_PROJECTION = 'fields'  # to change to word for query projections
# HATEOAS = True
# LINKS = 'links'
# JSON = False
# JSON_SORT_KEYS = True
# JSON_REQUEST_CONTENT_TYPES = ['application/json', 'application/csp-report']


# Rate limiting
RATE_LIMIT_GET = (1, 60)  # 1 request every 60 seconds
RATE_LIMIT_POST = (1, 60)

## PATCH - to edit document
## PUT - to replace document
## DELETE - to delete document
