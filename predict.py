import fasttext
import os

def main():
    model = fasttext.load_model('models/model.bin')
    os.makedirs('results', exist_ok=True)
    with open('data/fineweb_5000.txt', 'r', encoding='utf-8') as fin, \
         open('results/fineweb_5000_labeled.txt', 'w', encoding='utf-8') as fout:
        for line in fin:
            text = line.strip()
            if not text:
                continue
            label, prob = model.predict(text)
            fout.write(f"{label[0]}\t{prob[0]:.4f}\t{text}\n")
    print('打标完成，结果已保存到 results/fineweb_5000_labeled.txt')

if __name__ == '__main__':
    main()


