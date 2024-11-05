import sender_stand_request

# Obtener el token antes de las pruebas
auth_token = sender_stand_request.post_new_user()  # Esto obtiene el token

# Definir las funciones antes de usarlas
def positive_assert(response, expected_name):
    assert response.status_code == 201, f"Test Fallido: Se esperaba 201, pero se recibió {response.status_code}\nRespuesta: {response.json()}"
    assert response.json().get("name") == expected_name, f"El nombre en la respuesta no coincide con el enviado: {response.json().get('name')}"

def negative_assert(response, expected_status=400):
    assert response.status_code == expected_status, f"Test Fallido: Se esperaba {expected_status}, pero se recibió {response.status_code}\nRespuesta: {response.json()}"

# Casos positivos y negativos
def test_1_1_letter_name():
    response = sender_stand_request.post_new_client_kit({"name": "A"}, auth_token)
    positive_assert(response, "A")

def test_2_511_letter_name():
    response = sender_stand_request.post_new_client_kit({"name": "A" * 511}, auth_token)
    positive_assert(response, "A" * 511)

# Continúa con los demás tests...


# Casos negativos
def test_3_0_letter_name():
    response = sender_stand_request.post_new_client_kit({"name": ""}, "your_auth_token")
    negative_assert(response, 400)

def test_4_512_letter_name():
    response = sender_stand_request.post_new_client_kit({"name": "A" * 512}, "your_auth_token")
    negative_assert(response, 400)

def test_5_special_car_name():
    response = sender_stand_request.post_new_client_kit({"name": "@#$%^&*"}, auth_token)
    positive_assert(response, "@#$%^&*")  # Cambiar a `positive_assert` según la sugerencia

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
