from bottle import run, get, view, static_file, error


#######  STATIC-FILES  #######
@get("/app.css")
def _():
    return static_file("app.css", root="./views/css")

@get('/static/<filename>')
def _(filename):
    return static_file(filename, root="./static")

################  ERROR 404  ####################
@error(404)
@view("404")
def _(error):
    print(error)
    return


#######  GET  #######
import home_GET
import users_GET
import items_GET
import signup_GET
import login_GET
import admin_GET
import logout_GET

import update_tweet_GET

#######  POST  #######
import signup_POST
import login_POST
import admin_POST



#######  DELETE  #######
import delete_user_POST







run(server="paste", host="localhost", port=8080, reloader=True, debug=True)