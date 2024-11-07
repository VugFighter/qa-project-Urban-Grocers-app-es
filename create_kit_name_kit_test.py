import sender_stand_request

def positive_assert(response):
    assert response.status_code == 201, f"Test Fallido: Se esperaba 201, pero se recibió {response.status_code}\nRespuesta: {response.json()}"

def negative_assert(response, expected_status=400):
    assert response.status_code == expected_status, f"Test Fallido: Se esperaba {expected_status}, pero se recibió {response.status_code}\nRespuesta: {response.json()}"

def test_1_1_letter_name():
    response = sender_stand_request.post_new_client_kit({"name": "a"})
    positive_assert(response)
    response_data = response.json()
    assert response_data["name"] == "a", "Error: el nombre del kit en la respuesta no coincide con el nombre enviado en la solicitud."

def test_2_511_letter_name():
    response = sender_stand_request.post_new_client_kit({"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"})
    positive_assert(response)
    response_data = response.json()
    assert response_data["name"] == "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC", "Error: el nombre del kit en la respuesta no coincide con el nombre enviado en la solicitud."

def test_3_0_letter_name():
    response = sender_stand_request.post_new_client_kit({"name": ""})
    negative_assert(response, 400)

def test_4_512_letter_name():
    response = sender_stand_request.post_new_client_kit({"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"})
    negative_assert(response, 400)

def test_5_special_car_name():
    response = sender_stand_request.post_new_client_kit({"name": "№%@"})
    positive_assert(response)
    response_data = response.json()
    assert response_data["name"] == "№%@", "Error: el nombre del kit en la respuesta no coincide con el nombre enviado en la solicitud."

def test_6_space_bt_letters_name():
    response = sender_stand_request.post_new_client_kit({"name": " A Aaa "})
    positive_assert(response)
    response_data = response.json()
    assert response_data["name"] == " A Aaa ", "Error: el nombre del kit en la respuesta no coincide con el nombre enviado en la solicitud."

def test_7_string_number_name():
    response = sender_stand_request.post_new_client_kit({"name": "123"})
    positive_assert(response)
    response_data = response.json()
    assert response_data["name"] == "123", "Error: el nombre del kit en la respuesta no coincide con el nombre enviado en la solicitud."

def test_8_no_name():
    response = sender_stand_request.post_new_client_kit({})
    negative_assert(response, 400)

def test_9_integer_name():
    response = sender_stand_request.post_new_client_kit({"name": 123})
    negative_assert(response, 400)