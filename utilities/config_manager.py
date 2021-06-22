import json


def config_load():
    with open('appconfig.json') as config_file:
        data = json.load(config_file)

    port = data['port']
    workdir = data['workdir']
    print(port)
    print(workdir)
    return data
