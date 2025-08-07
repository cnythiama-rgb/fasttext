import os
from datasets import load_dataset
from tqdm import tqdm
import json

def save_jsonl(dataset, out_path, max_bytes=100*1024*1024):
    total_bytes = 0
    with open(out_path, 'w', encoding='utf-8') as f:
        for item in tqdm(dataset, desc=f"Writing to {out_path}"):
            text = item.get('text', '').replace('\n', ' ').strip()
            if not text:
                continue
            line = json.dumps({'text': text}, ensure_ascii=False)
            line_bytes = len(line.encode('utf-8')) + 1  # +1 for newline
            if total_bytes + line_bytes > max_bytes:
                break
            f.write(line + '\n')
            total_bytes += line_bytes

def main():
    os.makedirs('data', exist_ok=True)

    # 下载 openwebmath
    print("Downloading openwebmath...")
    openwebmath = load_dataset("open-web-math/open-web-math", split="train", streaming=True)
    save_jsonl(openwebmath, "data/openwebmath_sample.jsonl", max_bytes=100*1024*1024)

    # 下载 fineweb
    print("Downloading fineweb...")
    fineweb = load_dataset("HuggingFaceFW/fineweb", split="train", streaming=True)
    save_jsonl(fineweb, "data/fineweb_sample.jsonl", max_bytes=100*1024*1024)

    print("数据下载与采样完成！")

if __name__ == "__main__":
    main()