section .text
	global _start

_start:
	mov eax, 12
	mov ebx, dir
	int 80h


	mov eax, 1
	mov ebx, 0
	int 80h



section .data
dir:	db	'/TIDAK_ADA'

