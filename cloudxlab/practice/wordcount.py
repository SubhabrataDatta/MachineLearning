#Program to give word with maximum repititions

#name=input('enter file name: ')
#handle=open(name,'r')

handle=open('text.txt','r')
text=handle.read()
words=text.split()
print(text)
print(words)
counts=dict()
for word in words:
        counts[word]=counts.get(word,0)+1
bigcount=None
bigword=None

for word,count in counts.items():
    if bigcount is None or count >bigcount:
        bigword=word
        bigcount=count
print(bigword,bigcount)
print(bigword + ":" + "\t" + str(bigcount))
