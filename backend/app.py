from flask import Flask,request,make_response,jsonify
from flask_restful import Api,Resource
from flask_cors import CORS
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

app = Flask(__name__)
api = Api(app)
CORS(app)



class ContactMe(Resource):
    def post(self):
        
        try:
            dataSubject = request.form['subject']
            dataContent = request.form['content']
            contact = Mail(
                from_email='faizalnf3245@proton.me',
                to_emails='faizalnf3245@gmail.com',
                subject=dataSubject,
                html_content=dataContent)
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            sending = sg.send(contact)
            response = {
                "msg": "Email sent successfully"
            }
            return make_response(jsonify(response))
        except Exception as e:
            print(e)

api.add_resource(ContactMe,'/api/sendemail', methods=['POST'])


if __name__ == '__main__':
    app.run(debug=True)