from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/<string:page_name>')
def my_home(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open("database.txt", mode="a") as db:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        db.write(f"\n{email}, {subject}, {message}")


def write_to_csv(data):
    with open("database.csv", mode="a", newline="") as db2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_file = csv.writer(db2, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow([email, subject, message])

@app.route('/submit_form', methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            print(data)
            write_to_csv(data)
            return redirect("/thankyou.html")
        except:
            return "Did not save to database!"
    else:
        return "Something is wrong!"
