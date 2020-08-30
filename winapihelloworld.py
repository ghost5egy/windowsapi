import ctypes

uhandle = ctypes.WinDLL('User32.dll')
khandle = ctypes.WinDLL('Kernel32.dll')

msgbox = uhandle.MessageBoxW( None , 'Hello Ghost5egy' ,'Ghost5egy' , 0x00000001)
print(msgbox)

errors = khandle.GetLastError()
if errors > 0:
	print('error {0}'.format(errors))
