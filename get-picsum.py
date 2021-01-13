import sys, os
import shutil

import requests

if len(sys.argv) != 3:
    raise TypeError("Wrong amount of arguements, should be 2 command line arguements (excluding source code file).")

url_args = sys.argv[1]

num_of_times = int(sys.argv[2])
# 这里设置目录
dir_path = 'img/' + url_args.replace('/', '_').replace('.', '_')
print("dest dir:", dir_path)

exist_f_num = set()
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
else:
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            f_num = file.split('.')[0]
            exist_f_num.add(int(f_num))
# 补齐数字空隙

if exist_f_num:
    max_num = int(max(exist_f_num))
    new_set = set(int(i) for i in range(max_num + 1))
    need_add_num = list(new_set-exist_f_num)
    new_add_num = need_add_num + [int(i) for i in range(max_num + 1, max_num + 1 + num_of_times)]
else:
    new_add_num = [i for i in range(num_of_times)]

default = ""
for i in new_add_num:
    print(f"try to get number {i} img")
    url = f"https://picsum.photos/id/{i}/{url_args}"
    # url = f"https://picsum.photos/{url_args}"
    # url = f"https://corgi.photos/{url_args}"
    r = requests.get(url, stream=True)
    try:
        suffix = r.headers['Content-Type'].split('/')[1]
    except:
        suffix = 'png'
    with open(f"{dir_path}/{i}.{suffix}", "wb") as img:
        # shutil.copyfileobj(r.raw, img)
        img.write(r.content)
