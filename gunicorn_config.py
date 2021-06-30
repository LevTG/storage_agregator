command = '/home/backy/venv/bin/gunicorn'
pythonpath = '/home/backy/storage_aggregator'
bind = '159.89.186.245:8080'
workers = 3
user = 'backy'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=storage_aggregator.settings'
