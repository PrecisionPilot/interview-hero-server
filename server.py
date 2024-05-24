from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_mail import Mail
from flask_mail import Message
import sys
from key import mail_password

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'seanwaterloo2997@gmail.com'
# TODO: securely store password
app.config['MAIL_PASSWORD'] = mail_password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
CORS(app)

@app.route("/", methods=['GET'])
def home():
    return "What's up G"

@app.route("/api/home", methods=['GET'])
def return_home():
    return jsonify({
        'message': "Get Started For free!"
    })

@app.route("/api/send_email", methods=['POST'])
def send_email():
    data = request.form.to_dict()
    name = data['name']
    email = data['email']
    message = data['message']

    msg = Message("Message from " + name,
                sender=(name, "seanwaterloo2997@gmail.com"),
                recipients=["seanwaterloo2997@gmail.com"])
    msg.body = f"{name}, {email} says:\n\n" + message
    try:
        mail.send(msg)
        return jsonify({
            'message': "Message sent!"
        })
    except Exception as e:
        return jsonify({
            'message': "Message failed to send: " + str(e)
        })

if __name__ == "__main__":
    app.run(debug=False, port=8080)