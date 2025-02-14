import os
from celery import Celery

# Set default settings for Celery to use Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

celery_app = Celery('myproject')

# Load Celery config from Django settings
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks from installed apps
celery_app.autodiscover_tasks()
