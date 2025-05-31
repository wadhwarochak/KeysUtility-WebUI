import csv
from playwright.sync_api import sync_playwright

# Set the target URL
url = "http://main.test.silicon-alliance.com/hp-intel"  # Replace with the actual URL

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(url)

    # -------- Get all featured_document_key values --------
    # Look for any elements with the attribute "featured_document_key"
    featured_elements = page.query_selector_all('[featured_document_key]')
    featured_keys = []
    for el in featured_elements:
        key_value = el.get_attribute("featured_document_key")
        if key_value:
            featured_keys.append(key_value.strip())

    # -------- Get all anchor tags --------
    #anchors = []
    #anchor_elements = page.query_selector_all("a")
    #for el in anchor_elements:
    #    href = el.get_attribute("href")
    #    text = el.inner_text().strip()
    #    if href:
    #        anchors.append({"text": text, "href": href})

    browser.close()

# -------- Save to CSV --------
with open("Featured_Keys.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Type", "Value"])

    # Write featured_document_key values
    for key in featured_keys:
        writer.writerow(["FeaturedDocumentKey", key, ""])

    # Write anchor tag values
    #for anchor in anchors:
    #    writer.writerow(["Anchor", anchor["text"], anchor["href"]])
