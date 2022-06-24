import os
import json
import safaribooks
import argparse

for (dirpath, dirnames, filenames) in os.walk("../OneDrive - ueqt/safaribooks/_index/"):
    for filename in filenames:
        with open(dirpath + '/' + filename) as json_file:
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
                book = safaribooks.SafariBooks(args)
        except FileNotFoundError as err:
            print(args.bookid + " not found")
        except Exception as err:
            print(err)
            continue
