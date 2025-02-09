from concurrent.futures import ThreadPoolExecutor
from multiprocessing import AuthenticationError
import os
import json
import time
import safaribooks
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

# https://learning.oreilly.com/search/?query=*&extended_publisher_data=true&highlight=true&include_assessments=false&include_case_studies=true&include_courses=true&include_playlists=true&include_collections=true&include_notebooks=true&include_cloud_scenarios=true&include_sandboxes=true&include_scenarios=true&is_academic_institution_account=false&source=user&formats=book&sort=relevance&facet_json=true&json_facets=true&page=0&include_facets=true&include_practice_exams=true

currentPath = os.getcwd()
defaultPath = currentPath + "/../OneDrive - ueqt/safaribooks/_index/"
lock = Lock()
# lock2 = Lock()
thread_count = 16
result = 0
delete_count = 0
# notfounds = []

def dealFile(filename):
    global result
    global delete_count
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
        args.dir = currentPath + "/Downloads/"
        args.no_cookies = None
        args.log = None
        args.cred = None
        args.kindle = None
        if os.path.isfile(currentPath + "/info_" + args.bookid + ".log"):
            # 有日志
            print('has log')
            if os.stat(currentPath + "/info_" + args.bookid + ".log").st_size == 0 : 
                os.remove(currentPath + "/info_" + args.bookid + ".log")
        # 仅中文
        # if data["language"].startswith("zh"):
        if not os.path.isfile(args.dir + args.bookid + "/" + args.bookid + ".epub") and not os.path.isfile(args.dir  + "../../OneDrive - ueqt/safaribooks/" + args.bookid + ".epub"):
            # 没处理过
            print('start deal')
            safaribooks.SafariBooks(args)
            print('deal end')
    except FileNotFoundError as err:
        print(args.bookid + " not found")
        if not os.path.exists(defaultPath + "../" + filename[0:-4] + "epub"):
            os.remove(defaultPath + filename)
            delete_count = delete_count + 1
        # with lock2:
        #     notfounds.append(args.bookid + ' ' + filename)
    except AuthenticationError as err:
        print('no auth')
        os.kill(os.getpid(), 9)
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

# for nf in notfounds:
#     toDelete = nf.split(' ')
#    if os.stat(currentPath + "/info_" + toDelete[0] + ".log").st_size == 0 : 
#         os.remove(defaultPath + toDelete[1])
#        try:
#            os.remove(currentPath + "/info_" + toDelete[0] + ".log")
#        except:
#            pass
#        print('deleted ' + nf)

print('*' * 50)
print('*' * 50)
print('*' * 50)
print("finish")
print('*' * 50)
print('*' * 50)
print('*' * 50)
print('delete: ' + str(delete_count))
with open('./_delete.txt', 'w') as txt_file_handler:
    txt_file_handler.write(str(delete_count))
txt_file_handler.close()  
