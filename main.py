import requests
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument('url', help='URL to download video from ex. https://www.instagram.com/p/id')
parser.add_argument('name', help='Output name')
args = parser.parse_args()

res = requests.get(args.url)
dec = res.content.decode()
soup = BeautifulSoup(dec, 'html.parser')
videotag = soup.find_all('meta', attrs={'property':'og:video:secure_url'})
video = str(videotag[0])
video = video.strip('" property="og:video:secure_url"/>')
video = video.strip('<meta content="')
if 'instagram' in args.url:
    final_link = video.split('amp;')
    final_link = final_link[0] + final_link[1] + final_link[2] + final_link[3] + final_link[4]
    r = requests.get(final_link)
elif 'facebook' in args.url:
    final_link = video.split('amp;')
    final = ""
    for x in range(0,8):
        final += final_link[x]
    final_link = final
    r = requests.get(final_link)
file_name = args.name + ".mp4"
x = open(file_name, "wb")
x.write(r.content)
x.close()
