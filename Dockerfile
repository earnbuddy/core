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

# Copy the built Svelte project from the builder stage
COPY --from=builder /app/build /app/public

# Copy the FastAPI application code
COPY /server .

# Expose the port
EXPOSE 8000

# Command to run the FastAPI server
CMD ["sh", "-c", "alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 8000"]