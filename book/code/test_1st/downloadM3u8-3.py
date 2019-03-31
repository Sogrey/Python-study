import os
import time
import m3u8
import requests
from glob import iglob
import natsort
from concurrent.futures import ThreadPoolExecutor

from natsort import natsorted


def get_ts_url(m3u8_url):
    m3u8_obj = m3u8.load(m3u8_url)
    base_uri = m3u8_obj.base_uri

    for seg in m3u8_obj.segments:
        yield base_uri + seg.uri


def download_ts(urlinfo):
    url, ts_name = urlinfo
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36', }
    Res = requests.get(url, headers=headers)
    with open(ts_name, 'wb') as fp:
        fp.write(Res.content)


def combin_ts(ts_dir=os.path.dirname(__file__)):
    ts_path = os.path.join(ts_dir, '*.ts')
    new_path = os.path.join(ts_dir, 'new')  # 防止被处理,写判断多余，直接重命名即可
    with open(new_path, 'wb') as fn:
        for ts in natsorted(iglob(ts_path)):
            with open(ts, 'rb') as ft:
                scline = ft.read()
                fn.write(scline)
    for ts in natsorted(iglob(ts_path)):  # 删除下载的ts文件
        os.remove(ts)
    os.rename(new_path, new_path + '.ts')


if __name__ == '__main__':
    m3u8_url = 'https://zk.wb699.com/2019/03/06/aLdpUIBeHC48HGTk/playlist.m3u8'
    # 'http://pp385.com:2100/ppvod/S8buERIZ.m3u8'
    urls = get_ts_url(m3u8_url)

    threadpool = ThreadPoolExecutor(max_workers=10)
    start = time.time()

    for index, url in enumerate(urls, 1):
        threadpool.submit(download_ts, [url, f'{index}.ts'])  # 强制设置文件以索引命名
    threadpool.shutdown()

    end = time.time()

    print(f"用时:{end - start}")
    start = time.time()
    combin_ts()
    end = time.time()
    print(f"用时:{end - start}")
