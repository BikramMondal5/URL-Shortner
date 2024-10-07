import pyshorteners


def shorten_url(url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)
    return short_url

url = ''
short_url = shorten_url(url)

print(f'Short URL: {short_url}')

