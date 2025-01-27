import requests
from bs4 import BeautifulSoup
import subprocess
import json
# import os

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def fetch_salmon(url, salmons):
    try:
        res = ''
        response = requests.get(url,headers=headers)
        response.encoding = 'utf-8'  # 设置编码为 UTF-8
        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.find_all("table")  # 找到所有表格
        index = 0
        length = len(salmons)
        for table in tables:
            if index >= length:
                break
            res +='<p>'+salmons[index]+': </p>'
            res += table.prettify()
            index+=1
        return res
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except Exception as e:
        print(f"Error parsing data: {e}")
        return None

def main():
    url = "https://wikiwiki.jp/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/"
    html = "<head><meta charset=\"UTF-8\"><style>table{border-collapse: collapse;border: 1px solid black;margin:10px;}td, th {border: 1px solid black;}</style></head>"
    ザコシャケ = {"ザコシャケ":['コジャケ','シャケ','シャケ（ラッシュ）','ドスコイ','タマヒロイ']}
    ハコビヤたち = {"ハコビヤたち":['シャケコプター', 'ハコビヤ母艦']}
    オオモノシャケ = ['バクダン','ヘビ','テッパン','タワー','モグラ','コウモリ','カタパッド','ハシラ','ダイバー','ナベブタ','テッキュウ']
    特殊な状況でのみ出現する特殊なシャケ =['キンシャケ','グリル','ドロシャケ']
    Extra_Waveでのみ出現するオカシラシャケ = ['ヨコヅナ','タツ','ジョー']
    for key,value in ザコシャケ.items():
        html+=fetch_salmon(url+key,value)
    for salmon in オオモノシャケ:
        html+=fetch_salmon(url+salmon,[salmon])
    for salmon in 特殊な状況でのみ出現する特殊なシャケ:
        html+=fetch_salmon(url+salmon,[salmon])
    for key,value in ハコビヤたち.items():
        html+=fetch_salmon(url+key,value)
    for salmon in Extra_Waveでのみ出現するオカシラシャケ:
        html+=fetch_salmon(url+salmon,[salmon])
    with open("salmon.html", "w", encoding="utf-8") as file:
        file.write(html)    

if __name__ == "__main__":
    main()