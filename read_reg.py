import json

with open("start_regs.txt","r") as f:
  lines = f.readlines()
  for line in lines:
    string = line.rstrip().strip('{}')
    #print(string)
    pairs = string.split(', ')
    #print(pairs)
    temp_name=""
    temp_value=""
    for pair in pairs:
      key, value =(pair.split(': '))
      if key =="name":
        temp_name=value
      if key == "value":
        temp_value=value
        #print(key+"..."+value.strip("''"))
    temp_name=temp_name.strip("''")
    print(' '*8+temp_name+' = '+'mu.reg_read(UC_TRICORE_REG_'+temp_name+')')
    print(' '*8+'print(">>> '+temp_name+'= 0x%x" %'+temp_name+')')
