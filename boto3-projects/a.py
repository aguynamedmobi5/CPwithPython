import json, requests, hashlib, os


URL = "https://api.chucknorris.io/jokes/random"


def generate_id():
    random_bytes = os.urandom(16)
    hash_object = hashlib.sha256(random_bytes)
    random_hash = hash_object.hexdigest()
    return random_hash


def get_joke():
    response = requests.get(URL)
    response.raise_for_status()
    data = response.json()
    return data["value"]


def make_json_data():
    data = {
        "jokeId": generate_id(),
        "joke": get_joke()
    }
    return data


def create_file(path, data):
    file_path = os.path.join(path, "jokes.json")

    if not os.path.exists(file_path):
        with open("jokes.json", "w") as f:
            json.dump(data, f)
    else:
        with open("jokes.json", "a") as f:
            json.dump(data, f)


# print(generate_id())


def main():
    cwd = os.getcwd()
    create_file(cwd, make_json_data())





if __name__ == "__main__":
    main()
