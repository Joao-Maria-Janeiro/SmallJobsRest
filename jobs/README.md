jobs/create


In the header:
- Key: Authorization
- Value: Bearer 4ff21d27977120cf76ee5379ab0f5dda32ff8fcf 

#### Input
```json
{		
    "title": "JobTitle",
    "description": "Small Job Description",
    "start_date" : "12-12-2012",
    "end_date" : "27-12-2013",
    "start_time" : "12:12",
    "end_time" : "18:18",
    "payment": 12.32,   
    "location": "local",
    "phone_number": "123456789"
}
```
jobs/all

#### Output
```json
[
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
    }
]

```
jobs/employee-accept-job
#### Input
```json
    "id": 7 //Job id
```
#### Output

This function has no output.




jobs/get-all-job-qeued-users
#### Input
```json
    "id": 7 //Job id
```

#### Output
```json
[
    {
        "id": 12,  <UserId>
        "userprofile": {
            "age": 18,
            "phone_number": "123456789",
            "description": "Small Job Description",
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
            ]
        }
        "username": "username1",
        "first_name": "FirstName",
        "last_name": "LastName",
        "email": "mail@gmail.com"
      
    }
]

```
