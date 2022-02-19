from bottle import get, view
import data


################# USERS / GET ###################
@get("/users")
@view("users")
def _():
   
    return dict(users=data.USERS)