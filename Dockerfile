FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apt update
RUN apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6
RUN apt-get install -y wget
#download and install chrome
ARG CHROME_VERSION="81.0.4044.113-1"

RUN wget --no-verbose -O /tmp/chrome.deb https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_${CHROME_VERSION}_amd64.deb \
  && apt install -y /tmp/chrome.deb \
  && rm /tmp/chrome.deb
RUN pip install -r requirements.txt

COPY . .
CMD python -m pytest --driver Chrome --driver-path ./selenium_driver/chromedriver_linux