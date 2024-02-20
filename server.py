from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['Name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        quantity = request.form['quantity']

        if not (name and email and phone and address and quantity):
            return "All fields are required"
        #Data to be fetched and stored
        registration_data = {
            'name': name,
            'email': email,
            'phone': phone,
            'address': address,
            'quantity': quantity
        }

        save_registration(registration_data)
        
        #email msg 
        
        summary_message = f"""We are delighted to inform you that your registration for food donation at Zero Hunger was successful!
        {name} Your commitment to contributing to our cause is truly appreciated, and we are thrilled to have you join our efforts in fighting hunger and making a positive impact in our community\n"""
        summary_message += f"Details:\n"
        summary_message += f"Email: {email}\n"
        summary_message += f"Phone: {phone}\n"
        summary_message += f"Address: {address}\n"
        summary_message += f"Quantity: {quantity} kg\n"

        send_email(email, summary_message)

        return summary_message
    
def save_registration(data):
    try:
        with open('data/registrations.json', 'r') as file:      #Form Details are being stored in a json file
            registrations = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        registrations = []

    registrations.append(data)

    with open('data/registrations.json', 'w') as file:
        json.dump(registrations, file, indent=4)

def send_email(receiver_email, message):
    sender_email = "zhunger7@gmail.com" #leave this things like this 
    password = "kljm aqow swdu hssj" 

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Registration Success"

    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)  #smpt gmail server and pass key
    server.starttls()
    server.login(sender_email, password) 
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()

#routing html pages with python flask server
@app.route('/food_donation')
def food_donation():
    return render_template('fd.html') 

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/hotel_info')
def hotel_info():
    return render_template('hotel.html')

@app.route('/area')
def area():
    return render_template('area.html')

@app.route('/location')
def location():
    return render_template('location.html')

if __name__ == '__main__':
    app.run(debug=True)
