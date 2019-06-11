#!/usr/bin/env python3
"""A local listener for webhook."""
import argparse
import datetime as DT
import hashlib
import hmac
from flask import Flask, abort, request
import requests
import time


app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    """Webhook listener."""
    if request.method == 'POST':

        # Authentication
        uber_signature = request.headers.get('X-Uber-Signature')
        if not verify_signature(uber_signature, request.data):
            print('Signature is incorrect, return 401')
            return '', 401

        meta_data = request.get_json().get('meta')

        # get order id from meta data
        order_id = meta_data.get('resource_id')

        # get store id from meta data
        store_id = meta_data.get('user_id')

        print('Retrieving order details...')
        # use Get Order API to get the order details
        order_details = get_order_details(order_id)

        print(order_details)

        # YOUR CODES HERE
        # retrieve and save access token when needed
        # push the order details to the POS using store ID
        # logging the records

        print('send 200 OK to webhook')
        return '', 200
    else:
        abort(400)


def parse_args():
    """Define, parse and return command-line arguments."""
    parser = argparse.ArgumentParser()
    parser._action_groups.pop()
    required = parser.add_argument_group("required arguments")
    optional = parser.add_argument_group("optional arguments")

    required.add_argument(
        "-s", "--secret",
        help="client secret",
        type=str,
        required=True
    )
    required.add_argument(
        "-c", "--client",
        help="client id",
        type=str,
        required=True
    )
    optional.add_argument(
        "-p", "--port",
        help="port",
        default=5000,
        type=int
    )

    return parser.parse_args()


def verify_signature(uber_signature, body):
    """Check if the  signature is correct."""
    # convert secret to bytes
    secret = bytes(args.secret, encoding='utf-8')
    digester = hmac.new(secret, body, hashlib.sha256).hexdigest()

    if digester == uber_signature:
        return True
    else:
        return False


class GetAccessToken:
    """Processor that gets access token."""

    def __init__(self, scope):
        """Construct the scope type and token."""
        timestamp = time.time()
        self.scope = scope
        self.token = None

        if self.token is None or self.token.expires_in < timestamp:
            payload = {
                'client_secret': args.secret,
                'client_id': args.client,
                'grant_type': 'client_credentials',
                'scope': self.scope
            }
            res = requests.post('https://login.uber.com/oauth/v2/token', data=payload)
            res_json = res.json()
            print('requested new access token')

            # This is only an example for storing the access token
            # You should use your own method for token management
            self.token = {
                'access_token': res_json.get('access_token'),
                'scope': res_json.get('scope'),
                'expires_in': access_token_expiry(res_json.get('expires_in'))
            }


def get_order_details(id):
    """Get order details from Uber."""
    headers = {'Authorization': 'Bearer ' + _access_token_order.token.get('access_token')}
    res = requests.get('https://api.uber.com/v1/eats/orders/' + id, headers=headers)
    return res.json()


def access_token_expiry(seconds):
    """Calculate the expiry date of the access token."""
    ts = DT.datetime.now() + DT.timedelta(seconds=seconds)
    st = ts.strftime("%s")
    return st


if __name__ == '__main__':
    args = parse_args()
    # This is only an example of storing the access token into a variable
    # You should use your own method for token management
    _access_token_order = GetAccessToken('eats.order')
    print('Webhook listener is now activated')
    app.run(debug=False, use_reloader=True, port=args.port)
