import urllib.request as request


print("This is a site connectivity checker program")

site = input("Enter a site to check for connectivity: ")


def siteConnection(url):
    try:
        response = request.urlopen(url)
        print(f"The code is {response.getcode()}")
    except:
        print("The site is unavailable")


siteConnection(site)