import json
import random
import os
from tqdm import tqdm

def sample_jsonl(input_path, output_path, sample_size):
    lines = []
    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            lines.append(line.strip())
    sampled = random.sample(lines, min(sample_size, len(lines)))
    with open(output_path, 'w', encoding='utf-8') as f:
        for line in sampled:
            f.write(line + '\n')

def convert_to_fasttext(jsonl_path, label, out_path):
    with open(jsonl_path, 'r', encoding='utf-8') as f, open(out_path, 'w', encoding='utf-8') as out:
        for line in f:
            try:
                data = json.loads(line)
                text = data.get('text', '').replace('\n', ' ').strip()
                if text:
                    out.write(f"__label__{label} {text}\n")
            except Exception:
                continue

def split_train_valid(pos_path, neg_path, train_path, valid_path, valid_ratio=0.1):
    with open(pos_path, 'r', encoding='utf-8') as f:
        pos_lines = f.readlines()
    with open(neg_path, 'r', encoding='utf-8') as f:
        neg_lines = f.readlines()
    all_lines = pos_lines + neg_lines
    random.shuffle(all_lines)
    valid_size = int(len(all_lines) * valid_ratio)
    valid_lines = all_lines[:valid_size]
    train_lines = all_lines[valid_size:]
    with open(train_path, 'w', encoding='utf-8') as f:
        f.writelines(train_lines)
    with open(valid_path, 'w', encoding='utf-8') as f:
        f.writelines(valid_lines)

def main():
    os.makedirs('data', exist_ok=True)
    # 采样数量可根据实际情况调整
    pos_sample = 10000
    neg_sample = 10000
    sample_jsonl('data/openwebmath_sample.jsonl', 'data/openwebmath_sampled.jsonl', pos_sample)
    sample_jsonl('data/fineweb_sample.jsonl', 'data/fineweb_sampled.jsonl', neg_sample)
    convert_to_fasttext('data/openwebmath_sampled.jsonl', 'math', 'data/pos.txt')
    convert_to_fasttext('data/fineweb_sampled.jsonl', 'other', 'data/neg.txt')
    split_train_valid('data/pos.txt', 'data/neg.txt', 'data/train.txt', 'data/valid.txt')
    print('数据处理完成！')

if __name__ == '__main__':
    main()



