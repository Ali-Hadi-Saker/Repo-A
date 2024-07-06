import yaml
import os

def main():
    config = readConfig()
    if config.get('run_localhost'):
        print('ERROR !!!')



main()

def readConfig():
    path = os.path.join(os.path.dirname(__file__), '..', 'config.yaml')
    with open(path, 'r') as file:
        config = yaml.safe_load(file)
    return config
# def repo_name():
#     print('hi Repo A')