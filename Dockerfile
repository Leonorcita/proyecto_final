FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN apt-get update \
    && apt-get install -y postgresql-client

RUN apt-get install -y git

RUN pip install -r requirements.txt

CMD ["sh", "start_dev_env.sh"]
