FROM python:3.12-slim
ENV  PYTHONUNBUFFERED=1
ENV  PYTHONDONTWRITEBYTECODE=1

WORKDIR /usr/src/app

COPY requirements.txt ./

COPY ./project/ .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]