# 获取bookid目录
# https://learning.oreilly.com/topics/?sort=date_added&format=book&page=1291
# 目前下载46455本书 每页36本

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import requests
import re
import json

PATH = os.path.dirname(os.path.realpath(__file__))
COOKIES_FILE = os.path.join(PATH, "cookies.json")
SESSION = requests.Session()

def retrieve_page_contents(url):
    SESSION.cookies.update(json.load(open(COOKIES_FILE)))
    r = SESSION.get(url)
    if r.status_code < 300:
        return (r.content.decode())
    
    print("Current url: {0} returned invalid status code.".format(url))
    raise ValueError('Invalid server response.')
    

def parse_contents_into_list(text): 
    return json.loads(text)["results"]

def write_id_list_to_txt_file(book_list):
    for book in book_list:
        with open("books/" + book["archive_id"] + ".json", 'w') as txt_file_handler:
            txt_file_handler.write(json.dumps(book, indent='\t'))       
        txt_file_handler.close()

if __name__ == '__main__':

    url = "https://learning.oreilly.com/api/v2/search/?query=*&limit=36&include_collections=true&include_courses=true&include_notebooks=false&include_playlists=true&include_sandboxes=true&include_scenarios=true&collection_type=expert&exclude_fields=description&include_facets=false&formats=book&sort=date_added&page="

    for page_number in range(0, 1): # range(0, 1291)
        # don't expect to see a topic with more than 100 pages of books in it
        print(page_number)
        book_list_for_topic = []
        # for page_number in range(1, 100):
        try:
            page_content = retrieve_page_contents(url + str(page_number))
            
        except ValueError:
            break
        
        finally:
            book_list = parse_contents_into_list(page_content)
            book_list_for_topic.extend(book_list)
        print("{0} book ids found".format(len(book_list_for_topic)))
        write_id_list_to_txt_file(book_list_for_topic)
            
