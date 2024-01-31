import yaml


def get_creds(test_data):
    with open(test_data, "r") as file:
        creds = yaml.safe_load(file)
    return creds
