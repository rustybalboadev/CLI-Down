import requests
import argparse
import crayons
import time
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--image', action='store_true')
parser.add_argument('url', help='URL to download video from ex. https://www.instagram.com/p/id')
parser.add_argument('name', help='Output name')
options = Options()
options.add_argument('--headless')
options.add_argument('--log-level=3')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
args = parser.parse_args()
res = requests.get(args.url)
dec = res.content.decode()
soup = BeautifulSoup(dec, 'html.parser')

os.system('cls')
print(crayons.red("""
   ____ _     ___      ____                      
  / ___| |   |_ _|    |  _ \  _____      ___ __  
 | |   | |    | |_____| | | |/ _ \ \ /\ / / '_ \ 
 | |___| |___ | |_____| |_| | (_) \ V  V /| | | |
  \____|_____|___|    |____/ \___/ \_/\_/ |_| |_|                                           
"""))


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
        final_link = final_link[0] + final_link[1] + final_link[2] + final_link[3] + final_link[4] + "c"
        checkPage = requests.get(final_link).text
        if 'Bad URL' in checkPage:
            final_link = final_link[:-1]
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
def facebookVideo(url):
    try:
        print(crayons.green("Getting Facebook Video"))
        driver.get(url)
        time.sleep(4)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()
        content = """"""
        content += soup.prettify()
        soup = BeautifulSoup(content, 'html.parser')
        video_tag = soup.find_all('meta', attrs={'property':'og:video'})
        video = video_tag[0]
        video = str(video).split(' ')[1]
        video = video.strip('content="')
        final_link = video.split('amp;')
        video_link = ""
        for each in final_link:
            video_link += each
        print(crayons.green('Direct Link: \n{}\n'.format(video_link)))
        r = requests.get(video_link).content
        time.sleep(1)
        file_name = args.name + ".mp4"
        print(crayons.green('Saving Video: {}'.format(file_name)))
        x = open(file_name, 'wb')
        x.write(r)
        x.close()
    except IndexError:
        print(crayons.red('Something went wrong! Check your syntax!'))
#function to get twitch clip
def twitchClip(url):
    try:
        driver.get(url)
        time.sleep(4)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()
        content = """"""
        content += soup.prettify()
        soup = BeautifulSoup(content, 'html.parser')
        video_tag = soup.find_all('video')
        video = video_tag[0]
        video = str(video).split(' ')[2]
        video = video.split('src="')[1]
        video_link = video[:-1]
        print(crayons.green('Direct Link: \n{}\n'.format(video_link)))
        r = requests.get(video_link).content
        time.sleep(1)
        file_name = args.name + ".mp4"
        print(crayons.green('Saving Video: {}'.format(file_name)))
        x = open(file_name, 'wb')
        x.write(r)
        x.close()
    except IndexError:
        print(crayons.red('Something went wrong! Check your syntax! '))
#function to get tiktok downloader
def tiktokVideo(url):
    try:
        driver.get(url)
        time.sleep(4)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()
        content = """"""
        content += soup.prettify()
        soup = BeautifulSoup(content, 'html.parser')
        video_tag = soup.find_all('video')
        video = video_tag[0]
        video = str(video).split('src="')[1]
        video = video.replace('">\n</video>', '')
        print(crayons.green('Direct Link: \n{}\n'.format(video)))
        time.sleep(1)
        file_name = args.name + ".mp4"
        print(crayons.green('Saving Video: {}'.format(file_name)))
        r = requests.get(video).content
        x = open(file_name, 'wb')
        x.write(r)
        x.close()
    except:
        print(crayons.red('Something went wrong! Check your syntax! '))

if args.image == True:
    if 'vsco' in args.url:
        vscoImage()
    elif 'instagram' in args.url:
        instagramImage()
elif args.image == False:
    if 'instagram' in args.url:
        instagramVideo()
    elif 'facebook' in args.url:
        facebookVideo(args.url)
    elif 'twitch' in args.url:
        twitchClip(args.url)
    elif 'tiktok' in args.url:
        tiktokVideo(args.url)