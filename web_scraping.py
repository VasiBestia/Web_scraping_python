import requests
import bs4

res1 = requests.get("https://quotes.toscrape.com")
soup = bs4.BeautifulSoup(res1.text, "lxml")

author = soup.select(".author")
authors_name = [a.get_text(strip=True) for a in author]
print("Authors name are:\n")
print("\n".join(authors_name))


quotes = soup.select(".text")
quotes_text = [a.get_text(strip=True) for a in quotes]
print("Quotes are:\n")
print("\n".join(quotes_text))


top10tag = soup.select(".tag-item>a")
top10tag_name = [a.get_text(strip=True) for a in top10tag]
print("Top10tag_name are:\n")
print("\n".join(top10tag_name))


basic_url = "https://quotes.toscrape.com/page/{}"

unique_authors = set()
nr = 1
fisiere = requests.get(basic_url.format(nr))
while fisiere.status_code == 200:
    getter = bs4.BeautifulSoup(fisiere.text, "lxml")
    author = getter.select(".author")

    if not author:
        break

    authors_name = [a.get_text(strip=True) for a in author]

    for a in authors_name:
        unique_authors.add(a)
    nr += 1
    fisiere = requests.get(basic_url.format(nr))

print("Unique authors on all pages are:\n")
print("\n".join(unique_authors))
