FROM python:3.9

EXPOSE 5000

RUN mkdir /home/app
WORKDIR /home/app

COPY requirements.txt /home/app/requirements.txt
RUN apt-get update && apt-get install -y \
  git \
  zlib1g-dev \
  unixodbc \
  unixodbc-dev \
  freetds-dev \
  freetds-bin \
  tdsodbc \
  libicu-dev\
  wget
# Alterando time zone
RUN cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime

# Instalação de bibliotecas
RUN pip install -r requirements.txt

COPY . /app
CMD python  app.py