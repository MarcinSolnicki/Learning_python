
def read_file(file_name):
    f=open(file_name,"r")#r means read_only
    for x in f: #readlines by loop
        print(x)
    f.close() #closing file path

def write_file(file_name):
    f=open(file_name,"w")
    f.writelines("firstline \n")
    f.writelines("next line \n")
    f.close()



read_file("plik_tekst.txt")
write_file("tekstowy_1")
