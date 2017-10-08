import os

"""

# mongo online db(MLAB) credentials
MONGO_HOST = os.environ.get('MONGO_HOST', '')
MONGO_PORT = os. environ.get('MONGO_PORT', '')
MONGO_USERNAME = os.environ.get('MONGO_USERNAME', '')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', '')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME', '')

"""

# mongo local db credentials
MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = os. environ.get('MONGO_PORT', 27017)
MONGO_USERNAME = os.environ.get('MONGO_USERNAME', 'admin')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', '123')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'flask_angular')
MONGO_AUTH_SOURCE = os.environ.get('MONGO_AUTH_SOURCE', 'admin')


RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

CACHE_CONTROL = 'max-age=20'
CACHE_EXPIRES = 20

URL_PREFIX = "api"

machine = {
    'item_title': 'machine',

    'schema': {
        'username': {
            'type': 'string'
        },

        'ip': {
            'type': 'string'
        },

        'device': {
            'type': 'string'
        },

        'password': {
            'type': 'string'
        },

        'port': {
            'type': 'string'
        }
    }

}


DOMAIN = {
    'machine': machine
}


if __name__ == '__main__':
    print('Current settings are')
    print ('MONGO_HOST: %s' % MONGO_HOST)
