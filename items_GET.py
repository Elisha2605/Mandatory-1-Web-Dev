from bottle import get, view



################# ITEMS / GET  ###################
@get("/items")
@view("items")
def _():
    return