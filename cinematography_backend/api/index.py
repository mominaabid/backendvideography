from vercel_python_wsgi import VercelWSGIHandler
from cinematography_backend.wsgi import application

handler = VercelWSGIHandler(application)
