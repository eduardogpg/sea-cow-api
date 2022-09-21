from flask import Flask
from SeaCow import create_invoice as sea_cow_create_invoice

from constants import DEBUG

app = Flask(__name__)

@app.route('/api/invoices/', methods=['GET', 'POSt'])
def create_invoice():
    return sea_cow_create_invoice()

if __name__ == '__main__':
    app.run(debug=DEBUG)