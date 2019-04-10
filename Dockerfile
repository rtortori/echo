FROM python:3.7-alpine

# Set the working directory to /
WORKDIR /

# Copy required configuration files
ADD . /

# Optionally define proxy environment
ARG http_proxy=http://proxy-wsa.esl.cisco.com:80
ARG https_proxy=http://proxy-wsa.esl.cisco.com:80

# Install requirements
RUN pip install -r requirements.txt

# Run it
CMD python echo.py

# Expose port 5000
EXPOSE 5000/tcp
