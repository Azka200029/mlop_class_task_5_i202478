# Use a lightweight web server image
FROM nginx:alpine

# Copy static files to nginx directory
COPY index.html /usr/share/nginx/html

# Expose port 80
EXPOSE 82

# Command to run the web server
CMD ["nginx", "-g", "daemon off;"]
