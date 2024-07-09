import requests

# Replace these variables with your actual values
jenkins_url = 'http://<jenkins-server>'
job_name = 'example-job'
github_token = '<your-github-token>'

# Construct the URL for the last completed build
url = f"{jenkins_url}/job/{job_name}/lastCompletedBuild/api/json"

# Headers for GitHub token authentication
headers = {
    'Authorization': f'token {github_token}'
}

# Make the request to the Jenkins API
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    build_info = response.json()
    print("Last completed build info:")
    print(build_info)
else:
    print(f"Failed to get job info: {response.status_code}")
