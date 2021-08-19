FROM python:3.8

RUN mkdir -p /usr/src/app/
COPY requirements.txt /usr/src/app/requirements.txt
WORKDIR /usr/src/app/
RUN python -m pip install -r requirements.txt
COPY . /usr/src/app/

CMD ["python", "./manage.py", "runserver"]
