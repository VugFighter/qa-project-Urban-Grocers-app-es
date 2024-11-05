import requests
import configuration
import data


def post_new_user():
    url = f"{configuration.URL_SERVICE + configuration.CREATE_USER_PATH}"
    headers = {"Authorization": "Bearer some_auth"}  # Usa el encabezado adecuado si es necesario
    response = requests.post(url, json=data.new_user_data, headers=headers)

    if response.status_code == 201:
        return response.json().get("authToken")  # Asume que el token está en esta clave
    else:
        print(f"Error: Código de estado {response.status_code} en post_new_user")
        return None


def post_new_client_kit(kit_body, auth_token):
    url = f"{configuration.URL_SERVICE + configuration.KITS_PATH}"
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.post(url, json=kit_body, headers=headers)
    return response


