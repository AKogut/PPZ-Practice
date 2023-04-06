# Task 1
import re

def get_text_info(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()

    words = re.findall(r'\b\w+\b', text.lower())
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for word, count in word_count.items():
        print(f'{word} - {count}')

get_text_info('source_data/article.txt')

# Task 2
import http.client

def download_csv(urlpath):
    conn = http.client.HTTPSConnection("support.staffbase.com")
    conn.request("GET", urlpath)
    res = conn.getresponse()
    content = res.read().decode()
    rows = content.split('\n')
    rows = list(filter(lambda x: x.strip() != '', rows))
    rows = rows[:-1]
    content = '\n'.join(rows)

    with open('source_data/username.csv', 'w') as f:
        f.write(content)

    print("Completed!")

download_csv("https://support.staffbase.com/hc/en-us/article_attachments/360009197031/username.csv")

