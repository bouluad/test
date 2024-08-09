import json
import requests
from requests.auth import HTTPBasicAuth

# Jenkins credentials
jenkins_url = "http://your-jenkins-url"
username = "your-username"
api_token = "your-api-token"

# Path to the JSON file with plugin information
json_file_path = "plugins.json"

# Load the JSON file
with open(json_file_path, "r") as file:
    plugins = json.load(file)

# Jenkins API endpoint for installing plugins
install_url = f"{jenkins_url}/pluginManager/installNecessaryPlugins"

# Function to install a single plugin
def install_plugin(plugin_name, plugin_version):
    # The payload format expected by Jenkins
    payload = {
        "dynamicLoad": True,
        "plugins": [{
            "name": plugin_name,
            "version": plugin_version
        }]
    }
    
    headers = {
        "Content-Type": "application/json"
    }

    # Send the POST request to install the plugin
    response = requests.post(install_url, 
                             auth=HTTPBasicAuth(username, api_token), 
                             headers=headers, 
                             json=payload)

    if response.status_code == 200:
        print(f"Plugin {plugin_name} version {plugin_version} installed successfully.")
    else:
        print(f"Failed to install plugin {plugin_name} version {plugin_version}.")
        print(f"Status Code: {response.status_code}, Response: {response.text}")

# Install each plugin from the JSON file
for plugin_name, plugin_version in plugins.items():
    install_plugin(plugin_name, plugin_version)

print("All plugins installation requests have been sent.")
