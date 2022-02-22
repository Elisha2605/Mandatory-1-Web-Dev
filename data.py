import time


######################## REGEX ###############################
REGEX_EMAIL = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'

######################## COOKIES ###############################
SESSIONS = []
COOKIE_SECRET = "This is my secret"

######################## DICTS ###############################
USERS = [
    {
        "id": "9283498327492374937498", 
        "firstname": "Aïcha", 
        "lastname": "Haïdara", 
        "email": "a@a.com", 
        "password": "123",
    },
    {
        "id": "4923849082034832048092", 
        "firstname": "Elisha", 
        "lastname": "Ngoma", 
        "email": "elisha_ngoma@yahoo.fr", 
        "password": "123"
    }
]
TWEETS = [
    {
        "id": "c10118bf-60dd-4099-bca4-8c73e0489234", 
        "title": "Aïcha", 
        "description": "Haïdara",
        "time": str(time.time()) 
    },
    {
        "id": "56f41f60-7614-4e35-85a8-73dbff779e4a", 
        "title": "Elisha", 
        "description": "Haïdara",
        "time": str(time.time()) 
    }
]
