FROM python:3.9

ENV MYSQL_HOST=mariadb.app.svc.cluster.local
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=aaaaaa
ENV MYSQL_DB=appDb

WORKDIR /app

COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app
 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]