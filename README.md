# One line Python Crawler

I got inspiration from this [BrainF* interpreter](https://github.com/davekch/b) that was written using Python in only one line. 

| |`crawler.py`|`crawler.min.py`|
|--|--|--|
|one line|:x:| :heavy_check_mark:|
|commented|:heavy_check_mark:|:x:|
|cool|:heavy_check_mark:|:heavy_check_mark:|

## Flags
|Flag|Meaning|
|--|--|
|-h|show help message|
|-u *url*|url for crawling|
|-f *file*|file to output in|
|~~-d *depth*~~|~~(optional) depth of crawl. default: 5~~|

## Usage Examples
*This program has to be run through a terminal.*<br><br>
Crawl `https://www.google.com/` and write to `links.txt`:

`$ python scraper.py -u https://www.google.com/ -f links.txt`

## Issues
- [ ] Crawls only one layer deep
