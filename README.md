<p align='center'>
  <img src='https://github.com/RustyBalboadev/CLI-Down/blob/master/CLI-Down.png'>
</p>

# Usage 🔧
``pip install -r requirements.txt``
```
usage: main.py [-h] [-i] url name

positional arguments:
  url          URL to download video from ex. https://www.instagram.com/p/id
  name         Output name

optional arguments:
  -h, --help   show this help message and exit
  -i, --image
```

# Examples 💡
```
python main.py -i https://www.instagram.com/p/CATBmJ9JCSo/ instagram_image
python main.py https://www.instagram.com/p/B4xWatkjsPa/ instagram_video
```
