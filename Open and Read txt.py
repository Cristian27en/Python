f = open("prueba.txt", "w")
f.write("es una prueba")
f.close()

with open('test.txt', 'w') as file:
    print(type(file))
    print(id(file))
    file.write('This is a test')