import json


def save_object_to_json(obj, file_path):
    data = {}

    attributes = dir(obj)
    for attr in attributes[-5:]:  # ignores unnecessary information
        print(attr)
        try:
            value = getattr(obj, attr)
            if attr in ["send", "stream"]:
                data[attr] = "method"
            else:
                data[attr] = value
        except Exception:
            data[attr] = None

    # Write the data to a JSON file
    with open(file_path, "w") as json_file:
        json.dump(data, json_file, cls=CustomEncoder, indent=4)

    print(f"Object attributes saved to {file_path}")


class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        if hasattr(o, "__dict__"):
            return o.__dict__
        else:
            return str(o)
