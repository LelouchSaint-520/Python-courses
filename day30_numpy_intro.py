import numpy as np
import time

size = 1_000_000_000
python_list = list(range(size))
numpy_array = np.array(python_list)

start_time = time.time()
result_list = []
for item in python_list:
    result_list.append(item*2)
end_time = time.time()
print(f"Python list cost :{end_time - start_time:.6f} sec.")

start_time = time.time()
result_array = numpy_array*2
end_time = time.time()
print(f"Numpy array cost :{end_time - start_time:.6f} sec.")