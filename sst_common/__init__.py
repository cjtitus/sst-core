import os
from pkg_resources import get_distribution, DistributionNotFound
try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
   # package is not installed
   pass

STATION_ENV = "SST_STATION"

station_specified = STATION_ENV in os.environ
os.environ.setdefault(STATION_ENV, "sst_sim")

STATION_NAME = os.environ[STATION_ENV].lower()

