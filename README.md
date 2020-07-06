# ToDo Django App
TODO server app with Python, Django, and PostgreSQL. The primary interface is
a REST API. 

Also provided an admin dashboard using Django’s Admin Site system.

Configured the app to run on a Gunicorn WSGI server, behind an NGINX instance acting as
a reverse-proxy. Deploy all components — Django, Postgres, Gunicorn, NGINX — as
Docker containers managed by docker-compose.

To run the server, open terminal in the root folder and type

docker-compose -f docker-compose.prod.yml up --build

# Testing
To test the API's, cd to testing_scripts/api_testing_v2.py and run the following command.

AUTH=authKey python api_testing_v2.py

Replace auth key with any of the auth keys

authKey: 23d638bb9bb16d60cf3a8410cf8101a4ad3a4282 
 
