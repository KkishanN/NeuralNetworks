import sys
import numpy as np


inputs = [1,2,3, 2.5]
weights1 = [.2,.8,-.5, 1]
weights2 = [.5,-.91,.26, -.5]
weights3 = [-.26, -.27, .17, .87]

bias1 = 2
bias2 = 3
bias3 = .5


output = [inputs[0] * weights1[0] + inputs[1] * weights1[1] + inputs[2] * weights2[2] + bias1,
          inputs[0] * weights2[0] + inputs[1] * weights2[1] + inputs[2] * weights2[2] + bias1,
          inputs[0] * weights3[0] + inputs[1] * weights3[1] + inputs[2] * weights2[2] + bias1]

print(output)