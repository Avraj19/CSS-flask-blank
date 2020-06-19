# First import flack
from flask import Flask, render_template

# To use render_template you must have a file call templates on the same level as run.py

# This file (templates) stores the HTML, Python and CSS code.

# To distinguish file and will later be used to run.
app = Flask(__name__)


# To map the route
# Anything in the brackets will be end of the url
@app.route("/")
def home():
    # To use render_template
    # Have a file in templates
    # The name of the file goes in brackets
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')

# This runs the app (if in main)
# (debug=True) is there for devs making change
# So when a change is made is happen immediately
# So you don't have to constantly restart your server
if __name__ == "__main__":
    app.run(debug=True)
