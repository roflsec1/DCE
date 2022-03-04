#https://github.com/roflsec1/DCE/blob/main/exp2.py
#HUFFMAN CODING
import math

string1 = "ABBCCCDDDD" 
print("Sample string: {}".format(string1))
frequency = {}
sorted_by_probability = {}
entropy = 0

class NodeTree:
	def __init__(self, left=None, right=None): #constructor
		self.left = left
		self.right = right
		
	def children(self):
		return(self.left, self.right)
		
	def all_nodes(self):
		return(self.left, self.right)
		
	def __str__(self):
		return "{}-{}".format(self.left, self.right)
		
def huffman_tree(node, left=True, binary=''):
	if type(node) is str:
		return {node:binary}
	(l, r) = node.children()
	dictionary = dict()
	dictionary.update(huffman_tree(l, True, binary + '0'))
	dictionary.update(huffman_tree(r, False, binary + '1'))
	return dictionary

for i in string1: #calculate frequency
	if i not in frequency:
		frequency[i]=1
	else:
		frequency[i]+=1

sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True) #sort by value, x[0] for sort by key

for i in range(len(sorted_frequency)): #calculate average
	(key, value) = sorted_frequency[i]
	sorted_by_probability[key] = round(value/len(string1), 2)

print(sorted_by_probability)

for i in sorted_by_probability: #calculate entropy
	entropy+=math.log(1/sorted_by_probability[i])

all_nodes = sorted_frequency #list of tuples

while len(all_nodes) > 1:
	(key1, value1) = all_nodes[-1] #key = data element, value = frequency of respective data element.
	(key2, value2) = all_nodes[-2] #same
	all_nodes = all_nodes[:-2] #crop out the remaining key-value pairs
	node = NodeTree(key1, key2) #instantiate object
	all_nodes.append((node, value1+value2)) #and re-add
	all_nodes = sorted(all_nodes, key=lambda x: x[1], reverse=True) #sort by value again
	
huff_code = huffman_tree(all_nodes[0][0])

print("Entropy = {:.2f}".format(entropy))
print("Tree: ", huff_code)
print("|Character\t|Frequency\t|Code\t|Size")
character = []
freq = []
code = []
size = []

for i in huff_code: #make a list of character and code
	character.append(i)
	code.append(huff_code[i])

for i,j in sorted_frequency: #make a list of frequency
	freq.append(j)

for i in range(len(huff_code)): #calculate and make a list of size
	size.append(len(code[i])*freq[i])
	
for i in range(len(huff_code)):
	print(" {}\t\t {}\t\t {}\t {}".format(character[i],freq[i],code[i],size[i]))

