def read():
	chat = []
	with open ('C:/Users/DOS/Desktop/coding/chat/-LINE-Viki.txt', 'r',encoding = 'utf-8-sig') as f:
		for line in f:
			chat.append(line.strip())
		# print(chat)
		return chat

def convert(chat):
	picture_total3 = []
	picture3 = 0
	picture_total4 = []
	picture4 = 0
	picture_total= []
	picture1 = 0
	picture2_total = []
	picture2 = 0
	Allen_total = []
	VIki_total = []
	Allen_word = 0
	VIki_word = 0
	for line in chat:
		s = line.split(' ')
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				picture1 = 1
				picture_total.append(picture1)
				picture1 = 0
				continue
			elif s[2] == '圖片':
				picture3 = 1
				picture_total3.append(picture3)
				picture3 = 0
				continue
			for m in s[2:]:
				Allen_word += len(m)
				Allen_total.append(Allen_word)
				Allen_word = 0

		elif name == 'Viki':
			if s[2] == '貼圖':
				picture2 = 1
				picture2_total.append(picture2)
				picture2 = 0
				continue
			elif s[2] == '圖片':
				picture4 = 1
				picture_total4.append(picture4)
				picture4 = 0
				continue
			for m2 in s[2:]:
				VIki_word += len(m2)
				VIki_total.append(VIki_word)
				VIki_word = 0
	Allen_total = sum(Allen_total)
	print('it has',Allen_total,'word Allen said')
	VIki_total = sum(VIki_total)
	print('it has',VIki_total,'word Viki said')
	picture_total = sum(picture_total)
	print('it has',picture_total,' Allen 貼圖')
	picture2_total = sum(picture2_total)
	print('it has',picture2_total,' Viki 貼圖')
	picture_total3 = sum(picture_total3)
	print('it has',picture_total3,'Allen 圖片')
	picture_total4 = sum(picture_total4)
	print('it has',picture_total4,'Viki 圖片')
def write_file(new):
	with open ('output.txt','w',encoding = 'utf-8-sig')as f:
		for line in new:
			f.write(line + '\n')

def main():
	chat = read()
	new = convert(chat)
	# write_file(new)

main()