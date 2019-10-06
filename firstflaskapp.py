from flask import Flask

app = Flask(__name__)  # creating the Flask class object



def about():
    return "this is about page";

app.add_url_rule("/about","about",about)
if __name__ == '__main__':
    app.run(debug=True)
