from bottle import get, view, request, redirect
import data



####################  Upadte-tweet / GET  ######################
@get("/update-tweet/<tweet_id>")
@view("update")
def _(tweet_id):

    tweet_id = request.forms.get("user_id")
    title = request.forms.get("title")
    description = request.forms.get("description")

    for tweet in data.TWEETS:
        if tweet["id"] == tweet_id:
            return redirect(f"/update?title={title}&description={description}")
        else:
            return redirect(f"/admin?error={tweet_id}")
    return 