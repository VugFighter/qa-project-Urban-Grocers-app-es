import sender_stand_request

# Definir las funciones antes de usarlas
def positive_assert(response):
    assert response.status_code == 201, f"Test Fallido: Se esperaba 201, pero se recibió {response.status_code}\nRespuesta: {response.json()}"

def negative_assert(response, expected_status=400):
    assert response.status_code == expected_status, f"Test Fallido: Se esperaba {expected_status}, pero se recibió {response.status_code}\nRespuesta: {response.json()}"

# Luego, define tus pruebas aquí abajo usando las funciones


# Casos positivos
def test_1_1_letter_name():
    response = sender_stand_request.post_new_client_kit({"name": "A"}, "your_auth_token")
    positive_assert(response)

def test_2_511_letter_name():
    response = sender_stand_request.post_new_client_kit({"name": "A" * 511}, "your_auth_token")
    positive_assert(response)

# Casos negativos
def test_3_0_letter_name():
    response = sender_stand_request.post_new_client_kit({"name": ""}, "your_auth_token")
    negative_assert(response, 400)

def test_4_512_letter_name():
    response = sender_stand_request.post_new_client_kit({"name": "A" * 512}, "your_auth_token")
    negative_assert(response, 400)

def test_5_special_car_name():
    response = sender_stand_request.post_new_client_kit({"name": "@#$%^&*"}, "your_auth_token")
    negative_assert(response, 400)

def test_6_space_bt_letters_name():
    response = sender_stand_request.post_new_client_kit({"name": "A B C"}, "your_auth_token")
    positive_assert(response)

def test_7_string_number_name():
    response = sender_stand_request.post_new_client_kit({"name": "123456"}, "your_auth_token")
    positive_assert(response)

def test_8_no_name():
    response = sender_stand_request.post_new_client_kit({}, "your_auth_token")  # Asumiendo que omitir el campo 'name' causa un error
    negative_assert(response, 400)

def test_9_integer_name():
    response = sender_stand_request.post_new_client_kit({"name": 123}, "your_auth_token")
    negative_assert(response, 400)
