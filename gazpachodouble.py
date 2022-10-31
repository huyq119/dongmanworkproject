from gazpacho import get, Soup

url = "http://henanfucai.com/"
html = get(url)
soup = Soup(html)
print(html)