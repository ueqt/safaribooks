from concurrent.futures import ThreadPoolExecutor
import os
import json
import time
import safaribooks
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed

defaultPath = "../OneDrive - ueqt/safaribooks/_index/"

def dealFile(filename):
    with open(defaultPath + filename) as json_file:
        data = json.load(json_file)
    args = argparse.Namespace()
    args.bookid = data["archive_id"]
    args.url = data["url"]
    args.dir = "../OneDrive - ueqt/safaribooks/"
    args.no_cookies = None
    args.log = None
    args.cred = None
    args.kindle = None
    try:
        if os.path.isfile("./info_" + args.bookid + ".log"):
            # 有日志
            if os.stat("./info_" + args.bookid + ".log").st_size == 0 : 
                os.remove("./info_" + args.bookid + ".log")
        if not os.path.isfile(args.dir + args.bookid + "/" + args.bookid + ".epub"):
            # 没处理过
            safaribooks.SafariBooks(args)
    except FileNotFoundError as err:
        print(args.bookid + " not found")
    except Exception as err:
        print(err)
    print('done: ' + filename)
    return filename

for (dirpath, dirnames, filenames) in os.walk(defaultPath):
    print(filenames.count())
    time.sleep(5)
    with ThreadPoolExecutor(max_workers=16) as t:
        # begin = time.time()
        t.map(dealFile, filenames)
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
print('*' * 50)
print('*' * 50)
print('*' * 50)
print("finish")
print('*' * 50)
print('*' * 50)
print('*' * 50)
