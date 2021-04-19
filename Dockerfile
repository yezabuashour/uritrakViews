FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip build-essential
COPY . /app
WORKDIR /app
RUN pip3 install flask
ENTRYPOINT ["python3"]
EXPOSE 5000
CMD ["app.py"]