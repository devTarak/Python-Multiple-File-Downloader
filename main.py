import os
import requests
from bs4 import BeautifulSoup
import csv
"""
This Script is developed by Developer Tarak.
visit: https://devtarak.github.io/
"""

def download_pdf(url, folder, filename):
    response = requests.get(url)
    if response.status_code == 200:
        os.makedirs(folder, exist_ok=True)
        filepath = os.path.join(folder, filename)

        with open(filepath, 'wb') as file:
            file.write(response.content)
        print(f"PDF file '{filename}' downloaded to '{folder}' successfully.")
    else:
        print(f"Failed to download PDF file from '{url}'. Status code: {response.status_code}")


def find_and_download_pdfs(url, folder):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a', href=True)

        for link in links:
            href = link['href']
            if href.endswith('.pdf'):
                pdf_url = href if href.startswith('http') else f'{url}/{href}'
                filename = os.path.basename(pdf_url)
                download_pdf(pdf_url, folder, filename)


csv_file_path = 'source-file-list.csv'
names_list = []
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  
    for row in csv_reader:
        names_list.append(row[0])

download_folder = "downloaded_pdfs"
for name in names_list:
    url = f"https://api.codewithharry.com/media/videoSeriesFiles/courseFiles/{name}/" //replace this Url accroding to your needs
    find_and_download_pdfs(url, download_folder)
