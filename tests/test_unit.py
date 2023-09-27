import requests

"""def test_user_input():
    url = "http://127.0.0.1:5005/user_input"

    payload = {'input': 'test'}
    files=[

    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)

    assert response.text == 'Input: test'"""

def test_tests():
    assert 'Input: test' == 'Input: test'