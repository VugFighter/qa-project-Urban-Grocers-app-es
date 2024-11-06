import requests
import configuration
import data

def post_new_user():
    url = f"{configuration.URL_SERVICE + configuration.CREATE_USER_PATH}"
    headers = {"content-type": "application/json"}
    response = requests.post(url, json=data.new_user_data, headers=headers)

    if response.status_code == 201:
        print("Respuesta de post_new_user:", response.json())
        return response.json().get('authToken')
    else:
        print(f"Error: Código de estado {response.status_code} en post_new_user")
        return None

def post_new_client_kit(kit_body):
    auth_token = post_new_user()
    if not auth_token:
        print("Error: No se obtuvo el token de autorización, no se puede continuar.")
        return None

    url = f"{configuration.URL_SERVICE + configuration.KITS_PATH}"
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "content-type": "application/json"
    }
    response = requests.post(url, json=kit_body, headers=headers)
    return response



