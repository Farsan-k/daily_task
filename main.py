import numpy as np


stride = 1

image = np.array([
    [1,2,3,1,0],
    [0,1,2,3,1],
    [1,2,0,3,0],
    [1,2,0,3,0],
    [1,0,3,2,1]
])

kernel =  np.array([
    [1,0,1],
    [0,1,0],
    [1,0,1]
])

image_h, image_w = image.shape

k = kernel.shape[0]

output_h = (image_h - k) + 1 // stride
output_w = (image_w - k) + 1 // stride


output = np.zeros(
    [output_h,
     output_w]
)

for i in range(output_h):
  for j in range(output_w):
    region = image[
        i * stride : i * stride + k,
        j * stride : j * stride + k
    ]

    output[i,j] = np.sum(region * kernel)

print(output)