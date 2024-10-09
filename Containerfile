FROM docker.io/library/python:3.12.6
# FROM docker.io/library/python:3.12.7

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

LABEL org.opencontainers.image.title="cloud-native-demo"

COPY ./app ./app

RUN rm requirements.txt

CMD [ "python", "-m", "app.main" ]
