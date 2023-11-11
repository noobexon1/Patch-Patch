import sys
import argparse
import struct
from elf_constants_32 import *


# TODO: Make a toString() function (we can make an array of strings out of the values). (pages 1-4, ... , 1-8).
# TODO: The product of e_phentsize * e_phnum is equal to the program header table's size in bytes! Use it!
# TODO: The product of e_shentsize * e_shnum is equal to the section header table's size in bytes! Use it!
# TODO: make a function to check that e_ident[EI_VERSION] = EV_CURRENT otherwise exit.

# TODO: Add support for 64-bit files (maybe make ELFHeader32 and ELFHeader64 sub classes that inherit from ELFHeader).


class ELFHeader:
    def __init__(self, file_bytes):
        self.e_ident = file_bytes[:EI_NIDENT]    # Identifier flags in an array. Used to decode and interpret the file.

        endian_format = '<' if self.e_ident[EI_DATA] == ELFDATA2LSB else '>'  # '<' == little endian, '>' == big endian.
        struct_format = endian_format + 'HHIIIIIHHHHHH'  # 'H' -> 2 bytes, 'I' -> 4 bytes.

        (
            self.e_type,        # Object file's type.
            self.e_machine,     # Required CPU architecture for the file.
            self.e_version,     # Object file's version.
            self.e_entry,       # Virtual address of the entry point, where the process start executing.
            self.e_phoff,       # Program header table's file offset in bytes or 0 if non-existent.
            self.e_shoff,       # Section header table's file offset in bytes or 0 if non-existent.
            self.e_flags,       # Holds processor-specific flags associated with the file.
            self.e_ehsize,      # ELF Header's size in bytes.
            self.e_phentsize,   # Size in bytes of an entry in the program header table. All entries have same size.
            self.e_phnum,       # Number of entries in the program header table or 0 if there is no PHT.
            self.e_shentsize,   # Size in bytes of a section header (one entry at SH table). All entries have same size.
            self.e_shnum,       # Number of entries in the section header table or 0 if there is no SHT.
            self.e_shstrndx     # Index of "string table" section at the section header table or SHN_UNDEF if no SHT
        ) = struct.unpack(struct_format, file_bytes[EI_NIDENT:EI_NIDENT + struct.calcsize(struct_format)])


class ELFFile:
    def __init__(self, filepath):

        self.file_path = filepath   # Path to the file provided by the user.
        self.file_bytes = None      # File's data as bytes.
        self.elf_header = None      # ELF File's Header.

        self.__read_bytes()
        if self.__is_elf():
            self.__parse_elf_header()
        else:
            raise ValueError("The file provided is not an ELF object file.")

    def __read_bytes(self):
        with open(self.file_path, 'rb') as file:
            self.file_bytes = file.read()

    def __is_elf(self):
        return self.file_bytes.startswith(ELF_MAGIC)

    def __parse_elf_header(self):
        self.elf_header = ELFHeader(self.file_bytes)


def main():
    # TODO: add 'usage' and update to 32/64-bit after we add support for 64.
    # TODO: add interactive mode where things can be changed in real time.
    parser = argparse.ArgumentParser(
        prog='patch-patch',
        description='A simple 32-bit ELF file explorer and patcher'
    )
    # TODO: add more arguments as needed.
    parser.add_argument("-f", "--file", help="path to the ELF file", required=True)

    args = parser.parse_args()
    filepath = args.file

    try:
        elf_file = ELFFile(filepath)
    except ValueError as err:
        print("[ERROR]:", err)


if __name__ == "__main__":
    main()
