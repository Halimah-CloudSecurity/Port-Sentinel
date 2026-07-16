DEFAULT_TIMEOUT = 3

MAX_WORKERS = 100


# Default port range
START_PORT = 1
END_PORT = 1024


# Validation limits
MIN_PORT = 1
MAX_PORT = 65535

MIN_TIMEOUT = 1
MAX_TIMEOUT = 30

MIN_WORKERS = 1
MAX_ALLOWED_WORKERS = 1000


# Common HTTP ports
HTTP_PORTS = [

    80,
    81,
    8000,
    8080,
    8888,
    9000

]


# Common HTTPS ports
HTTPS_PORTS = [

    443,
    444,
    8443,
    9443

]

# Enable TLS certificate analysis
ENABLE_TLS_ANALYSIS = True