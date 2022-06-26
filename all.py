from concurrent.futures import ThreadPoolExecutor
import os
import json
import time
import safaribooks
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

currentPath = os.getcwd()
defaultPath = currentPath + "/../OneDrive - ueqt/safaribooks/_index/"
lock = Lock()
thread_count = 64
result = 0

def dealFile(filename):
    global result
    with lock:
        result += 1
        print('=' * 50)
        print(result)
        print(filename)
        print("begin")
    try:
        with open(defaultPath + filename) as json_file:
            data = json.load(json_file)
        args = argparse.Namespace()
        args.bookid = data["archive_id"]
        args.url = data["url"]
        args.dir = currentPath + "/../OneDrive - ueqt/safaribooks/"
        args.no_cookies = None
        args.log = None
        args.cred = None
        args.kindle = None
        if os.path.isfile(currentPath + "/info_" + args.bookid + ".log"):
            # 有日志
            print('has log')
            if os.stat(currentPath + "/info_" + args.bookid + ".log").st_size == 0 : 
                os.remove(currentPath + "/info_" + args.bookid + ".log")
        if not os.path.isfile(args.dir + args.bookid + "/" + args.bookid + ".epub"):
            # 没处理过
            print('start deal')
            safaribooks.SafariBooks(args)
    # except FileNotFoundError as err:
    #     print(args.bookid + " not found")
        print('deal end')
    except Exception as err:
        print(err)
    print('done: ' + filename)
    return filename

for (dirpath, dirnames, filenames) in os.walk(defaultPath):
    list_fn = [i for i in filenames]
    # time.sleep(5)
    with ThreadPoolExecutor(max_workers=thread_count) as t:
        # begin = time.time()
        t.map(dealFile, list_fn)
        # obj_list = []
        # for fn in filenames:
        #     obj = t.submit(dealFile, fn)
        #     obj_list.append(obj)

        # for future in as_completed(obj_list):
        #     data = future.result()
        #     print(data)
        #     print('*' * 50)

        # times = time.time() - begin
        # print(times)
    print(len(list_fn))
    print(result)
print('*' * 50)
print('*' * 50)
print('*' * 50)
print("finish")
print('*' * 50)
print('*' * 50)
print('*' * 50)
