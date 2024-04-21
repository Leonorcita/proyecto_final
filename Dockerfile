FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN apt-get update

RUN apt-get install -y git

CMD ["python", "run.py"]
