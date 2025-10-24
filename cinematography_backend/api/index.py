from vercel_python_wsgi import VercelWSGIHandler

from cinematography_backend.wsgi import application

handler = make_wsgi_handler(application)
