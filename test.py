import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def get_all_urls(base_url):
    # Send a GET request to the base URL
    response = requests.get(base_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract all anchor tags (links) from the page
        links = soup.find_all('a')

        # Extract href attribute from each anchor tag
        urls = set()
        for link in links:
            href = link.get('href')
            # If href is not None and is a valid URL, add it to the set of URLs
            if href:
                # Normalize the URL by joining with base URL
                url = urljoin(base_url, href.strip())
                urls.add(url)

        return urls
    else:
        # If the request was not successful, print an error message
        print("Failed to retrieve page:", response.status_code)

# Example usage:
if __name__ == "__main__":
    url = input("Enter the URL: ")
    all_urls = get_all_urls(url)
    if all_urls:
        print("All URLs found under", url, ":")
        for url in all_urls:
            print(url)
    else:
        print("No URLs found.")
