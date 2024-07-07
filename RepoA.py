import yaml
import requests

def main():
    url = "https://github.com/Ali-Hadi-Saker/Repo-A-B/main/config.yaml"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            print(response.text)
            config = yaml.safe_load(response.text)
            if config.get('run_localhost'):
                print('ERROR !!!')
        except yaml.YAMLError as exc:
            print(f"Error parsing YAML: {exc}")
    else:
        print(f"Failed to fetch the config.yaml file. Status code: {response.status_code}")

main()



# def repo_name():
#     print('hi Repo A')