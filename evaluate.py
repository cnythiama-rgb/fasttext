import fasttext

def main():
    model = fasttext.load_model('models/model.bin')
    result = model.test('data/valid.txt')
    print(f"验证集样本数: {result[0]}")
    print(f"准确率: {result[1]:.4f}")
    print(f"召回率: {result[2]:.4f}")

if __name__ == '__main__':
    main()


