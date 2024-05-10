# Base image: Ubuntu
FROM ubuntu:latest

# Update package lists
RUN apt-get update

# Install Python 3 and pip
RUN apt-get install -y python3 python3-pip

# Verify Python installation
RUN python3 --version

# Set the working directory in the container
WORKDIR /app

# Copy your application code to the container
COPY . /app

# Install Python dependencies (if any)
RUN pip3 install -r requirements.txt

RUN pip3 install ibm_watsonx_ai

# Set the default command to execute when the container starts
CMD ["python3", "main.py"]