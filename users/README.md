### URL PATTERNS

  /users/signup

##### Input

```json
{		
	"email":"mail@gmail.com",
	"username":"username",
	"password":"password",
	"first_name": "FirstName", 
	"last_name" : "LastName",
	"age": 18,
	"phone_number": 123456789,
	"description": "Small Job Description",
	"skills": [       
		"FirstSkill",
		"SecondSkill",
		"ThrirdSkill"
	]
}
```
In the header:
- Key: Authorization
- Value: Bearer 4ff21d27977120cf76ee5379ab0f5dda32ff8fcf 

  users/login
  #### Input
  
  ```json
    "email":"password"
    "password":"password"
  ```
  
  #### Output
  
  ```json
  {
    "last_name": "LastName",
    "description": "Small Job Description",
    "first_name": "FirstName",
    "skills": [
        {
            "id": 4,
            "name": "firstskill"
        },
        {
            "id": 5,
            "name": "secondskill"
        },
        {
            "id": 6,
            "name": "thrirdskill"
        }
    ],
    "age": 18,
    "phone_number": "123456789",
    "email": "password",
    "token": "c0c20ea64b7c0aca69891ee5eced6f1e2b34df8e"
}
  
  ```
urls/get-previous-jobs
In the header:
- Key: Authorization
- Value: Bearer 4ff21d27977120cf76ee5379ab0f5dda32ff8fcf 





urls/my-created-jobs
#### Input
```json
[
    {
        "id": 7,
        "title": "JobTitle",
        "description": "Small Job Description",
        "start_date": "2012-12-12",
        "end_date": "2013-12-27",
        "payment": 12.32,
        "start_time": "12:12:00",
        "end_time": "18:18:00",
        "location": "local",
        "phone_number": "123456789",
        "employer": "FirstName"
    },
    {
        "id": 8,
        "title": "JobTitle1",
        "description": "Small Job Description",
        "start_date": "2012-12-12",
        "end_date": "2013-12-27",
        "payment": 12.32,
        "start_time": "12:12:00",
        "end_time": "18:18:00",
        "location": "local",
        "phone_number": "123456789",
        "employer": "FirstName"
    },
    {
        "id": 9,
        "title": "JobTitle2",
        "description": "Small Job Description",
        "start_date": "2012-12-12",
        "end_date": "2013-12-27",
        "payment": 12.32,
        "start_time": "12:12:00",
        "end_time": "18:18:00",
        "location": "local",
        "phone_number": "123456789",
        "employer": "FirstName"
    }
]

```
