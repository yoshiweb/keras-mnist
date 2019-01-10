# KerasでMNIST（手書き数字画像の判別）をする　畳み込みニューラルネットワーク

チュートリアルでMNISTをやっても正解率98%のような数字しか出てこないので  
実際に手書き文字画像を判別するものを作った。


### gitからクローンしてライブラリをインストール

```
$ git clone https://github.com/yoshiweb/keras-mnist
$ cd keras-mnist
$ pip install -r requirements.txt
```


### ディレクトリに移動

```
$ cd keras-mnist/mnist_cnn
```


### 学習

```
$ python mnist_cnn_train.py
Using TensorFlow backend.
x_train shape: (60000, 28, 28, 1)
60000 train samples
10000 test samples
Train on 60000 samples, validate on 10000 samples
2019-01-10 15:16:28.304051: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
Epoch 1/12
60000/60000 [==============================] - 186s 3ms/step - loss: 0.2707 - acc: 0.9164 - val_loss: 0.0574 - val_acc: 0.9810
Epoch 2/12
60000/60000 [==============================] - 172s - loss: 0.1107 - acc: 0.9667 - val_loss: 0.0604 - val_acc: 0.9791
Epoch 3/12
60000/60000 [==============================] - 172s - loss: 0.0860 - acc: 0.9745 - val_loss: 0.0446 - val_acc: 0.9844
Epoch 4/12
60000/60000 [==============================] - 172s - loss: 0.0711 - acc: 0.9783 - val_loss: 0.0382 - val_acc: 0.9868
Epoch 5/12
60000/60000 [==============================] - 172s - loss: 0.0628 - acc: 0.9815 - val_loss: 0.0368 - val_acc: 0.9877
Epoch 6/12
60000/60000 [==============================] - 173s - loss: 0.0552 - acc: 0.9830 - val_loss: 0.0346 - val_acc: 0.9887
Epoch 7/12
60000/60000 [==============================] - 173s - loss: 0.0500 - acc: 0.9852 - val_loss: 0.0313 - val_acc: 0.9888
Epoch 8/12
60000/60000 [==============================] - 174s - loss: 0.0468 - acc: 0.9859 - val_loss: 0.0332 - val_acc: 0.9889
Epoch 9/12
60000/60000 [==============================] - 173s - loss: 0.0433 - acc: 0.9870 - val_loss: 0.0315 - val_acc: 0.9896
Epoch 10/12
60000/60000 [==============================] - 173s - loss: 0.0418 - acc: 0.9880 - val_loss: 0.0308 - val_acc: 0.9895
Epoch 11/12
60000/60000 [==============================] - 173s - loss: 0.0390 - acc: 0.9884 - val_loss: 0.0294 - val_acc: 0.9900
Epoch 12/12
60000/60000 [==============================] - 173s - loss: 0.0375 - acc: 0.9889 - val_loss: 0.0301 - val_acc: 0.9895
Test loss: 0.030060273105
Test accuracy: 0.9895
```

`mnist_cnn_model.h5` ファイルが生成される


### 画像を判別

例：引数に数字の5の画像を渡す

```
$ python mnist_cnn_predict.py number/5.png
Using TensorFlow backend.
2019-01-10 15:19:54.419785: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
5
```

