import fnmatch
import os

#file1=open("start_0x80000000_0x802FFFFF","rb")
#data1=file1.read()
#print(len(data1)/1024)


for file in os.listdir('.'):
  if fnmatch.fnmatch(file, 'start_0x????????_0x????????'):
    print(file)
    str_var1=file[6:16]
    str_var2=file[17:27]
    temp_file = open(file, "rb")
    temp_data = temp_file.read()
    #print(len(temp_data)>>10)
    var1=int(str_var1,16)
    var2=int(str_var2,16)
    print(str_var1)
    print(var1)
    print(str_var2)
    print(var2)
    #mu.mem_map(var1, var2-var1)
    #mu.mem_write(var1, data)
    print(var2-var1)
    print(len(temp_data))
    
