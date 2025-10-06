# Stage 1: Build
FROM python:3.11-slim-buster AS build

# Set the working directory in the container
WORKDIR /app

# Copy requirements file and install Python dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy your Flask application code
COPY . .

# Stage 2: Production
FROM python:3.11-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files from the builder stage
COPY --from=build /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Copy your Flask application code
COPY . .

# Variables de entorno por defecto
ENV FLASK_APP=main.py
ENV FLASK_ENV=production
ENV GUNICORN_BIND=0.0.0.0:8080


# Expose the port your Flask app listens on (e.g., 5000)
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD node -e "require('http').get('http://localhost:8080/health', (r) => {process.exit(r.statusCode === 200 ? 0 : 1)})"

# Run the app with Gunicorn, a production-grade WSGI server
# CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:app"]
CMD [ "python3", "main.py"]
