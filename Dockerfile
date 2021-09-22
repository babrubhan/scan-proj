FROM python:3.7
ENV ENV_FILE_LOCATION ./.env
ENV ENV_FILE_LOCATION ./.env.test
ADD . /app
WORKDIR /app
EXPOSE 3500
RUN pip install -r requirements.txt
