import tensorflow as tf

#scaler tensor(0D tensor)
scalar_tensor=tf.constant(11)
print("Scaler Tensor :",scalar_tensor)

#1D Tensor(Vector)
vextor_tensor=tf.constant([11,21,51,101])
print("Vector tensor :",vextor_tensor)

#2D Tensor (Matrix)
matrix_tensor=tf.constant([[10,20,30],[40,50,60]])
print("matrix tensor :",matrix_tensor)

#3D Tensor 
tensor_3D=tf.constant([
    [[1,2],[3,4]],
    [[5,5],[6,6]],
    [[7,8],[9,10]]
    ])

print("3D tensor :",tensor_3D)