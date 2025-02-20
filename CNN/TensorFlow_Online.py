import tensorflow as tf
 
class myCallback(tf.keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs={}):
    if(logs.get('accuracy')>0.9999):
      print("\nReached 99% accuracy so cancelling training!")
      self.model.stop_training = True
 
mnist = tf.keras.datasets.mnist
 
(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
 
callbacks = myCallback()
 
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(5120, activation=tf.nn.relu),
  tf.keras.layers.Dense(1000, activation=tf.nn.softmax)
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
 
model.fit(x_train, y_train, epochs=10, callbacks=[callbacks])
