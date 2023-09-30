import requests
from bs4 import BeautifulSoup
import csv

def get_articles_dataset(path, limit=500, start=0):
    articles = []
    with open(path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        csv_header = 0
        for row in reader:
            if csv_header == 0:
                csv_header = 1
                continue
            elif csv_header < start:
                csv_header += 1
                continue
            if csv_header == limit:
                break
            url = row[3]
            article = row[0]
            response = requests.get(str(url))
            if response.status_code == 200:
                # Parse the HTML content with BeautifulSoup
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Find all <p> tags in the HTML
                p_tags = soup.find_all('p')
                
                # Loop through and print the text within each <p> tag
                for p_tag in p_tags:
                    article += p_tag.get_text() # Get the text within the <p> tag
                articles.append(article)  # Get the text within the <p> tag
                # print(article)
            else:
                print("Failed to retrieve the HTML content.")
            print(csv_header)
            csv_header += 1
    return articles

# print(get_articles_dataset('Classifier/datasets/code_articles.csv'))




