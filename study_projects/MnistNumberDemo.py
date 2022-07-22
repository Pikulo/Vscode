#手写数字识别，自定义训练测试
import tensorflow as tf
import matplotlib.pyplot as plt

(train_image, train_labels), (test_image, test_labels) = tf.keras.datasets.mnist.load_data()
train_image = tf.expand_dims(train_image, -1)   #扩展维度
test_image = tf.expand_dims(test_image, -1)   
train_image = tf.cast(train_image/255, tf.float32)
test_image = tf.cast(test_image/255, tf.float32)
train_labels = tf.cast(train_labels, tf.int64)
test_labels = tf.cast(test_labels, tf.int64)
dataset = tf.data.Dataset.from_tensor_slices((train_image, train_labels))
test_dataset = tf.data.Dataset.from_tensor_slices((test_image, test_labels))

BATCH_SIZE = 32
AUTOTUNE = tf.data.experimental.AUTOTUNE
dataset = dataset.shuffle(10000).repeat().batch(BATCH_SIZE).prefetch(AUTOTUNE)
test_dataset = test_dataset.batch(BATCH_SIZE).prefetch(AUTOTUNE)



model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(64, (3, 3), input_shape=(28, 28, 1), activation='relu',padding='same'),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu',padding='same'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu',padding='same'),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu',padding='same'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(256, (3, 3), activation='relu',padding='same'),
    tf.keras.layers.Conv2D(256, (3, 3), activation='relu',padding='same'),
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])
model.summary()

model.compile(tf.keras.optimizers.Adam(lr=0.001),loss='sparse_categorical_crossentropy',metrics=['acc'])
steps_per_epoch = len(train_image)//BATCH_SIZE
validation_steps = len(test_image)//BATCH_SIZE
model.fit(dataset, epochs=10, steps_per_epoch=steps_per_epoch, validation_data=test_dataset, validation_steps=validation_steps)


#预测一张图片
predict=new_model.predict(tf.reshape(test_image[0],[1,28,28,1]))
np.argmax(predict[0])

