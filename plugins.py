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
        
        print("Installed Jenkins Plugins:")
        for plugin in plugins:
            print(f"Plugin: {plugin['shortName']}, Version: {plugin['version']}, Active: {plugin['active']}, Enabled: {plugin['enabled']}")
except Exception as e:
    print(f"Exception occurred: {str(e)}")
