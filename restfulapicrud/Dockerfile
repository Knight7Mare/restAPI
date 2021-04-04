FROM python:3.7.0

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY manage.py /usr/src/app/
COPY requests.log /usr/src/app/
COPY middleware.py /usr/src/app/
COPY dev.py /usr/src/app/
COPY requirements.txt /usr/src/app/
COPY employeeapi /usr/src/app/employeeapi
COPY restfulapicrud /usr/src/app/restfulapicrud
RUN pip install -r requirements.txt
EXPOSE 8000

