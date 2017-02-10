FROM ubuntu:latest
MAINTAINER Rajdeep Dua "dua_rajdeep@yahoo.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /server
WORKDIR /server
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["server.py"]
