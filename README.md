# djangoProjectV1
ToDo Django App
TODO server app with Python, Django, and PostgreSQL. The primary interface is
a REST API. 

Also provided an admin dashboard using Django’s Admin Site system.

Configured the app to run on a Gunicorn WSGI server, behind an NGINX instance acting as
a reverse-proxy. Deploy all components — Django, Postgres, Gunicorn, NGINX — as
Docker containers managed by docker-compose.

To run the server, open terminal in the root folder and type

docker-compose -f docker-compose.prod.yml up --build
