import traceback
import requests


class APIMethod:
    @staticmethod
    def _generate_url(base_url, endpoint=None, params=None) -> str:
        # Generate URL from endpoint and optional parameters
        url = base_url
        if endpoint:
            url += '/' + '/'.join(map(str, endpoint))

        # Adding query parameters from params
        if params:
            url += '?' + '&'.join([f"{key}={value}" for key, value in params.items()])
        return url

    def __init__(self, base_url, logger):
        self._base_url = base_url
        self._logger = logger

    def _send_request(self, method, *endpoint, headers=None, payload=None, params=None):
        url = self._generate_url(self._base_url, endpoint, params)
        self._logger.info(f"Request Method: {method.__name__}")
        self._logger.info(f"URL: {url}")
        try:
            response = method(url=url, headers=headers, json=payload, verify=False)
            self._logger.info(f"Response Status: {response.status_code}")
            self._logger.info(f"Response Body: {response.text}")
            return response
        except Exception as e:
            exception = str(e) + "\n" + str(traceback.format_exc())
            self._logger.error(f"Exception: {exception}")
            return None

    def get(self, *endpoint, **params):
        return self._send_request(requests.get, *endpoint, params=params)

    def post(self, headers, payload, *endpoint):
        return self._send_request(requests.post, *endpoint, headers=headers, payload=payload)

    def put(self, headers, payload, *endpoint):
        return self._send_request(requests.put, *endpoint, headers=headers, payload=payload)

    def delete(self, *endpoint):
        return self._send_request(requests.delete, *endpoint)
