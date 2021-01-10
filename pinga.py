import urllib.request
while True:
    site = input("Enter site name: ")
    site = "https://www." + site
    try:
        urllib.request.urlopen(site).getcode()
        print(site + " is up!")
    except:
        print(site + " is down!")
