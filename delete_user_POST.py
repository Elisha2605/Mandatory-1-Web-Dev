
from bottle import post, redirect, request
import uuid
import data


################# DELETE USERS ###################
@post("/delete-user")
def _():
    user_id = request.forms.get("user_id")
    for index, user in enumerate(data.USERS):
        if user["id"] == user_id:
            data.USERS.pop(index)
            return redirect("/users")
    return redirect("/users")