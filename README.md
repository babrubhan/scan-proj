# scan-proj
A REST API based resource management application with JWT based authorization and authentication privileges 

GitHub - https://github.com/babrubhan/scan-proj <br />
Heroku - https://scan-proj.herokuapp.com/ <br />

#### Run in container based envirionment:
```
  - Run docker-compose up -d
```  
  
#### Run in local environment:
```
  - export ENV_FILE_LOCATION=./.env
  - export ENV_FILE_LOCATION=./.env.test
  - pip install requirements.txt
  - python app.py
``` 
  
#### Authentication details for testing:
```
POST https://scan-proj.herokuapp.com/api/v1/auth
{
"email":"myfakeemail@gmail.com",
"password":"myfakepassword"
}
```
  
#### API Endpoints:
```
GET https://scan-proj.herokuapp.com/api/v1/perons
GET https://scan-proj.herokuapp.com/api/v1/perons/<id>

POST https://scan-proj.herokuapp.com/api/v1/persons
{
"name":"babru"
"resources":["R!", "R2", "R3"]
"limit":10
}

PUT https://scan-proj.herokuapp.com/api/v1/person/<id>
DELETE https://scan-proj.herokuapp.com/api/v1/person/<id>
PUT https://scan-proj.herokuapp.com/api/v1/person/<id>
```


###### NOTE: replace the APIs URL with http://127.0.0.1:3500 in case of local run
