# ********** ELF 32-Bit Data Types **********:

Elf32_Addr_Size = Elf32_Addr_Alignment = 4          # Unsigned program address
Elf32_Half_Size = Elf32_Half_Alignment = 2          # Unsigned medium integer
Elf32_Off_Size = Elf32_Off_Alignment = 4            # Unsigned file offset
Elf32_Sword_Size = Elf32_Sword_Alignment = 4        # Signed large integer
Elf32_Word_Size = Elf32_Word_Alignment = 4          # Unsigned large integer
unsigned_char_Size = unsigned_char_Alignment = 1    # Unsigned small integer


# ********** Elf 32-bit Header **********:

# ***** e_ident[] member *****:

# e_ident[] indexes
EI_MAG0 = 0         # File identification
EI_MAG1 = 1         # File identification
EI_MAG2 = 2         # File identification
EI_MAG3 = 3         # File identification
EI_CLASS = 4        # File class
EI_DATA = 5         # Data encoding
EI_VERSION = 6      # File version
EI_PAD = 7          # Start of padding bytes
EI_NIDENT = 16      # Size of e_ident[]

# Magic number
ELF_MAGIC = b'\x7fELF'  # entire magic number

# Magic number bytes
ELFMAG0 = 0x7F      # e_ident[EI_MAG0]
ELFMAG1 = ord('E')  # e_ident[EI_MAG1]
ELFMAG2 = ord('L')  # e_ident[EI_MAG2]
ELFMAG3 = ord('F')  # e_ident[EI_MAG3]

# File class = e_ident[EI_CLASS]
ELFCLASSNONE = 0    # Invalid class
ELFCLASS32 = 1      # 32-bit objects
ELFCLASS64 = 2      # 64-bit objects

# Data encoding = e_ident[EI_DATA]
ELFDATANONE = 0     # Invalid data encoding
ELFDATA2LSB = 1     # Little-endian
ELFDATA2MSB = 2     # Big-endian


# ***** Rest oof the members *****:

# e_type
ET_NONE = 0         # No file type
ET_REL = 1          # Relocatable file
ET_EXEC = 2         # Executable file
ET_DYN = 3          # Shared object file
ET_CORE = 4         # Core file
ET_LOPROC = 0xff00  # Processor-specific
ET_HIPROC = 0xffff  # Processor-specific

# e_machine
EM_NONE = 0          # No machine
EM_M32 = 1           # AT&T WE 32100
EM_SPARC = 2         # SPARC
EM_386 = 3           # Intel Architecture
EM_68K = 4           # Motorola 68000
EM_88K = 5           # Motorola 88000
EM_IAMCU = 6         # Intel 80860
EM_860 = 7           # Intel 80860
EM_MIPS = 8          # MIPS RS3000 big-endian
EM_MIPS_RS3_LE = 10  # MIPS RS4000 little-endian

# e_version
EV_NONE = 0         # Invalid version
EV_CURRENT = 1      # Current version
