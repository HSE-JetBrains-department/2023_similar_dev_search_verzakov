FROM python:3.8-slim-buster

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get -y install gcc mono-mcs && \
    rm -rf /var/lib/apt/lists/* \

WORKDIR /cmd

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3",  "cmd.py", "-p", "tests/repos/2022_similar_dev_search_kononov", "-p", "tests/repos/2022_similar_dev_search_petropavlovskiy"]
