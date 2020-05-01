# Telsa Credentials
a_tesla_email = '<email>'  # myTesla Account Username
a_tesla_password = '<password>'  # myTesla Account Password
a_tesla_car_idx = 0  # Index of the Car in myTesla Account in case of multiple Cars
a_allow_sleep = 1  # Allow Car to fall asleep / don't wake up if car is asleep on Scraper start
a_maximum_sleep = 1024  # Wake up every X seconds, if car is asleep

# Scraper API Config (you need that for using the android App)
a_enable_api = True
a_api_key = 'somerandomnumberwithenoughdigitsthatcantbeguessedeasily'
a_api_port = 8023
a_start_disabled = False  # Scrapper state on startup. This could
# be changed with the app if the
# a_enable_api is True
a_resolve_elevation = True  # Resolve Coordinates to Elevation. Will Autodownload Elevation data from https://dds.cr.usgs.gov

# Logging
a_logfile = 'apiscraper.log'                # APIScraper Logfile
#CRITICAL = 50
#FATAL = CRITICAL
#ERROR = 40
#WARNING = 30
#WARN = WARNING
#INFO = 20
#DEBUG = 10
#NOTSET = 0
a_loglevel = 20                             # Loglevel 10: DE

# Influx DB Credentials
a_influx_host = 'localhost'                 # Set this to influxdb_apiscraper in a Docker environment, otherwise: localhost
a_influx_port = 8086                        # InfluxDB Port
a_influx_user = 'tesla'                     # InfluxDB Username
a_influx_pass = '<influxdbpassword>'        # InfluxDB Password
a_influx_db = 'tesla'                       # InfluxDB Datebasename

a_dry_run = False  # Just for debugging purposes
