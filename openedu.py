from urllib.request import urlopen


response = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html")
html = response.read().decode('utf-8')
print(html)