from vercel_python_wsgi import VercelWSGIApp
from django.core.wsgi import get_wsgi_application
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinematography_backend.settings')
application = get_wsgi_application()
app = VercelWSGIApp(application)
