import subprocess
import json

# Jenkins credentials
jenkins_url = "http://your-jenkins-server/pluginManager/api/json?depth=1"
username = "your-username"
api_token = "your-api-token"

# Curl command to get the list of installed plugins
curl_command = f'curl -u {username}:{api_token} "{jenkins_url}"'

try:
    result = subprocess.run(curl_command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Failed to execute curl command")
        print(f"Error: {result.stderr}")
    else:
        plugins_info = json.loads(result.stdout)
        plugins = plugins_info.get("plugins", [])
        
        # Create a dictionary with plugin names and versions
        plugin_versions = {plugin['shortName']: plugin['version'] for plugin in plugins}
        
        # Save the dictionary to a JSON file
        with open('plugins.json', 'w') as json_file:
            json.dump(plugin_versions, json_file, indent=4)
        
        print("Plugin information has been saved to plugins.json")
except Exception as e:
    print(f"Exception occurred: {str(e)}")
