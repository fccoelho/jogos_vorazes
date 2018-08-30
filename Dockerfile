FROM python:3

MAINTAINER danielilaro@hotmail.com

WORKDIR /raiz

ADD . /raiz

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y gnuplot

CMD ["python", "simulador.py"]
