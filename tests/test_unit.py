import requests

def test_new_entry():
    url = "http://127.0.0.1:5005/new"

    payload = {}
    files=[

    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)

    assert type(response.text) == '<class ‘string‘>'

def test_tests():
    assert 'Input: test' == 'Input: test'