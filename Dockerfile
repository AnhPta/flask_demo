FROM python:3.4-alpine
ADD . /code
WORKDIR /code

RUN pip install -r requirements.txt
#RUN apt install -y python-psycopg2

CMD ["python", "run.py"]

#FROM python:2-alpine
#
#WORKDIR /usr/src/app
#
#COPY requirements.txt ./
##RUN pip install --no-cache-dir -r requirements.txt#

#COPY . .

#CMD [ "python", "./app.py" ]