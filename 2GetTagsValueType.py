import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
import csv

#url = ""  # Replace with your target URL


response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

data = []


for tag in soup.find_all(attrs={"document_key": True}):
    #print(str(tag.get_text(strip=True)))
    #print(str(tag.get_text(strip=True)))
    #print("=====")
    anchor_text = tag.get_text(strip=True)
    document_keys = tag['document_key']
    data.append((anchor_text, document_keys, 'document_key'))

for tag in soup.find_all(attrs={"internal_document_key": True}):
    #print(str(tag.get_text(strip=True)))
    #print(str(tag.get_text(strip=True)))
    #print("=====")
    anchor_text = tag.get_text(strip=True)
    document_keys = tag['internal_document_key']
    data.append((anchor_text, document_keys, 'internal_document_key'))
    
    
with open("anchors_and_document_keys.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Anchor Text", "Document Key"])
    writer.writerows(data)