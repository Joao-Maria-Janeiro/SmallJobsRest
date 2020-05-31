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
#### Input


urls/my-created-jobs
#### Input
