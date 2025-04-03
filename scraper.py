import requests
from bs4 import BeautifulSoup

# Define the topic and output file
topic = "riv"
filename = f"{topic}_corpus.txt"

# Open the file for writing
with open(filename, "w", encoding="utf-8") as file:
    # Loop through pages 1 to 46
    for i in range(1, 47):
        url = f"https://arashlaw.com/category/local-accidents-news/riverside-county/page/{i}"
        print(f"Scraping page {i}...")

        # Fetch the webpage content
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Extract all text from paragraphs
            paragraphs = soup.find_all("p")
            text = "\n".join([p.get_text() for p in paragraphs])

            # Write to file
            file.write(text + "\n\n")
        else:
            print(f"Failed to retrieve page {i}. Skipping...")

print(f"Text successfully saved to {filename}")
