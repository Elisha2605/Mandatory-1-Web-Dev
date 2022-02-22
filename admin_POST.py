from turtle import title
from bottle import post, request, redirect, put
import uuid
import time
import data


#####################  admin / DELETE  ######################
@post("/admin-delete")
def _():
    tweet_id = request.forms.get("tweet_id")
    for index, tweet in enumerate(data.TWEETS):
        if tweet["id"] == tweet_id:
            data.TWEETS.pop(index)
            return redirect("/admin")
    return redirect("/admin")

#####################  admin / UPDATE  ######################
@post("/admin-update")
def _():
    id = request.forms.get("id")
    new_title = request.forms.get("title")
    new_description = request.forms.get("description")
    for index, tweet in enumerate(data.TWEETS):

        if tweet['id'] == id:
            data.TWEETS[index]["title"] = new_title
            data.TWEETS[index]["description"] = new_description
            data.TWEETS[index]["time"] = int(time.time())
    
    return redirect("/admin")

####################  admin / POST  ######################
@post("/admin-create")
def _():
    
    tweet_id = str(uuid.uuid4())
    title = request.forms.get("title")
    description = request.forms.get("description")

    new_tweet = {
        "id": tweet_id,
        "title": title, 
        "description": description,
        "time": str(time.time())
    }

    data.TWEETS.append(new_tweet)

    return redirect("/admin")

    