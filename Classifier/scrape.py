import requests
from bs4 import BeautifulSoup
import csv


with open('./Classifier/datasets/code_articles.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    i = 0
    for row in reader:
        if i == 0:
            i += 1
            continue
        url = row[3]
        response = requests.get(str(url))
        if response.status_code == 200:
            # Parse the HTML content with BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all <p> tags in the HTML
            p_tags = soup.find_all('p')
            
            # Loop through and print the text within each <p> tag
            for p_tag in p_tags:
                print(p_tag.get_text())  # Get the text within the <p> tag
        else:
            print("Failed to retrieve the HTML content.")
        
# html = r.text

# #soup = BeautifulSoup(html, "html5lib")
# soup = BeautifulSoup(html, "lxml")
# print(soup.title)
# print(soup.get_text())






