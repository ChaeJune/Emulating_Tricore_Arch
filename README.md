# Emulating_Tricore_Arch
Unicorn emulator, emulate tricore arch using dump file

Memory dump files are split into about 70 chunks, named like start_0x????????_0x???????? 
Organize stack from 0x10000000 to 0xD00C0000 with iterator
start_regs.txt contains the information of registers
solve.py performs brute-force to find flag using some hints of the problem CRC'LY, emulating tricore arch


dumpfile from https://github.com/camercu/chv-ctf-2022-writeup/blob/main/CRCly.md
