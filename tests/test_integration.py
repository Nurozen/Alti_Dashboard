import requests

def test_input_text():
    url = "http://127.0.0.1:5005/user_input"

    payload = {'input': 'test'}
    files=[

    ]
    headers = {}

    input_response = requests.request("POST", url, headers=headers, data=payload, files=files)

    url = "http://127.0.0.1:5005/input_analysis"

    payload = {'input_resp': input_response.text}
    files=[

    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)

    assert response.text == """[" test"]\n"""