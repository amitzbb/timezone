FROM python:slim-buster
COPY ./requirements.txt /requirements.txt
WORKDIR /
RUN pip install -r requirements.txt
COPY . /
ENV port=6500
EXPOSE $port
CMD ["python3","app.py"]