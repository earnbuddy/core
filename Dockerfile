# Stage 1: Build the Svelte project
FROM node:20 AS builder

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY app/package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY app/. .

# Build the Svelte project
RUN npm run build

# Stage 2: Serve the built Svelte project with FastAPI
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY server/requirements.txt .

# Install FastAPI and Uvicorn
RUN pip install -r requirements.txt

# Copy the Django application code
COPY /server .

# Copy the built Svelte project from the builder stage
COPY --from=builder /app/build /app/templates
COPY --from=builder /app/assets /app/static

RUN sed -i 's|"/|"/static/|g' /app/templates/index.html

# Expose the port
EXPOSE 8000

# Command to run the FastAPI server
CMD ["sh", "-c", "python manage.py migrate &&  gunicorn wsgi --bind 0.0.0.0:8000 --workers=1"]