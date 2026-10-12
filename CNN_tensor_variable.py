import tensorflow as tf

weight=tf.Variable(5.0)

print("Initial weight value :",weight.numpy())

weight.assign(10.0)
print("Updated weight :",weight.numpy())