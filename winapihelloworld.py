import ctypes

handle = ctypes.WinDLL('User32.dll')

msgbox = handle.MessageBoxW( None , 'Hello Ghost5egy' ,'Ghost5egy' , 0x00000001)
 print(msgbox)
