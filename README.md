# Keras で MNIST を試す

チュートリアルでMNISTをやっても正解率98%のような数字しか出てこないので  
実際に手書き文字画像を判別するものを作って試してみた。

- [Keras で MNIST（多層パーセプトロン）](keras-mnist/mnist_mlp)
- [Keras で MNIST（畳み込みニューラルネットワーク）](keras-mnist/mnist_cnn)

## 環境

- Python 3.6.1
- Keras 2.0.6
- Tensorflow 1.2.1

## 使い方

### gitからクローンしてライブラリをインストール

```
$ git clone https://github.com/yoshiweb/keras-mnist
$ cd keras-mnist
$ pip install -r requirements.txt
```

### ディレクトリに移動して実行

例）手書き文字の画像（数字の5）を判別

```
$ cd keras-mnist/mnist_mlp
$ python mnist_mlp_predict.py number/5.png
```

出力

```
Using TensorFlow backend.
input: number/5.png
2017-08-01 10:24:31.467366: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.2 instructions, but these are available on your machine and could speed up CPU computations.
2017-08-01 10:24:31.467392: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX instructions, but these are available on your machine and could speed up CPU computations.
2017-08-01 10:24:31.467397: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX2 instructions, but these are available on your machine and could speed up CPU computations.
2017-08-01 10:24:31.467401: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use FMA instructions, but these are available on your machine and could speed up CPU computations.
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense_1 (Dense)              (None, 512)               401920    
_________________________________________________________________
dropout_1 (Dropout)          (None, 512)               0         
_________________________________________________________________
dense_2 (Dense)              (None, 512)               262656    
_________________________________________________________________
dropout_2 (Dropout)          (None, 512)               0         
_________________________________________________________________
dense_3 (Dense)              (None, 10)                5130      
=================================================================
Total params: 669,706
Trainable params: 669,706
Non-trainable params: 0
_________________________________________________________________
[[ 0.  0.  0.  0.  0.  1.  0.  0.  0.  0.]]
5
```