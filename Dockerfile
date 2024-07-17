# Standard Base Image
FROM python:3.8-slim


# Setting a work directory
WORKDIR /app


# Install netcat
RUN apt-get update && apt-get install -y netcat-openbsd


# Copying required files
COPY . /app


# Installing dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# Exposing port for Streamlit
EXPOSE 8501


# Copying and executing initialization scripts
COPY start.sh /start.sh
RUN chmod +x /start.sh


# Defining the PORT environment variable
ENV PORT 8501


# Default command
CMD ["/start.sh"]