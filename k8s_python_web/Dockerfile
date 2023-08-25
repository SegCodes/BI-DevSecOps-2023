FROM python:3.8-alpine

COPY ./requirements.txt /app/requirements.txt
COPY ./view.py /app/view.py

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "view.py" ]