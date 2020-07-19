# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 18:22:28 2020

@author: Ultimate-SK
"""
import youtube_dl
import requests
import re


def captions_test02(url):
        ydl = youtube_dl.YoutubeDL({'writesubtitles': True, 'allsubtitles': False, 'writeautomaticsub': True})
        res = ydl.extract_info(url, download=False)
        if res['requested_subtitles'] and res['requested_subtitles']['en']:
            print('Grabbing vtt file from ' + res['requested_subtitles']['en']['url'])
            response = requests.get(res['requested_subtitles']['en']['url'], stream=True)
            f1 = open("testfile02.txt", "w")
            new = re.sub(r'\d{2}\W\d{2}\W\d{2}\W\d{3}\s\W{3}\s\d{2}\W\d{2}\W\d{2}\W\d{3}','',response.text)
            f1.write(new)
            f1.close()
            if len(res['subtitles']) > 0:
                print('manual captions')
            else:
                print('automatic_captions')
        else:
            print('Youtube Video does not have any english captions')
            

    
if __name__ == '__main__':
        
    captions_test02("https://www.youtube.com/watch?v=icetLikj7XY") 