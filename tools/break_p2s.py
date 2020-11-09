import nltk
import sys
# nltk.download('punkt')

with open(sys.argv[1], 'r', encoding='UTF-8') as fr, open(sys.argv[1] + "_sent.html", 'w', encoding='UTF-8') as fw:
    while True:
        p = fr.readline()
        if not p: break
        if len(p.strip()) == 0: continue

        sents = nltk.sent_tokenize(p)

        fw.write("<p>")
        for sent in sents:
            fw.write("<span class=\"sent\">")
            fw.write(sent)
            fw.write("</span>\n")
        fw.write("</p>\n")

