import fasttext
import os

def main():
    os.makedirs('models', exist_ok=True)
    model = fasttext.train_supervised(input='data/train.txt', epoch=10, lr=0.5, wordNgrams=2, verbose=2)
    model.save_model('models/model.bin')
    print('模型训练完成，已保存到 models/model.bin')

if __name__ == '__main__':
    main()


