FROM python:3.7.0

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY dashomer.py /usr/src/app/
COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt
EXPOSE 8988
CMD ["python", "dashomer.py"]

