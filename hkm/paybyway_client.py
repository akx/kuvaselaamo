
# -*- coding: utf-8 -*-

import logging
import requests
import hmac
import hashlib
import base64

from hkm import settings

LOG = logging.getLogger(__name__)


class PaybywayClient(object):

    API_ENDPOINT = settings.PBW_API_ENDPOINT
    API_KEY = settings.PBW_API_KEY
    SECRET_KEY = settings.PBW_SECRET_KEY

    def post(self, order_hash, price):
        url = PaybywayClient.API_ENDPOINT + '/auth_payment'
        msg = '%s|%s' % (PaybywayClient.API_KEY, order_hash)
        authcode = hmac.new(PaybywayClient.SECRET_KEY, msg,
                            hashlib.sha256).hexdigest().upper()
        # TODO refactor to reverse
        return_url = '%s/order/%s/confirmation/' % (
            settings.MY_DOMAIN, order_hash)
        # TODO refactor to reverse
        notify_url = '%s/order/%s/notify/' % (settings.MY_DOMAIN, order_hash)

        payload = {
            'version': 'w3.1',
            'api_key': PaybywayClient.API_KEY,
            'order_number': order_hash,
            'amount': price,
            'currency': 'EUR',
            'payment_method': {
                'type': 'e-payment',
                'return_url': return_url,
                'notify_url': notify_url,
            },
            'authcode': authcode
        }

        try:
            r = requests.post(url, json=payload, timeout=10)
            data = r.json()
            return data
        except requests.exceptions.RequestException as e:
            LOG.error(e, exc_info=True, extra={'data': {'order_hash': order_hash}})
            return None

    def cancel(self, order_hash):
        url = PaybywayClient.API_ENDPOINT + '/cancel'
        msg = '%s|%s' % (PaybywayClient.API_KEY, order_hash)
        authcode = hmac.new(PaybywayClient.SECRET_KEY, msg,
                            hashlib.sha256).hexdigest().upper()

        payload = {
          'version': 'w3.1',
          'api_key': PaybywayClient.API_KEY,
          'order_number': order_hash,
          'authcode': authcode,
        }

        try:
            r = requests.post(url, json=payload, timeout=10)
            data = r.json()
            return data
        except requests.exceptions.RequestException as e:
            LOG.error(e, exc_info=True, extra={'data': {'order_hash': order_hash}})
            return None

# just for testing this with a random order ID
client = PaybywayClient()
# client.post(139,777)

# /confirmation/?AUTHCODE=1CFDD5E0562B7772AF875859B009B05AF03670BE522097B20DC39E5B5229857A&RETURN_CODE=0&ORDER_NUMBER=hkmorder58&SETTLED=1
