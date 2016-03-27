# Server Gunicorn config file

import multiprocessing

bind = '0.0.0.0:8081'
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'
spew = False
daemon = False
pidfile = None
umask = 0
user = None
group = None
errorlog = '-'
loglevel = 'info'
accesslog = '-'
proc_name = None
