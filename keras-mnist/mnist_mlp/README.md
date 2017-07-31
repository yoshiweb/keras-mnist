# Keras で MNIST（多層パーセプトロン）

https://github.com/fchollet/keras/blob/master/examples/
https://github.com/fchollet/keras/blob/master/examples/mnist_mlp.py


## mnist_mlp.py

### 学習

```
$ python mnist_mlp_train.py
```

#### 結果

```
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
2017-07-31 12:10:30.362658: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.2 instructions, but these are available on your machine and could speed up CPU computations.
2017-07-31 12:10:30.362681: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX instructions, but these are available on your machine and could speed up CPU computations.
2017-07-31 12:10:30.362686: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX2 instructions, but these are available on your machine and could speed up CPU computations.
2017-07-31 12:10:30.362690: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use FMA instructions, but these are available on your machine and could speed up CPU computations.
60000/60000 [==============================] - 8s - loss: 0.2447 - acc: 0.9239 - val_loss: 0.1339 - val_acc: 0.9573
Epoch 2/20
60000/60000 [==============================] - 8s - loss: 0.1020 - acc: 0.9691 - val_loss: 0.0771 - val_acc: 0.9766
Epoch 3/20
60000/60000 [==============================] - 9s - loss: 0.0728 - acc: 0.9782 - val_loss: 0.0787 - val_acc: 0.9787
Epoch 4/20
60000/60000 [==============================] - 9s - loss: 0.0606 - acc: 0.9814 - val_loss: 0.0754 - val_acc: 0.9791
Epoch 5/20
60000/60000 [==============================] - 9s - loss: 0.0507 - acc: 0.9848 - val_loss: 0.0797 - val_acc: 0.9802
Epoch 6/20
60000/60000 [==============================] - 9s - loss: 0.0425 - acc: 0.9875 - val_loss: 0.0847 - val_acc: 0.9799
Epoch 7/20
60000/60000 [==============================] - 10s - loss: 0.0387 - acc: 0.9892 - val_loss: 0.0895 - val_acc: 0.9790
Epoch 8/20
60000/60000 [==============================] - 8s - loss: 0.0358 - acc: 0.9895 - val_loss: 0.0923 - val_acc: 0.9816
Epoch 9/20
60000/60000 [==============================] - 8s - loss: 0.0312 - acc: 0.9908 - val_loss: 0.1089 - val_acc: 0.9799
Epoch 10/20
60000/60000 [==============================] - 8s - loss: 0.0269 - acc: 0.9921 - val_loss: 0.0958 - val_acc: 0.9812
Epoch 11/20
60000/60000 [==============================] - 8s - loss: 0.0258 - acc: 0.9922 - val_loss: 0.0960 - val_acc: 0.9832
Epoch 12/20
60000/60000 [==============================] - 8s - loss: 0.0252 - acc: 0.9929 - val_loss: 0.1126 - val_acc: 0.9807
Epoch 13/20
60000/60000 [==============================] - 8s - loss: 0.0234 - acc: 0.9934 - val_loss: 0.1032 - val_acc: 0.9836
Epoch 14/20
60000/60000 [==============================] - 8s - loss: 0.0213 - acc: 0.9939 - val_loss: 0.1133 - val_acc: 0.9819
Epoch 15/20
60000/60000 [==============================] - 9s - loss: 0.0212 - acc: 0.9946 - val_loss: 0.1056 - val_acc: 0.9840
Epoch 16/20
60000/60000 [==============================] - 9s - loss: 0.0229 - acc: 0.9942 - val_loss: 0.1119 - val_acc: 0.9827
Epoch 17/20
60000/60000 [==============================] - 8s - loss: 0.0215 - acc: 0.9949 - val_loss: 0.1067 - val_acc: 0.9836
Epoch 18/20
60000/60000 [==============================] - 8s - loss: 0.0189 - acc: 0.9951 - val_loss: 0.1117 - val_acc: 0.9826
Epoch 19/20
60000/60000 [==============================] - 8s - loss: 0.0190 - acc: 0.9954 - val_loss: 0.1245 - val_acc: 0.9806
Epoch 20/20
60000/60000 [==============================] - 8s - loss: 0.0176 - acc: 0.9958 - val_loss: 0.1263 - val_acc: 0.9837
Test loss: 0.126284773826
Test accuracy: 0.9837
```

`mnist_mlp_model.h5` ファイルが生成される


### 画像を判別

```
$ python mnist_mlp_predict.py number/5.png
```

#### 結果

```
Using TensorFlow backend.
input: number/5.png
2017-07-31 12:14:01.870921: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.2 instructions, but these are available on your machine and could speed up CPU computations.
2017-07-31 12:14:01.870950: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX instructions, but these are available on your machine and could speed up CPU computations.
2017-07-31 12:14:01.870955: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX2 instructions, but these are available on your machine and could speed up CPU computations.
2017-07-31 12:14:01.870959: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use FMA instructions, but these are available on your machine and could speed up CPU computations.
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