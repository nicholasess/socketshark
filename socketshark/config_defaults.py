# Default settings that can be overridden.

# Which WebSocket backend to use. Currently only "websockets" is supported.
BACKEND = 'websockets'

# Logging config
LOG = {
    'level': 'INFO',
    'format': '%(message)s'
}

# Host and port to bind WebSockets.
WS_HOST = '127.0.0.1'
WS_PORT = '9000'

WS_PING = {
    # How often to ping WebSocket connections in seconds (None to not ping).
    'interval': 15,

    # Seconds after which we disconnect clients with no ping response.
    'timeout': 15,
}

# HTTP options when querying services.
HTTP = {
    # Optional path to custom CA file.
    'ssl_cafile': None,
    'timeout': 15,
    'tries': 3,
    'wait': 3,
}

# Redis options
REDIS = {
    'host': 'localhost',
    'port': 6379,
    'channel_prefix': '',
}

# Authentication
AUTHENTICATION = {}

# List of services
SERVICES = {}