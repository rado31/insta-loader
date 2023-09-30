# Download only just video or photo by [instaloader](https://instaloader.github.io) library

## Steps

- create virtual environment

```bash
python3 -m venv venv # on linux and mac
python -m venv venv # on windows
```

- activate it

```bash
source venv/bin/activate # linux and mac
Scripts/bin/activate # windows
. venv/bin/activate.fish # fish shell
```

- create urls.txt file with video urls, example

```
https://www.instagram.com/reel/CwnrCzMBL1y/?igshid=MzRlODBiNWFlZA==
https://www.instagram.com/reel/CxfTQLXIhTa/?igshid=MzRlODBiNWFlZA==
https://www.instagram.com/reel/Cw8HwaDPwib/?igshid=MzRlODBiNWFlZA==
```

- run it

```bash
python index.py
```

## If you try to download more than once, instagram will block you (with 401 status code). So use proxy for it

## It is possible to download without proxy, you just need to login an account (read the docs about it - [instaloder.doc](https://instaloader.github.io/as-module.html)), but there is an issue with loggining on the remote server 
