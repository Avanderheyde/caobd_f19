def mapper(line):
    for word in line.split():
        yield word, 1

for output in mapper("i am a string a short string"):
    print(output)