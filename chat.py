def read():
	chat = []
	with open ('C:/Users/DOS/Desktop/coding/input.txt', 'r',encoding = 'utf-8-sig') as f:
		for line in f:
			chat.append(line.strip())
		print(chat)
		return chat

def convert(chat):
	new = []
	person = None
	for line in chat:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		new.append(person + ': ' + line)
	print(new)
	return new

def write_file(new):
	with open ('output.txt','w',encoding = 'utf-8-sig')as f:
		for line in new:
			f.write(line + '\n')

def main():
	chat = read()
	new = convert(chat)
	write_file(new)

main()