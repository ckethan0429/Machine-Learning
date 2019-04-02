import tensorflow as tf
import numpy as np

#데이터생성하고 결과를 시뮬레이션
x_data = np.random.randn(2000, 3)
w_real = [0.3, 0.5, 0.1]
b_real = -0.2

noise = np.random.randn(1,2000) * 0.1
y_data = np.matmul(w_real, x_data.T) + b_real + noise

print(x_data.shape, y_data.shape)

wb_ = [] #직접 연산에는 참여안함

x = tf.placeholder(tf.float32, shape=[None, 3])
y_true = tf.placeholder(tf.float32, shape = None)

w = tf.Variable([[0,0,0]], dtype = tf.float32)
b = tf.Variable(0, dtype = tf.float32)
y_pred = tf.matmul(w, tf.transpose(x)) +b

loss = tf.reduce_mean(tf.square(y_true - y_pred))

optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

NUM_STEPS =10

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for step in range(NUM_STEPS):
        sess.run(train, {x: x_data, y_true: y_data})
        if(step%5 ==0):
            print(step, sess.run([w,b]))
            wb_.append(sess.run([w,b]))
            
    print(10, sess.run([w,b]))