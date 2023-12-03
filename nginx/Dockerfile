# syntax=docker/dockerfile:1

FROM nginx:1.25-bookworm

EXPOSE 80

# Set default configuration for NGINX
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Disable nginx user in config because container will run as non-root
RUN sed -i 's/user\s*nginx;/#user  nginx;/g' /etc/nginx/nginx.conf

# Change ownership of nginx dependency directories and files
RUN chown -R nginx:nginx /var/cache/nginx \
    && touch /var/run/nginx.pid && chown -R nginx:nginx /var/run/nginx.pid

# Run container with nginx user 
USER nginx

CMD ["nginx", "-g", "daemon off;"]
