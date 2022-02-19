from bottle import post, request, redirect, put
import uuid
import time
import data



####################  admin / POST  ######################
@post("/admin")
def _():
    
    user_id = str(uuid.uuid4())
    title = request.forms.get("title")
    description = request.forms.get("description")

    new_tweet = {
        "id": user_id,
        "title": title, 
        "description": description,
        "time": str(time.time())
    }

    data.TWEETS.append(new_tweet)

    return redirect("/admin")

#####################  admin / DELETE  ######################
@post("/admin-delete")
def _():
    user_id = request.forms.get("user_id")
    for index, tweet in enumerate(data.TWEETS):
        if tweet["id"] == user_id:
            data.TWEETS.pop(index)
            return redirect("/admin")
    return redirect("/admin")

#####################  admin / UPDATE  ######################
#(to do)