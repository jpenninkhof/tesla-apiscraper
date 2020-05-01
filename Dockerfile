FROM python:3

ADD apiscraper.py /
ADD teslajson.py /
ADD apiconfig.py /
ADD config.py /
ADD srtmread.py /

RUN git clone https://github.com/tkrajina/srtm.py
WORKDIR srtm.py
RUN python3 ./setup.py install
WORKDIR /

RUN pip install influxdb

EXPOSE 8023
CMD [ "python", "./apiscraper.py" ]