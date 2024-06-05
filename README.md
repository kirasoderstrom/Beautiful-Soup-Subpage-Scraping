# Beautiful Soup Web Subpage Scraping Repository

## Overview
This Python script performs web scraping to extract subpages from a given main URL and uploads the content of those subpages to an Azure Blob Storage container. The script uses the requests library to fetch the HTML content of the subpages and the BeautifulSoup library to parse the HTML.

## Prerequisites
Before running the script, ensure you have the following:

- Python 3.x installed
- Azure Blob Storage account with a container created
- Azure Blob Storage connection string (to be set as `connection_str` in the script)
- Main URL from which subpages will be scraped (to be set as `main_url` in the script)

## Setup
1. Install the required Python libraries:
- pip install requests beautifulsoup4 azure-storage-blob
1. Set the `connection_str` variable in the script to your Azure Blob Storage connection string.
1. Replace `main_url` with the URL from which you want to scrape subpages.

## Usage
Run the script using Python:
- python webscraping.py

The script will fetch subpages from the specified URL, extract their content, and upload it to the Azure Blob Storage container.

## Notes
Make sure your Azure Blob Storage container is properly configured with the correct permissions.
Adjust the script as needed to handle any specific requirements for your use case.