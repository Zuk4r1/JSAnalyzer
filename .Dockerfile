# docker pull andmyhacks/JSPaserHandler


FROM python:3

LABEL "Author"=" Zuk4r1"

RUN mkdir -p /var/www/JSPaserHandler
WORKDIR /var/www/JSPaserHandler

COPY . /var/www/JSPaserHandler/

RUN apt-get update
RUN apt-get install -y  git python-setuptools
RUN pip install --upgrade pip

RUN python setup.py install


ENTRYPOINT ["python", "handler.py"]