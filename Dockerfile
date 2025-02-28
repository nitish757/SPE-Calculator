# Use Python 3.8 base image
FROM python:3.8

# Set the working directory
WORKDIR /app

# Copy the calculator script and test script into the container
COPY calculator.py /app/calculator.py
COPY test.py /app/test.py

# Ensure scripts have proper UNIX line endings
RUN python3 -m pip install --upgrade pip

# Run unit tests to validate functionality inside the container
RUN python3 -m unittest /app/test.py

# Set the default command to run the calculator script
CMD ["python3", "/app/calculator.py"]