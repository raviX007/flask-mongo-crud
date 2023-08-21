# FROM python:3.9-slim-buster
# WORKDIR /app
# COPY ./requirements.txt /app
# RUN pip3 install -r requirements.txt
# COPY app.py .
# EXPOSE 27017
# EXPOSE 5000
# ENV FLASK_APP=app.py
# CMD ["--port 27017", "--smallfiles"]
# CMD ["flask", "run", "--host", "0.0.0.0","5000"]
FROM python:3.9-slim-buster

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip3 install -r requirements.txt

COPY app.py .

# Expose port 5000 for Flask app
EXPOSE 5000

# Set the Flask app environment variable
ENV FLASK_APP=app.py

# Run the Flask app with host 0.0.0.0 and port 5000
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
