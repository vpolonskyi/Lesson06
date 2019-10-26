with open("in_txt.txt", "r") as f:
    res_dict = {}
    res_list = []
    for line in f:
        for word in line.split():
            word = word.strip('-,!.():; #"')
            if word.isalpha():
                word = word.lower()
                if res_dict.get(word) is None:
                    res_dict[word] = 1
                    res_list.append(word)
                else:
                    res_dict[word] += 1
res_list.sort()
out = ''
for word in res_list:
    out = out + word + " " + str(res_dict[word]) + "\n"

with open("out_txt.txt", "w") as f:
    f.write(out)
