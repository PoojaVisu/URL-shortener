import pyshorteners
link=input('enter the link:')
shorten_url=pyshorteners.Shortener()
x=shorten_url.tinyurl.short(link)
print("Shortened URL is:",x)
