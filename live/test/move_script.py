import json
import os
import re
import time
import random
import requests
from pypinyin import lazy_pinyin
from bs4 import BeautifulSoup

# 定义目标目录
output_dir = "dian-ying"
os.makedirs(output_dir, exist_ok=True)

# 模拟登录的会话
session = requests.Session()

# 替换为你的已登录 Cookie（从浏览器中提取）
cookies = {
    "bid": "diYTymxGzzI",
    "_pk_id.100001.4cf6": "a2e166d0ae147f6e.1734187052.",
    "__utmc": "223695111",
    "__utmz": "223695111.1734187053.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)",
    "__yadk_uid": "7DFistGj0Iicos60MzdImei1ZgT1a1i2",
    "ll": "\"108288\"",
    "_vwo_uuid_v2": "DD2B62AD85B3B570B058DEA1D45BF0EC9|f8617c8fad68166a1e15eecc3b3dffd5",
    "push_noty_num": "0",
    "push_doumail_num": "0",
    "__utmv": "30149280.28537",
    "dbcl2": "\"285378677:JVbBpS6GZeg\"",
    "ck": "p-0H",
    "frodotk_db": "\"92979b41cea5f4c2b7c6d1c56bf1de46\"",
    "ap_v": "0,6.0",
    "_pk_ref.100001.4cf6": "[\"\", \"\", 1734356527, \"https://www.google.com/\"]",
    "_pk_ses.100001.4cf6": "1",
    "__utma": "30149280.1809040293.1734187053.1734192732.1734356527.3",
    "__utmt_douban": "1",
    "__utmb": "30149280.2.10.1734356527",
    "report": "ref=/&from=mv_a_pst",
}

# 更新会话的 Cookie
session.cookies.update(cookies)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer": "https://www.douban.com",
}


# 获取网页内容，支持重试
def fetch_with_retry(url, params=None, retries=3):
    for attempt in range(retries):
        try:
            response = session.get(url, headers=headers, params=params, timeout=10)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"请求错误，第 {attempt + 1} 次重试...: {e}")
            time.sleep(random.uniform(5, 10))  # 增加随机延迟
    print("多次尝试后连接失败。")
    return None


# 获取电影信息
def get_movie_info(movie_name):
    # 将电影名称转换为拼音
    filename = "-".join(lazy_pinyin(movie_name)) + ".md"
    filepath = os.path.join(output_dir, filename)
    # 如果文件已存在，跳过写入
    if os.path.exists(filepath):
        print(f"文件 {filename} 已存在，跳过获取豆瓣信息。")
        return
    res_default = {
        "intro": "暂无简介",
        "actors": "暂无演员信息",
        "rating": 0,
        "english_title": ""
    }
    search_url = "https://search.douban.com/movie/subject_search"
    params = {"search_text": movie_name, "cat": "1002"}
    response = fetch_with_retry(search_url, params=params)
    if response is None:
        return res_default

    soup = BeautifulSoup(response.text, "html.parser")
    script_tag = soup.find("script", string=re.compile('window.__DATA__'))

    # 从 <script> 标签中提取 JSON 数据
    movie_urls = []
    if script_tag:
        match = re.search(r'window\.__DATA__ = ({.*?});', script_tag.string, re.DOTALL)
        if match:
            json_data = json.loads(match.group(1))
            if not json_data or not json_data['items']:
                return res_default
            # 提取电影的 URL 列表
            movie_urls = [item.get('url') for item in json_data['items']]

    if len(movie_urls) == 0:
        return res_default
    # 获取电影详情页链接
    link = movie_urls[0]
    if not link:
        return res_default
    if not link.startswith("https://movie.douban.com/subject/"):
        print(f"搜索结果中未找到有效的电影链接: {link}")
        return res_default

    time.sleep(random.uniform(2, 5))  # 随机延迟

    detail_response = fetch_with_retry(link)
    if detail_response is None:
        return res_default

    detail_soup = BeautifulSoup(detail_response.text, "html.parser")

    # 获取简介、演员和评分
    intro = detail_soup.find("span", property="v:summary")
    intro = intro.get_text(strip=True) if intro else "暂无简介"

    actors = detail_soup.find_all("a", rel="v:starring")
    actors = ", ".join([actor.get_text(strip=True) for actor in actors]) if actors else "暂无演员信息"

    rating = detail_soup.find("strong", class_="ll rating_num")
    rating = rating.get_text(strip=True) if rating else "0"

    english_title = detail_soup.find("span", property="v:itemreviewed")
    english_title = english_title.get_text(strip=True) if english_title else "Unknown Title"

    return {
        "intro": intro,
        "actors": actors,
        "rating": rating,
        "english_title": english_title
    }


# 写入 Markdown 文件
def write_markdown(movie_name, info):
    # 将电影名称转换为拼音
    filename = "-".join(lazy_pinyin(movie_name)) + ".md"
    filepath = os.path.join(output_dir, filename)

    # 如果文件已存在，跳过写入
    if os.path.exists(filepath):
        print(f"文件 {filename} 已存在，跳过写入。")
        return filename

    content = f"""# {movie_name} ({info['english_title']})

## 随笔

## 简介

{info['intro']}

## 演员

{info['actors']}

## 豆瓣评分 & 我的评分

{info['rating']} / 我的评分
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return filename


# 记录所有文件的索引
def write_index():
    index_filepath = os.path.join(output_dir, "_index.md")
    movie_infos = []

    for filename in os.listdir(output_dir):
        if filename.endswith(".md") and filename != "index.md":
            filepath = os.path.join(output_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                title_match = re.search(r'# (\S+)', content)
                rating_match = re.search(r'豆瓣评分 & 我的评分\n\n(.+) / (.+)', content)

                # 提取评分部分
                rating = 0
                if rating_match:
                    try:
                        rating = rating_match.group(1)
                        rating2 = rating_match.group(2)
                        if rating2 != "我的评分":
                            rating = rating2
                    except ValueError:
                        rating = 0

                movie_infos.append({
                    "name": title_match.group(1) if title_match else "未知电影",
                    "rating": float(rating),
                    "filename": filename
                })

    # 按评分排序
    sorted_movies = sorted(movie_infos, key=lambda x: x['rating'], reverse=True)

    with open(index_filepath, "w", encoding="utf-8") as f:
        for movie in sorted_movies:
            f.write(f"  * [{movie['name']}](dian-ying/{movie['filename']})\n")


# 主函数
def main():
    movies = []

    if not os.path.exists("目录.txt"):
        print("文件不存在！")

    with open("目录.txt", "r", encoding="utf-8") as file:
        # 按行读取并去掉可能的换行符
        movies = [line.strip() for line in file if line.strip()]
    for movie_name in movies:
        print(f"正在获取《{movie_name}》的信息")
        info = get_movie_info(movie_name)
        if info:
            filename = write_markdown(movie_name, info)
            print(f"《{movie_name}》的信息已保存到 {filename}")
        else:
            print(f"未找到《{movie_name}》的信息。")

    write_index()
    print("所有电影信息已处理完毕，索引文件已生成。")


if __name__ == "__main__":
    main()
