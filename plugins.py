import subprocess
import json
import re

# Jenkins credentials and URL
jenkins_url = "http://your-jenkins-server"
username = "your-username"
api_token = "your-api-token"

# Function to create a valid filename from a URL
def create_filename_from_url(url):
    # Remove the protocol (http or https) and any non-alphanumeric characters
    sanitized_url = re.sub(r'http[s]?://', '', url)
    sanitized_url = re.sub(r'\W+', '_', sanitized_url)
    return f"{sanitized_url}_plugins.json"

# Create the complete Jenkins API URL
api_url = f"{jenkins_url}/pluginManager/api/json?depth=1"

# Create a filename based on the Jenkins server URL
json_filename = create_filename_from_url(jenkins_url)

# Curl command to get the list of installed plugins
curl_command = f'curl -u {username}:{api_token} "{api_url}"'

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
        with open(json_filename, 'w') as json_file:
            json.dump(plugin_versions, json_file, indent=4)
        
        print(f"Plugin information has been saved to {json_filename}")
except Exception as e:
    print(f"Exception occurred: {str(e)}")
