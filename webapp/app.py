from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results', methods=["POST"])
def results():
    text_list = request.form["text_list"].split()
    pat = request.form["pat"]
    matches_list = [re.findall(pat, text) for text in text_list]
    return render_template('index.html', matches_list=matches_list, regex_pattern=pat, text_list=text_list)

@app.route('/mailvalid', methods=["POST"])
def valid():
    email = request.form["email"]
    # Regular expression pattern to validate email format
    email_pattern = r'\w+@\w+\.\w+'
    if re.match(email_pattern, email):
        result = "Valid"
    else:
        result = "Invalid"
    return render_template('mail_valid.html', email=email, result=result)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
