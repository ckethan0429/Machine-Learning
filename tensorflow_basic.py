#virtualenv 활성화 시키기 : source ~/tensorflow/bin/activate
#비활성화 : deactivate

import tensorflow as tf

h = tf.constant("hello")
w = tf.constant(" world")
hw = h + w
print(hw)

with tf.Session() as sess:
    ans = sess.run(hw)

print(ans)