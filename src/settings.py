#
# Gunicorn config file
#
wsgi_app = "src.main:app"

# Server Mechanics
# ========================================
# current directory
chdir = "./src/"

# daemon mode
daemon = False

# enviroment variables
# raw_env = ["ENV_TYPE=dev", "HOGEHOGE_KEY=xxxxxxxxxxxxxxxxxxxxxxxxx"]

# Server Socket
# ========================================
bind = "0.0.0.0:8000"

# Worker Processes
# ========================================
# workers = 2

#  Logging
# ========================================
# access log
# accesslog = '/work/python/gunic/gu/logs/access.log'
# access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
# gunicorn log
# errorlog = '-'
# loglevel = 'info'
