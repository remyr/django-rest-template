from .base import *
import os


if os.environ.get("ENV_NAME") == 'production':
    from .production import *
else:
    from .local import *
