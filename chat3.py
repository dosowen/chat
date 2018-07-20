lines = []
with open('C:/Users/DOS/Desktop/coding/chat/3.txt','r',encoding = 'utf-8-sig')as f:
	for line in f:
		s = line.strip().split(' ')
		lines.append(s)  
		# print(s)
		time = s[0] [:5]
		print(time)
		name = s[0] [5:]
		print(name)