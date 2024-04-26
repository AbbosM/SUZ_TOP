from random import randint
word_list = ["abbos", "bahti", "baho", "dado"]
def word_sample(w):
    length = len(w)
    print(f"Men {length} xonali so'z o'yladim. Topa olasizmi?")
    empty =list("_"*int(f"{length}"))
    w = list(w)
    entered_letters =[]
    while empty.count("_") != 0:
        letters_input = input("Harf kiriting:>>> ")
        entered_letters.append(letters_input)
        if letters_input in w and entered_letters.count(letters_input)<=1:
            for i in range(length):
                if letters_input == w[i]:
                    empty[i] = letters_input.title()#=>>> "javob" da title() bo'lsa ikkinchi bir xil harf kichik bo'ladi
            print(empty)
            print(w)
                    
            print(f"{letters_input.title()} harfi to'g'ri.")
            javob = ''.join(empty)
            print(javob)
        elif entered_letters.count(letters_input) > 1:
            print("Bu harfni avval kiritgansiz. Boshqa harf kiriting:")
        else:
            print("Bunday harf yo'q.")
     removed_same = list(dict.fromkeys(entered_letters))
    print(f"Tabriklayman topdingiz! Siz kiritgan harflar: {','.join(entered_letters)}\n"
            f"Urinishlar soni: {len(entered_letters)}")
    print(f"{','.join(removed_same)}")

indx = randint(0,len(word_list)-1)
one_word = word_list[indx]
word_sample(one_word)
