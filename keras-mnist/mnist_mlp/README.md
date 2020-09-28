# KerasでMNIST（手書き数字画像の判別）をする　多層パーセプトロン

チュートリアルでMNISTをやっても正解率98%のような数字しか出てこないので  
実際に手書き文字画像を判別するものを作った。

- 環境：Python 3.6.1


### gitからクローンしてライブラリをインストール

```
$ git clone https://github.com/yoshiweb/keras-mnist
```


### ディレクトリに移動

```
$ cd keras-mnist/mnist_mlp
$ pip install -r requirements.txt
```


### 学習

```
$ python mnist_mlp_train.py
Using TensorFlow backend.
60000 train samples
10000 test samples
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
Train on 60000 samples, validate on 10000 samples
Epoch 1/20
2019-01-10 15:06:22.453247: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
60000/60000 [==============================] - 7s 116us/step - loss: 0.2460 - acc: 0.9231 - val_loss: 0.1019 - val_acc: 0.9675
Epoch 2/20
60000/60000 [==============================] - 7s 122us/step - loss: 0.1022 - acc: 0.9689 - val_loss: 0.0799 - val_acc: 0.9750
Epoch 3/20
60000/60000 [==============================] - 7s 116us/step - loss: 0.0750 - acc: 0.9772 - val_loss: 0.0793 - val_acc: 0.9782
Epoch 4/20
60000/60000 [==============================] - 9s 153us/step - loss: 0.0597 - acc: 0.9814 - val_loss: 0.0920 - val_acc: 0.9753
Epoch 5/20
60000/60000 [==============================] - 8s 134us/step - loss: 0.0503 - acc: 0.9849 - val_loss: 0.0695 - val_acc: 0.9825
Epoch 6/20
60000/60000 [==============================] - 7s 119us/step - loss: 0.0435 - acc: 0.9872 - val_loss: 0.0736 - val_acc: 0.9819
Epoch 7/20
60000/60000 [==============================] - 6s 103us/step - loss: 0.0377 - acc: 0.9888 - val_loss: 0.0793 - val_acc: 0.9805
Epoch 8/20
60000/60000 [==============================] - 6s 105us/step - loss: 0.0358 - acc: 0.9893 - val_loss: 0.0798 - val_acc: 0.9825
Epoch 9/20
60000/60000 [==============================] - 6s 106us/step - loss: 0.0307 - acc: 0.9913 - val_loss: 0.0883 - val_acc: 0.9819
Epoch 10/20
60000/60000 [==============================] - 7s 114us/step - loss: 0.0295 - acc: 0.9913 - val_loss: 0.0876 - val_acc: 0.9824
Epoch 11/20
60000/60000 [==============================] - 11s 191us/step - loss: 0.0270 - acc: 0.9922 - val_loss: 0.0815 - val_acc: 0.9849
Epoch 12/20
60000/60000 [==============================] - 7s 113us/step - loss: 0.0224 - acc: 0.9935 - val_loss: 0.0935 - val_acc: 0.9823
Epoch 13/20
60000/60000 [==============================] - 7s 113us/step - loss: 0.0228 - acc: 0.9935 - val_loss: 0.1019 - val_acc: 0.9811
Epoch 14/20
60000/60000 [==============================] - 6s 105us/step - loss: 0.0215 - acc: 0.9940 - val_loss: 0.1147 - val_acc: 0.9821
Epoch 15/20
60000/60000 [==============================] - 6s 104us/step - loss: 0.0209 - acc: 0.9937 - val_loss: 0.1167 - val_acc: 0.9810
Epoch 16/20
60000/60000 [==============================] - 6s 108us/step - loss: 0.0199 - acc: 0.9945 - val_loss: 0.0946 - val_acc: 0.9838
Epoch 17/20
60000/60000 [==============================] - 6s 105us/step - loss: 0.0183 - acc: 0.9952 - val_loss: 0.1133 - val_acc: 0.9823
Epoch 18/20
60000/60000 [==============================] - 7s 111us/step - loss: 0.0183 - acc: 0.9953 - val_loss: 0.1122 - val_acc: 0.9822
Epoch 19/20
60000/60000 [==============================] - 7s 119us/step - loss: 0.0182 - acc: 0.9951 - val_loss: 0.1024 - val_acc: 0.9836
Epoch 20/20
60000/60000 [==============================] - 8s 141us/step - loss: 0.0177 - acc: 0.9957 - val_loss: 0.0974 - val_acc: 0.9849
Test loss: 0.09741231448445078
Test accuracy: 0.9849
```

`mnist_mlp_model.h5` ファイルが生成される


### 画像を判別

例：引数に数字の5の画像を渡す

```
$ python mnist_mlp_predict.py number/5.png
Using TensorFlow backend.
2019-01-10 15:13:41.981085: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
5
```

