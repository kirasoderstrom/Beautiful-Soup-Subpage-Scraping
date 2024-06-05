import requests
from bs4 import BeautifulSoup
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

from urllib.parse import urlparse

def print_blobs_in_container(container_client):
    # List the blobs in the container
    blobs = container_client.list_blobs()
    # Get the count of blobs
    blob_count = len(list(blobs))
    # Print the result
    print(f"Number of blobs in container '{container_name}': {blob_count}")

def get_base_url(link):
    parsed_url = urlparse(link)
    return f"{parsed_url.scheme}://{parsed_url.netloc}"

def upload_file_to_blob(file_content, blob_name):
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(file_content, blob_type="BlockBlob", overwrite=True)

def get_subpages(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    links = soup.find_all('a')
    subpages = [link.get('href') for link in links if isinstance(link.get('href'), str) and link.get('href').startswith('/')]
    subpages = list(set(subpages))
    return subpages

def scrape_and_upload_subpages(main_url):
    subpages = get_subpages(main_url)
    base_url = get_base_url(main_url)
    print("Length of subpages: " , len(subpages))
    for subpage_url in subpages:
        print("subpage url:" + subpage_url)
        full_subpage_url = base_url + subpage_url
        print("full subpage url:" + full_subpage_url)
        subpage_content = requests.get(full_subpage_url).text
        blob_name = subpage_url.split('/')[-1]  # Create a blob name based on the subpage URL
        if not blob_name:  # If the URL ends with a '/', take the second last part of the URL
            blob_name = subpage_url.strip('/').split('/')[-1]
        upload_file_to_blob(subpage_content, blob_name + '.html')  # Append '.html' to the blob name
    print("finished")

# Initialize the Blob Service Client
connection_str = 'your_connection_string'
container_name = 'your_container_name'
blob_service_client = BlobServiceClient.from_connection_string(connection_str)
container_client = blob_service_client.get_container_client(container_name)

# Set url variable to scrape
main_url = 'url_to_scrape'

# Print log of current quantity of containers prior to run
print("Prior to running scraping logic")
print_blobs_in_container(container_client)

# Scrape websites from main_url
scrape_and_upload_subpages(main_url)

# Print log of current quantity of containers after scraping and uploading subpages
print("After running scraping logic")
print_blobs_in_container(container_client)