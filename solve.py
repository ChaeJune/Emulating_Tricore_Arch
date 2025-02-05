#!/usr/bin/env python
'''
unicorn engien + tricore emulation + scattered firmware
'''

from __future__ import print_function
from unicorn import *
from unicorn.tricore_const import *
from pwn import *
import fnmatch
import os
import natsort
import binascii
import re
#all binary in dump_crc emulated

arr=['spoon','scary','asked']
new_arr=[]
li=[]
for i in range(0,3):
  new_arr.append("FLAG{"+arr[i]+arr[(i+1)%3]+arr[(i+2)%3])
  new_arr.append("FLAG{"+arr[i]+arr[(i+2)%3]+arr[(i+1)%3])

# callback for tracing basic blocks
def hook_block(uc, address, size, user_data):
    #print(">>> Tracing basic block at 0x%x, block size = 0x%x" %(address, size))
    pass
# callback for tracing instructions
def hook_code(uc, address, size, user_data):
    pass
    #if address == 0x800065fe:
      #uc.mem_write(0x80000020,binascii.unhexlify("5f"))
      #payload=b'FLAG{scaryspoonaskedrainy}\x00'
      #print("compulsory assignment")
      #uc.reg_write(UC_TRICORE_REG_D15, 0x5f)
def print_reg(mu):
        #print(">>> Emulation done. Below is the CPU context")
        #D0 = mu.reg_read(UC_TRICORE_REG_D0)
        #print(">>> D0= 0x%x" %D0)
        #D1 = mu.reg_read(UC_TRICORE_REG_D1)
        #print(">>> D1= 0x%x" %D1)
        D2 = mu.reg_read(UC_TRICORE_REG_D2)
        #print(">>> D2= 0x%x" %D2)
        D15 = mu.reg_read(UC_TRICORE_REG_D15)
        #print(">>> D15= 0x%x" %D15)
        A10 = mu.reg_read(UC_TRICORE_REG_A10)
        #print(">>> A10= 0x%x" %A10)
        if D2 == D15:
          print("stack 0x700395d8: "+str(mu.mem_read(0x700395d8,0x20)))
          print(" >>> D2 = 0x%x" %D2)
          print(">>> D15= 0x%x" %D15)

# Test TriCore
def test_tricore():
    print(new_arr)
    print("Emulate TriCore code")
    try:
        prev_addr = 0
        # Initialize emulator in TriCore mode
        mu = Uc(UC_ARCH_TRICORE, UC_MODE_LITTLE_ENDIAN)

        sortedList = natsort.natsorted(os.listdir('.'))
        for file in sortedList:
          if fnmatch.fnmatch(file, 'start_0x????????_0x????????'):
            str_var1=file[6:16]
            str_var2=file[17:27]
            temp_file = open(file, "rb")
            temp_data = temp_file.read()
            var1=int(str_var1,16)
            var2=int(str_var2,16)
            unit=0x4000
            iterator = var1
            while iterator < var2:
              mu.mem_map(iterator, unit)
              iterator = iterator + unit
            if str_var1[2]=='C' or str_var1[2]=='D':
              #print('C')
              temp_data=temp_data[:-1]
            mu.mem_write(var1, temp_data)
        #register setup using start_regs.txt
        unit=0x4000
        print('.')
        print('mapping complete')
        mu.reg_write(UC_TRICORE_REG_D0, 0x0186A0)
        mu.reg_write(UC_TRICORE_REG_D1, 0x037C8192)
        mu.reg_write(UC_TRICORE_REG_D2, 0x00)
        mu.reg_write(UC_TRICORE_REG_D3, 0x00)
        mu.reg_write(UC_TRICORE_REG_D4, 0x00)
        mu.reg_write(UC_TRICORE_REG_D5, 0x00)
        mu.reg_write(UC_TRICORE_REG_D6, 0x00)
        mu.reg_write(UC_TRICORE_REG_D7, 0x00)
        mu.reg_write(UC_TRICORE_REG_D8, 0x3C)
        mu.reg_write(UC_TRICORE_REG_D9, 0x3C)
        mu.reg_write(UC_TRICORE_REG_D10, 0x00)
        mu.reg_write(UC_TRICORE_REG_D11, 0x00)
        mu.reg_write(UC_TRICORE_REG_D12, 0x00)
        mu.reg_write(UC_TRICORE_REG_D13, 0x00)
        mu.reg_write(UC_TRICORE_REG_D14, 0x00)
        mu.reg_write(UC_TRICORE_REG_D15, 0xFFFC000F)
        mu.reg_write(UC_TRICORE_REG_A0, 0x00)
        mu.reg_write(UC_TRICORE_REG_A1, 0x00)
        mu.reg_write(UC_TRICORE_REG_A2, 0xF0030000)
        mu.reg_write(UC_TRICORE_REG_A3, 0xF0030000)
        mu.reg_write(UC_TRICORE_REG_A4, 0x70000000)
        mu.reg_write(UC_TRICORE_REG_A5, 0x800002C0)
        mu.reg_write(UC_TRICORE_REG_A6, 0x00)
        mu.reg_write(UC_TRICORE_REG_A7, 0x00)
        mu.reg_write(UC_TRICORE_REG_A8, 0x00)
        mu.reg_write(UC_TRICORE_REG_A9, 0x00)
        mu.reg_write(UC_TRICORE_REG_A10, 0x70039600)
        mu.reg_write(UC_TRICORE_REG_A11, 0x800064da)
        mu.reg_write(UC_TRICORE_REG_A12, 0x00)
        mu.reg_write(UC_TRICORE_REG_A13, 0x00)
        mu.reg_write(UC_TRICORE_REG_A14, 0x00)
        mu.reg_write(UC_TRICORE_REG_A15, 0x800081DC)
        mu.reg_write(UC_TRICORE_REG_PC, 0x80006564)
        mu.reg_write(UC_TRICORE_REG_PSW, 0x0C000981)
        mu.reg_write(UC_TRICORE_REG_PCXI, 0x370E70)
        mu.reg_write(UC_TRICORE_REG_FCX, 0x070E71)
        mu.reg_write(UC_TRICORE_REG_LCX, 0x070EED)
        mu.reg_write(UC_TRICORE_REG_ISP, 0x70039B00)
        mu.reg_write(UC_TRICORE_REG_ICR, 0x8000)
        mu.reg_write(UC_TRICORE_REG_BIV, 0x802FE000)
        mu.reg_write(UC_TRICORE_REG_BTV, 0x80000100)
        # tracing one instruction at ADDRESS with customized callback

        f = open("string_data","r")
        tsr = f.readlines()
        for line in tsr:
          tmp=re.search(r'".{5,10}"',line.replace(' ',''))
          if tmp!=None:
            ll=line.replace(' ','')
            #print(ll[tmp.start()+1:tmp.end()-1])
            li.append(ll[tmp.start()+1:tmp.end()-1])
         #print(len(arr))
        mu.hook_add(UC_HOOK_CODE, hook_code)
        mu.emu_start(0x80006564,0x80006602)
        for item in li:
          for head in new_arr:
            payload = head+item+"}\0"
            #print(payload)
            mu.mem_write(0x700395d8,payload.encode())
            mu.emu_start(0x80006602, 0x8000660e)
        # now print out some registers
            print_reg(mu)

    except UcError as e:
        print("ERROR: %s" % e)
        print_reg(mu)
if __name__ == '__main__':
    test_tricore()
