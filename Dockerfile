FROM python:3-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add -u zlib-dev jpeg-dev gcc musl-dev


RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .build-deps

CMD ["python3", "app.py"]