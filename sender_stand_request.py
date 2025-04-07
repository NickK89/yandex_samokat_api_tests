import configuration
import requests
import data


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                        json=body,
                        headers=data.headers)


def post_order_and_get_track_number():
    response = post_new_order(data.new_order_body)
    track_number = response.json()['track']
    return track_number


def get_order_by_track(track):
    order = requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + str(track),
                        headers=data.headers)
    return order