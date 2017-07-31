# Keras で MNIST（多層パーセプトロン）

https://github.com/fchollet/keras/blob/master/examples/
https://github.com/fchollet/keras/blob/master/examples/mnist_mlp.py


## mnist_mlp.py

### 学習

```
$ python mnist_mlp_train.py
```

### 判別

```
$ python mnist_mlp_predict.py number/5.png
```

> Using TensorFlow backend.
> input: number/5.png
> 2017-07-31 12:14:01.870921: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.2 instructions, but these are available on your machine and could speed up CPU computations.
> 2017-07-31 12:14:01.870950: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX instructions, but these are available on your machine and could speed up CPU computations.
> 2017-07-31 12:14:01.870955: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX2 instructions, but these are available on your machine and could speed up CPU computations.
> 2017-07-31 12:14:01.870959: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use FMA instructions, but these are available on your machine and could speed up CPU computations.
> _________________________________________________________________
> Layer (type)                 Output Shape              Param #   
> =================================================================
> dense_1 (Dense)              (None, 512)               401920    
> _________________________________________________________________
> dropout_1 (Dropout)          (None, 512)               0         
> _________________________________________________________________
> dense_2 (Dense)              (None, 512)               262656    
> _________________________________________________________________
> dropout_2 (Dropout)          (None, 512)               0         
> _________________________________________________________________
> dense_3 (Dense)              (None, 10)                5130      
> =================================================================
> Total params: 669,706
> Trainable params: 669,706
> Non-trainable params: 0
> _________________________________________________________________
> [[ 0.  0.  0.  0.  0.  1.  0.  0.  0.  0.]]
> 5