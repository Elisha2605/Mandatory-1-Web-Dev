from bottle import get, view, request, response, redirect
import data
import jwt

####################  Admin / GET  ######################
@get("/admin")
@view("admin")
def _():
    user_session_jwt = request.get_cookie("jwt")

    if user_session_jwt not in data.SESSIONS:
        return redirect("/login")

    for session in data.SESSIONS:
        if session == user_session_jwt:
            user = jwt.decode(session, "secret", algorithms=["HS256"])
            
    return dict(tweets=data.TWEETS)

####################  Admin update / GET  ######################
@get("/admin-create")
@view("create")
def _():
    return


####################  Admin update / GET  ######################
@get("/admin-update")
@view("update")
def _():
    tweet_id = request.params.get("tweet_id")
    for tweet in data.TWEETS:
        if tweet["id"] == tweet_id:
            id = tweet["id"]
            title = tweet["title"]
            description = tweet["description"]

            return dict(id=id, title=title, description=description)