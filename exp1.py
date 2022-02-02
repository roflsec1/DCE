x = [9, 11, 11, 11, 14, 13, 15, 17, 16, 17, 20, 21]
x_cap_n = []
en = []
er = []
de = []
received_nocorrect = []
received_data = []
for i in range(0, len(x)):
	x_cap_n.append((i + 1) + x[0]-1)
	
for i in range(0, len(x)):
	en.append(x[i] - x_cap_n[i])
	
print(x_cap_n)
print(en)

for i in en: #encoding
	if i==0:
		er.append("00")
	elif i==1:
		er.append("10")
	else:
		er.append("01")

print("".join(er))

#################################################################

for i in er: #decoding
	if i=="00":
		de.append(0)
	elif i=="10":
		de.append(1)
	else:
		de.append(-1)

print(de)

for i in range(0, len(de)):
	received_nocorrect.append((i + x[0]))
	
print(received_nocorrect)

for i in range(0, len(received_nocorrect)):
	received_data.append(de[i] + received_nocorrect[i])
