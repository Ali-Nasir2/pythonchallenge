import pyshorteners

long_url=input("Enter the URL to shorten: ")
type_tiny=pyshorteners.Shortener()

shorturl=type_tiny.tinyurl.short(long_url)

print("Shortened URL is: ",shorturl)



