from celery import Celery

from util.celery.builder import CeleryBuilder
from util.discover.module_discover import discover_python_modules


# This will be not work well. To be Fix later.
# modules have to be with methods.
celery: Celery = CeleryBuilder(modules=discover_python_modules()).build()
