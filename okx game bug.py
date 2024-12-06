import json
import time
import random
import requests

def generate_data(total_entries, min_repeats=1, max_repeats=5):
    # 此函数保持不变
    generated_data = []
    current_time = int(time.time() * 1000)
    start_time = current_time
    remaining_entries = total_entries
    while remaining_entries > 0:
        repeats = random.randint(min_repeats, max_repeats)
        if repeats > remaining_entries:
            repeats = remaining_entries
        for _ in range(repeats):
            entry = {"b": 2, "t": start_time}
            generated_data.append(entry)
            start_time += random.randint(1, 500)
        remaining_entries -= repeats
    generated_data[-1]["t"] = current_time
    generated_data[0]["b"] = 1
    generated_data[-1]["b"] = 4
    return generated_data


def register(email, name):
    url = "https://case.ruiccm.com/2024/okx/app/api.php?op=info"
    headers = {
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
    }
    data = {
        "name": name,
        "email": email,
        "identity": 3,
        "op": "info"
    }
    resp = requests.post(url, headers=headers, data=data)
    if resp.status_code == 200:
        print(resp.content.decode())


def send(email, total_entries, score, name):
    url = "https://case.ruiccm.com/2024/okx/app/api.php?op=game"
    headers = {
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
    }
    data = {
        "email": email,
        "score": score,
        "fh": 0,
        "vd": 0,
        "log": generate_data(total_entries),
        "op": "game"
    }
    resp = requests.post(url, headers=headers, data=data)
    if resp.status_code == 200:
        print(resp.content.decode())


if __name__ == '__main__':
    email = input("请输入你的邮箱地址: ")
    total_entries = int(input("请输入总的条目数: "))
    score = int(input("请输入分数: "))
    name = input("请输入你的名字: ")
    send(email, total_entries, score, name)
