FROM python:3.10

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY requirements.txt requirements.txt
# Instalar dependencias del sistema
RUN python -m pip install --no-cache-dir -r requirements.txt
RUN python -m pip install gunicorn

COPY . .

COPY ./entrypoint.sh /
ENTRYPOINT [ "sh", "/entrypoint.sh" ]
