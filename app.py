from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static')

@app.route("/", methods=['GET', 'POST'])
def Home(name=None):
    return render_template('home.html', name = 'home')

# if __name__=="__main__":
#     app.run()

# debug mode running on 5050 port
if __name__=="__main__":
    app.run(host="localhost", debug=True, port=5050)
