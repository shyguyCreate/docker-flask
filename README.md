# Flask and NGINX in Docker

Docker container with Flask application powered by Waitress WSGI server to display a basic html website hosted on port 8080. And NGINX container to port forward HTTP calls to the html contents in the Flask container.

It is advice to run the containers with **docker compose** instead of indivually to automatically link containers with docker shared network[^1]. To inspect this project, refer to [app/Dockerfile](./app/Dockerfile) and [nginx/Dockerfile](./nginx/Dockerfile) for more detail.

[^1]: If NGINX container is run individually, it will fail to start if Flask container is not named `flask-app` and containers are not link in a shared network.
