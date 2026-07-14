import numpy as np

image = np.array([
    [2,5,1,4],
    [3,8,6,7],
    [0,2,9,5],
    [4,1,3,8]
])

stride = 2
pool_size = 2

output_h = (image.shape[0] - pool_size) // stride + 1
output_w = (image.shape[1] - pool_size) // stride + 1

output = np.zeros(
    [output_h,
     output_w]
)

for i in range(output_h):
    for j in range(output_w):
        row = i * stride
        col = j * stride

        window = image[row: row + pool_size, col: col + pool_size]
        output[i,j] = np.max(window)

print('Output:', output)