import sys
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

# 画像サイズ
img_height = 28
img_width = 28

if len(sys.argv) != 2:
    print("引数に判別する画像のパスを記載してください")
    sys.exit(1)

filename = sys.argv[1]
print('input:', filename)


# 画像を読み込む
img = image.load_img(filename, target_size=(img_height, img_width), color_mode='grayscale')
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)

# 白黒反転（黒背景に白文字）
x = 255 - x

# 1次元へ変換 
# x = x.reshape(-1, 784)

# モデル読み込み
model = load_model('mnist_cnn_model.h5')
model.summary()

# 学習したモデルに対して予測を行う
y = model.predict(x)

# 予測結果を出力
print(y)
print( np.argmax(y[0]) )
