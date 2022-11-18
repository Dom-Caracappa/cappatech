from flask import Flask, render_template




# Flask Instance
app = Flask(__name__, static_url_path='/static') 



@app.route("/", methods=['GET', 'POST'])
def Home(name=None):
    return render_template('base.html')

 
## Error Pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500     






    




# debug mode running on 5050 port
if __name__=="__main__":
    app.run(host="localhost", debug=True, port=5050)
