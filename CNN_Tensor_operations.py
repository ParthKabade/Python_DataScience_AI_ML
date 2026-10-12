import tensorflow as tf

tensor1 =tf.constant([10,20,30])
tensor2=tf.constant([1,2,3])

addition=tf.add(tensor1,tensor2)
print("Addition is : ",addition)

substraction=tf.subtract(tensor1,tensor2)
print("substraction is : ",substraction)

multiply=tf.multiply(tensor1,tensor2)
print("multiply is : ",multiply)

divide=tf.divide(tensor1,tensor2)
print("divide is : ",divide)

square=tf.square(tensor1,tensor2)
print("square is : ",square)

sum=tf.reduce_sum(tensor1)
print("reduce sum is : ",sum)

Mean=tf.reduce_mean(tensor1)
print("reduce Mean is : ",Mean)