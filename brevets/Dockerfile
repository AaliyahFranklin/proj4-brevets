FROM python:3
MAINTAINER Aaliyah Franklin "aaliyahf@uoregon.edu"
RUN apt-get update -y
RUN apt-get install -y python-dev-is-python3
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["flask_brevets.py"]
