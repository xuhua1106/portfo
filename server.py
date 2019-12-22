from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


def write_to_file(data):
    # with open('data.txt', mode='a') as database:
    #     email = data['email']
    #     subject = data['subject']
    #     message = data['message']
    #     file = database.write(f'\n{email},{subject},{message}')
    with open('database.csv', 'a', newline='') as csvfile:
        email = data['email']
        subject = data['subject']
        message = data['message']
        fieldnames = ['email', 'subject', 'message']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # writer.writeheader()
        writer.writerow({'email': email, 'subject': subject, 'message': message})


@app.route('/')
def my_home():
    return render_template('./index.html')
    # files has to be in 'tempaltes' folder


@app.route('/<page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            return redirect('thankyou.html')
        except:
            return 'something went wrong, did not save the info'
    else:
        return 'Something went wrong. Try again!'
