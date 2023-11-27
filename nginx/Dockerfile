# syntax=docker/dockerfile:1

FROM nginx:1.25-bookworm

EXPOSE 80

# Copy all files to /app directory
WORKDIR /nginx
COPY . .

COPY nginx.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]
