# Keras で MNIST（畳み込みニューラルネットワーク）

https://github.com/fchollet/keras/blob/master/examples/
https://github.com/fchollet/keras/blob/master/examples/mnist_cnn.py


## mnist_cnn.py

### 学習

```
$ python mnist_cnn_train.py
```

#### 結果  

```
Using TensorFlow backend.
x_train shape: (60000, 28, 28, 1)
60000 train samples
10000 test samples
Train on 60000 samples, validate on 10000 samples
Epoch 1/12
2017-07-31 12:16:36.365297: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.2 instructions, but these are available on your machine and could speed up CPU computations.
2017-07-31 12:16:36.365320: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX instructions, but these are available on your machine and could speed up CPU computations.
2017-07-31 12:16:36.365328: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX2 instructions, but these are available on your machine and could speed up CPU computations.
2017-07-31 12:16:36.365334: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use FMA instructions, but these are available on your machine and could speed up CPU computations.
60000/60000 [==============================] - 187s - loss: 0.3242 - acc: 0.9002 - val_loss: 0.0788 - val_acc: 0.9751
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

```
$ python mnist_cnn_predict.py number/5.png
```

#### 結果

```
Using TensorFlow backend.
input: number/5.png
2017-07-31 13:26:10.173888: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.2 instructions, but these are available on your machine and could speed up CPU computations.
2017-07-31 13:26:10.173914: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX instructions, but these are available on your machine and could speed up CPU computations.
2017-07-31 13:26:10.173918: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX2 instructions, but these are available on your machine and could speed up CPU computations.
2017-07-31 13:26:10.173922: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use FMA instructions, but these are available on your machine and could speed up CPU computations.
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 26, 26, 32)        320       
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 24, 24, 64)        18496     
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 12, 12, 64)        0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 12, 12, 64)        0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 9216)              0         
_________________________________________________________________
dense_1 (Dense)              (None, 128)               1179776   
_________________________________________________________________
dropout_2 (Dropout)          (None, 128)               0         
_________________________________________________________________
dense_2 (Dense)              (None, 10)                1290      
=================================================================
Total params: 1,199,882
Trainable params: 1,199,882
Non-trainable params: 0
_________________________________________________________________
[[ 0.  0.  0.  0.  0.  1.  0.  0.  0.  0.]]
5
```