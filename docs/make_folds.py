import os

f = open("b90bfb242d7240f2ab2048109719471a.md", "r")
lines = f.read().splitlines()
f.close()
count = 1
tmp = []
for i, ii in enumerate(lines):
    tmp.append(ii)
    if "**Chapter" in ii:
        fold="Chapter-" + str(count)
        if not os.path.exists(fold):
           os.makedirs(fold) 
        ff = fold + "/content.md"
        #ff = "Chapter-" + str(count) + ".md"
        fname = open(ff, "w")
        tmp = "\n".join(tmp)
        fname.write(tmp)
        fname.close()
        count += 1
        tmp = []
