# Use the official Python image as a base image
FROM python:latest

# Set an environment variable to prevent Python from buffering outputs
ENV PYTHONUNBUFFERED 1

# Create a directory to store your application code
RUN mkdir /code

# Set the working directory to /code
WORKDIR /code

# Copy the local requirements.txt file to the /code/ directory
COPY requirements.txt /code/

# Install the Python dependencies
RUN pip install -r requirements.txt

# Expose port 8000 for the Django application
EXPOSE 8000

# Set environment variables for Django superuser creation
ENV DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME}
ENV DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL}
ENV DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD}
ENV DJANGO_SUPERUSER_FIRST_NAME=${DJANGO_SUPERUSER_FIRST_NAME}
ENV DJANGO_SUPERUSER_LAST_NAME=${DJANGO_SUPERUSER_LAST_NAME}

# Run the Django migrations, create a superuser, and start the server
CMD python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py createsuperuser --noinput --username=${DJANGO_SUPERUSER_USERNAME} 2>&1 || true && \
    python manage.py runserver 0.0.0.0:8000
