# Emulating Tricore Architecture

This project uses the Unicorn emulator to emulate the Tricore architecture with a memory dump file.

## Memory Dump

The memory dump file is split into approximately 70 chunks, each named in the format `start_0x????????_0x????????`.

## Stack Organization

The stack is organized from `0x10000000` to `0xD00C0000` using an iterator.

## Register Information

The `start_regs.txt` file contains the initial register values.

## Flag Brute-forcing

The `solve.py` script performs a brute-force attack to find the flag. It utilizes clues from the problem description, "CRC'LY", and emulates the Tricore architecture.

## Source of Dump File

The memory dump file is from [CRCly writeup](https://github.com/camercu/chv-ctf-2022-writeup/blob/main/CRCly.md) on GitHub.
