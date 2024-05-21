import time
import json
import hmac
import hashlib
import binascii
from locust import HttpUser, task, between


class ApiV2(HttpUser):
    host = 'http://120.46.177.228'
    wait_time = between(1, 2)

    @task
    def webhook(self):
        self.client.post('/webhook1')

    # def request(self, app_id, app_secret, api, data):
    #     timestamp = int(time.time())
    #     body = json.dumps(data)
    #     sign_text = f"{app_id}{timestamp}"
    #     if len(body) != 2:
    #         sign_text = f"{sign_text}{body}"
    #     else:
    #         body = ""
    #     h = hmac.new(app_secret.encode('utf-8'), sign_text.encode('utf-8'), hashlib.sha256)
    #     server_sign = binascii.hexlify(h.digest()).decode('utf-8')
    #     return self.client.post(url='https://efb014f4merchantdev.ccpayment.com/ccpayment/v2/' + api,
    #                             headers={
    #                                 "Content-Type": "application/json;charset=uf8",
    #                                 "Appid": app_id,
    #                                 "Sign": server_sign,
    #                                 "Timestamp": f"{timestamp}"},
    #                             data=body)

    # @task
    # def get_coin_list(self):
    #     self.request(app_id='EvBIS9dcPwsWsG9B',
    #                  app_secret='2774c894fa90fd7fddf3015b4bad3174',
    #                  api='getCoinList',
    #                  data={})
    #
    # @task
    # def get_coin(self):
    #     self.request(app_id='EvBIS9dcPwsWsG9B',
    #                  app_secret='2774c894fa90fd7fddf3015b4bad3174',
    #                  api='getCoin',
    #                  data={'coinId': 3096})
