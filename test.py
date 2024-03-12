import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def get_all_urls(base_url, depth, current_depth=1):
    if current_depth > depth:
        return set()

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
                # Add anything after `/` to the URL
                url_parts = urlparse(url)
                path = url_parts.path
                if path and path != '/':
                    urls.add(urljoin(url, path))

        # Recursively get URLs from linked pages up to the specified depth
        if current_depth < depth:
            for url in urls.copy():
                urls |= get_all_urls(url, depth, current_depth + 1)

        return urls
    else:
        # If the request was not successful, print an error message
        print("Failed to retrieve page:", response.status_code)
        return set()

# Example usage:
if __name__ == "__main__":
    url = input("Enter the URL: ")
    depth = int(input("Enter the depth (up to 6): "))
    all_urls = get_all_urls(url, depth)
    if all_urls:
        print("All URLs found up to depth", depth, "under", url, ":")
        for url in all_urls:
            print(url)
    else:
        print("No URLs found.")
