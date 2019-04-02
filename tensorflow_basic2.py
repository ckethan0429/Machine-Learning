import tensorflow as tf

a = tf.constant(5)
b = tf.constant(2)
c = tf.constant(3)

d = tf.multiply(a,b) # d = a*b
e = tf.add(c,b) # e = c+d
f = tf.subtract(d,e) #f = d-e

sess = tf.Session() #연산그래프 실행을 위한 인터페이스
outs = sess.run(f) #연산그래프 실행 , 연산그래프 노드를 매개변수로 가짐, 연산결과를 리턴
sess.close()
print("out ={}".format(outs))
