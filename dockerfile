# Base image
FROM python:3.11-slim

# Set work directory inside container
WORKDIR /app

# Copy requirements (we'll make one)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app
COPY . .

# Expose the port your app runs on
EXPOSE 5001

# Command to run the app
CMD ["python", "app.py"]
