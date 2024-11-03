import requests
import configuration
import data


def post_new_user(auth_type):
    url = f"{configuration.URL_SERVICE + configuration.CREATE_USER_PATH}"
    headers = {"Authorization": auth_type}
    response = requests.post(url, json=data.new_user_data, headers=headers)

    if response.status_code == 201:
        return response.json()
    else:
        print(f"Error: Código de estado {response.status_code} en post_new_user")
        return None


def post_new_client_kit(kit_body, auth_token):
    url = f"{configuration.URL_SERVICE + configuration.KITS_PATH}"
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.post(url, json=kit_body, headers=headers)
    return response


