# FastText 数学文本分类器

本项目基于 FastText 实现数学领域文本的自动筛选，正样本来自 openwebmath，负样本来自 fineweb。可用于从大规模 Web 文本中筛选数学相关内容。

## 目录结构

```
├── scripts/
│   ├── prepare_data.py
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
├── requirements.txt
├── README.md
```

## 依赖安装

```bash
pip install -r requirements.txt
```
```

## 数据准备

1. 下载 openwebmath 和 fineweb 的部分数据，分别保存为 `data/openwebmath_sample.jsonl` 和 `data/fineweb_sample.jsonl`。
2. 运行数据处理脚本，生成 FastText 格式的训练/验证集：

```bash
python scripts/prepare_data.py
```

## 训练模型

```bash
python scripts/train.py
```
模型将保存为 `model.bin`。

## 评估模型

```bash
python scripts/evaluate.py
```
将输出验证集上的准确率、召回率等。

## 预测与打标

将 5000 条 fineweb 文本保存为 `data/fineweb_5000.txt`，每行一条。

```bash
python scripts/predict.py
```
打标结果输出到 `results/fineweb_5000_labeled.txt`，每行为：
```
__label__math	概率	原始文本
__label__other	概率	原始文本
```

## 评测流程说明

- **数据处理**：采样 openwebmath 作为正样本，fineweb 作为负样本，转换为 FastText 格式，划分训练/验证集。
- **训练**：用 FastText 训练二分类模型。
- **评估**：在验证集上评估分类效果。
- **打标**：用训练好的模型对 fineweb 5000 条文本进行打标。

## 参考
- [FastText 官方文档](https://fasttext.cc/docs/en/supervised-tutorial.html)
- [openwebmath 数据集](https://huggingface.co/datasets/open-web-math/open-web-math)
- [fineweb 数据集](https://huggingface.co/datasets/HuggingFaceFW/fineweb)



