import numpy as np

stried = 1

image = np.array([
    [1,2,3,0,1],
    [1,2,2,0,1],
    [2,1,3,1,2],
    [3,2,1,1,0],
    [0,2,1,3,1]
])

kernel = np.array([
    [1,0,1],
    [0,1,0],
    [1,0,1],
])

image_h, image_w = image.shape

k = kernel.shape[0]

output_h = ((image_h - k) // stried) + 1
output_w = ((image_w - k) // stried) + 1

output = np.zeros(
    [output_h,
     output_w]
)

for i in range(output_h):
    for j in range(output_w):
        region = image[
            i * stried : i * stried + k,
            j * stried : j * stried + k
        ]

        output[i,j] = np.sum(region * kernel)

print(output)