def read():
    chat = []
    with open ('C:/Users/DOS/Desktop/coding/chat/-LINE-Viki.txt', 'r',encoding = 'utf-8-sig') as f:
        for line in f:
            chat.append(line.strip())
        # print(chat)
        return chat

def convert(chat):
    Allen_total = []
    VIki_total = []
    Allen_word = 0
    VIki_word = 0
    for line in chat:
        s = line.split(' ')
        name = s[1]
        if name == 'Allen':
            for m in s[2:]:
                Allen_word += len(m)
                Allen_total.append(Allen_word)
                Allen_word = 0

        elif name == 'Viki':
            for m2 in s[2:]:
                VIki_word += len(m2)
                VIki_total.append(VIki_word)
                VIki_word = 0
    Allen_total = sum(Allen_total)
    print('it has',Allen_total,'word Allen said')
    VIki_total = sum(VIki_total)
    print('it has',VIki_total,'word Viki said')
def write_file(new):
    with open ('output.txt','w',encoding = 'utf-8-sig')as f:
        for line in new:
            f.write(line + '\n')

def main():
    chat = read()
    new = convert(chat)
    # write_file(new)

main()