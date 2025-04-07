# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app.py .

# Expose the port
EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=5 \
CMD curl -f http://localhost:5000/ || exit 1


# Run the application
CMD ["python", "app.py"]
