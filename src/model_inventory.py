import requests

OLLAMA_API = "http://172.25.48.1:11434"

def get_model_inventory():
    try:
        response = requests.get(
            f"{OLLAMA_API}/api/tags",
            timeout=5
        )

        response.raise_for_status()

        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError:
            print("Error: Ollama returned invalid JSON.")
            return None

        if not isinstance(data, dict):
            print("Error: Invalid response from Ollama API.")
            return None

        models = data.get("models")
        if not isinstance(models, list):
            print("Error: Invalid model inventory returned by Ollama.")
            return None

        return models
    
    except requests.exceptions.ConnectionError:
        print("Error: Cannot connect to Ollama.")
        return None

    except requests.exceptions.Timeout:
        print("Error: Ollama request timed out.")
        return None

    except requests.exceptions.HTTPError as error:
        print(f"HTTP Error: {error}")
        return None

    except requests.exceptions.RequestException as error:
        print(f"Unexpected request-related error: {error}")
        return None


def get_string_or_unknown(details, key):
    if isinstance(details, dict):
        value = details.get(key)
    else:
        return "Unknown"
    
    if isinstance(value, str):
        return value

    return "Unknown"


def build_inventory(models):
    if not isinstance(models, list):
        return []

    inventory = []

    for model in models:
        if (
            isinstance(model, dict)
            and isinstance(model.get("name"), str) and model.get("name").strip()
            and isinstance(model.get("details"), dict)
        ):
            inventory.append({
                "name": model['name'].strip(),
                "family": get_string_or_unknown(model['details'], "family"),
                "parameters": (get_string_or_unknown(model['details'],"parameter_size")),
                "quantisation": (get_string_or_unknown(model['details'], "quantization_level"))
            })
        else:
            print("Warning: Model data is incomplete. Skipping entry.")
            continue
    return inventory
        
def find_model(inventory, search_name):
    if isinstance(inventory, list) and isinstance(search_name, str) and search_name.strip():
        for model in inventory:
            if model['name'].lower().strip() == search_name.lower().strip():
                return model
            
    return None

def get_model_info(inventory, search_name):
    if inventory is None:
        return None
    
    inventory = build_inventory(inventory)
    return find_model(inventory, search_name)


if __name__ == "__main__":
    models = get_model_inventory()

    if models is None:
        print("Inventory is unavailable!")
    else:
        search_name = input("Enter model name to search: ")
        result = get_model_info(models, search_name)

        if result:
            print(f"Name: {result['name']}")
            print(f"Family: {result['family']}")
            print(f"Parameters: {result['parameters']}")
            print(f"Quantisation: {result['quantisation']}")
        else:
            print("Model not found!")