FROM python:3.9
COPY . /usr/src/app
ADD . /todo
WORKDIR /todo
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
