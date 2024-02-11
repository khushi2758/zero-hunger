from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        food_type = request.form['foodType']
        quantity = request.form['quantity']

        if not (name and email and phone and address and quantity):
            return 'All fields are required'

        registration_data = {
            'name': name,
            'email': email,
            'phone': phone,
            'address': address,
            'food_type': food_type,
            'quantity': quantity
        }

        try:
            with open('registrations.json', 'r') as file:
                registrations = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            registrations = []

        registrations.append(registration_data)

        with open('registrations.json', 'w') as file:
            json.dump(registrations, file, indent=4)

        return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/food_donation')
def food_donation():
    return render_template('fd.html')

if __name__ == '__main__':
    app.run(debug=True)
