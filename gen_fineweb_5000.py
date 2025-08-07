import json

input_path = 'data/fineweb_sample.jsonl'
output_path = 'data/fineweb_5000.txt'
max_lines = 5000

with open(input_path, 'r', encoding='utf-8') as fin, open(output_path, 'w', encoding='utf-8') as fout:
    count = 0
    for line in fin:
        if count >= max_lines:
            break
        try:
            data = json.loads(line)
            text = data.get('text', '').replace('\n', ' ').strip()
            if text:
                fout.write(text + '\n')
                count += 1
        except Exception:
            continue

print(f'已生成 {output_path}，共 {count} 条。')