import nltk
import textstat
import sys
# nltk.download('punkt')

list_score = list()

with open(sys.argv[1], 'r', encoding='UTF-8') as fr, open(sys.argv[1] + "_sent.html", 'w', encoding='UTF-8') as fw:
    while True:
        p = fr.readline()
        if not p: break
        if len(p.strip()) == 0: continue

        sents = nltk.sent_tokenize(p)

        fw.write("<p>")
        for sent in sents:
            dc_score = textstat.flesch_kincaid_grade(sent)
            list_score.append(dc_score)
            if dc_score < 4:
                dc_score = 3
            elif dc_score < 8:
                dc_score = 2
            else:
                dc_score = 1
            print(sent + "\nscore:" + str(dc_score))
            fw.write("<span class=\"sent\", data-dif = \"" + str(dc_score) + "\">")
            fw.write(sent)
            fw.write("</span>\n")
        fw.write("</p>\n")

list_score.sort()
print(list_score)