from flask import Flask, request, render_template , redirect, url_for
import wikipedia

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route("/pick_search", methods=['POST'])
def pick_search():
    try:
        text = request.form['search']
        form_text = wikipedia.summary(text)
    except Exception as e:
        error = e
        sorry_text = "This WikiPage does not exists, Search for something else."
    return render_template('content.html', form_text=form_text)

if __name__ == "__main__":
    app.debug = True
    app.run(use_reloader=True)
    app.run(debug = True)