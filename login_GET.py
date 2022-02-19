from bottle import get, view
import data


#################  LOGIN / GET  ###################
@get("/login")
@view("login")
def _():
    return