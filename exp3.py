import numpy as np

def find_common(first, last):
	global search_buffer, look_ahead_buffer, sample_string, sample_string_array, encoded_string
	for i in range(search_buffer_size-1):
		for j in range(1,search_buffer_size):
			print("Comparing {} with {}".format(search_buffer[i:j], look_ahead_buffer[first:last]))
			if(np.array_equal(search_buffer[i:j+1], look_ahead_buffer[first:last])):
				iteration = (j, i-j, search_buffer[-1])
				search_buffer = np.insert(search_buffer, j, look_ahead_buffer[i:j+1])
				print(search_buffer)
				return iteration

			else:
				search_buffer = np.append(search_buffer, look_ahead_buffer[0])
				encoded_string = np.append(encoded_string, search_buffer[0])
				search_buffer = search_buffer[1:]
				look_ahead_buffer = look_ahead_buffer[1:]
				look_ahead_buffer = np.append(look_ahead_buffer, sample_string_array[0])
				sample_string_array = sample_string_array[1:]
				print("{}||{}".format(search_buffer, look_ahead_buffer))
				return (0, 0, search_buffer[search_buffer_size])

encoded_string = []
encoded_string = np.array(encoded_string)
sample_string = "a,b,c,a,b,c,d,a,b,c,d,e,a,b,c,d,e,f"
sample_string_array = sample_string.split(",")
sample_string_array = np.array(sample_string_array)
window_size = int(input("Enter window size: "))
look_ahead_buffer_size = int(input("Enter look ahead buffer size: "))
search_buffer_size = window_size - look_ahead_buffer_size
iterations = []
search_buffer = [None] * search_buffer_size
look_ahead_buffer = []

#for i in range(search_buffer_size):
	#search_buffer.append('-')

for i in range(look_ahead_buffer_size):
	look_ahead_buffer.append(sample_string_array[i])

look_ahead_buffer = np.array(look_ahead_buffer)
search_buffer = np.array(search_buffer)

print("{}||{}".format(search_buffer, look_ahead_buffer))

for i in range(look_ahead_buffer_size):
	look_ahead_buffer = np.insert(look_ahead_buffer, i, sample_string_array[i])

sample_string_array = sample_string_array[look_ahead_buffer_size+1:]

for i in range(look_ahead_buffer_size):
	print("Calling find_common function")
	iteration = find_common(i, j)
	iterations.append(iteration)

for each in iterations:
	if each == "Not found":
		iterations.remove(each)
print(iterations)

print("Encoded string:", encoded_string)