from bottle import get, view
import data

################ HOME GET ####################
@get("/")
@view("index")
def _():
    return dict(tweets=data.TWEETS)