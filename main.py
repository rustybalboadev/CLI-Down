import requests
import argparse
import crayons
import time
import os
from bs4 import BeautifulSoup


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--image', action='store_true')
parser.add_argument('url', help='URL to download video from ex. https://www.instagram.com/p/id')
parser.add_argument('name', help='Output name')
args = parser.parse_args()
res = requests.get(args.url)
dec = res.content.decode()
soup = BeautifulSoup(dec, 'html.parser')


print(crayons.red("""
   ____ _     ___      ____                      
  / ___| |   |_ _|    |  _ \  _____      ___ __  
 | |   | |    | |_____| | | |/ _ \ \ /\ / / '_ \ 
 | |___| |___ | |_____| |_| | (_) \ V  V /| | | |
  \____|_____|___|    |____/ \___/ \_/\_/ |_| |_|                                           
"""))

os.system('cls')
#Function to get VSCO Image
def vscoImage():
    print(crayons.green("Getting VSCO Image\n"))
    try:
        imagetag = soup.find_all('meta', attrs={'property':'og:image'})
        image = str(imagetag[0])
        image = image.strip('<meta content=')
        image = image.strip('" data-rh="true" property="og:image"/>')
        r = requests.get("https://" + image[4:]).content
        print(crayons.green("Direct link: \n{}\n".format('https://' + image[4:])))
        time.sleep(1)
        file_name = args.name + '.png'
        print(crayons.green("Saving image: {}".format(file_name)))
        x = open(file_name, "wb")
        x.write(r)
        x.close()
    except IndexError:
        print(crayons.red('Something went wrong! Check your syntax'))


# Function to get Instagram Image
def instagramImage():
    try:
        print(crayons.green("Getting Instagram Image\n"))
        imagetag = soup.find_all('meta', attrs={'property':'og:image'})
        image = str(imagetag[0])
        split = image.split(' ')
        image = split[1]
        image = image.strip('content="')
        final_link = image.split('amp;')
        final_link = final_link[0] + final_link[1] + final_link[2] + final_link[3] + final_link[4]
        r = requests.get(final_link).content
        print(crayons.green("Direct link: \n{}\n".format(final_link)))
        time.sleep(1)
        file_name = args.name + ".png"
        print(crayons.green('Saving image: {}'.format(file_name)))
        x = open(file_name, 'wb')
        x.write(r)
        x.close()
    except IndexError:
        print(crayons.red('Something went wrong! Check your syntax'))


#Function to get Instagram Video
def instagramVideo():
    try:
        videotag = soup.find_all('meta', attrs={'property':'og:video:secure_url'})
        video = str(videotag[0])
        video = video.strip('" property="og:video:secure_url"/>')
        video = video.strip('<meta content="')
        print(crayons.green('Getting Instagram Video\n'))
        final_link = video.split('amp;')
        final_link = final_link[0] + final_link[1] + final_link[2] + final_link[3] + final_link[4]
        r = requests.get(final_link).content
        print(crayons.green("Direct Link: \n{}\n".format(final_link)))
        time.sleep(1)
        file_name = args.name + ".mp4"
        print(crayons.green('Saving Video: {}'.format(file_name)))
        x = open(file_name, 'wb')
        x.write(r)
        x.close()
    except IndexError:
        print(crayons.red("Something went wrong! Check your syntax!"))


#Function to get Facebook Video
def facebookVideo():
    try:
        videotag = soup.find_all('meta', attrs={'property':'og:video:secure_url'})
        video = str(videotag[0])
        video = video.strip('" property="og:video:secure_url"/>')
        video = video.strip('<meta content="')
        print(crayons.green("Getting Facebook Video\n"))
        final_link = video.split('amp;')
        final = ""
        for x in range(0,8):
            final += final_link[x]
        final_link = final
        r = requests.get(final_link).content
        print(crayons.green('Direct Link: \n{}\n'.format(final_link)))
        time.sleep(1)
        file_name = args.name + ".mp4"
        print(crayons.green("Saving Video: {}".format(file_name)))
        x = open(file_name, 'wb')
        x.write(r)
        x.close()
    except IndexError:
        print(crayons.red('Something went wrong! Check your syntax!'))


if args.image == True:
    if 'vsco' in args.url:
        vscoImage()
    elif 'instagram' in args.url:
        instagramImage()
elif args.image == False:
    if 'instagram' in args.url:
        instagramVideo()
    elif 'facebook' in args.url:
        facebookVideo()
