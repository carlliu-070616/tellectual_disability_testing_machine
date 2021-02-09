from main import app,bs
from flask import render_template


@app.errorhandler(404)
def not_found(error):
   return render_template('404.html',bs=bs)
   
   
@app.errorhandler(500)
def server_error(error):
   return render_template('500.html',bs=bs)