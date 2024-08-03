# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/requirements.txt

# Install the Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the entire project into the container
COPY . /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings

# Run the collectstatic command
RUN python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Run the Django server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]
