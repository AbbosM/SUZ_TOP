from random import randint
word_list = ["abbos", "bahti", "baho", "dado"]
# while True:
def word_sample(w):
    length = len(w)
    print(f"Men {length} xonali so'z o'yladim. Topa olasizmi?")
    # global empty
    empty =list("_"*int(f"{length}"))
    w = list(w)
    entered_letters =[]
    # global letters_input
    while empty.count("_") != 0:
        letters_input = input("Harf kiriting:>>> ")
        entered_letters.append(letters_input)
        if letters_input in w and entered_letters.count(letters_input)<=1:
            for i in range(length):
                if letters_input == w[i]:
                    # ind_num = one_word.index(letters_input)
                    empty[i] = letters_input.title()#=>>> "javob" da title() bo'lsa ikkinchi bir xil harf kichik bo'ladi
            print(empty)
            print(w)
                    
            print(f"{letters_input.title()} harfi to'g'ri.")
            javob = ''.join(empty)
            print(javob)
        elif entered_letters.count(letters_input) > 1:
            print("Bu harfni avval kiritgansiz. Boshqa harf kiriting:")
        # elif letters_input not in w:
        else:
            print("Bunday harf yo'q.")
        # elif "_" not in empty:
        #     break
    # return letters_input
    removed_same = list(dict.fromkeys(entered_letters))
    print(f"Tabriklayman topdingiz! Siz kiritgan harflar: {','.join(entered_letters)}\n"
            f"Urinishlar soni: {len(entered_letters)}")
    print(f"{','.join(removed_same)}")
        # if '-' in empty:
        #     continue
        # else:
        #     break

indx = randint(0,len(word_list)-1)
one_word = word_list[indx]
word_sample(one_word)