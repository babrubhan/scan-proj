FROM python:3.8.2
WORKDIR /code
COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

RUN printenv > /env.txt

EXPOSE 3500
heroku login
CMD [ "python", "app.py" ]