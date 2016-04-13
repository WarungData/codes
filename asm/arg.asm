section .text
	global _start

_start:
	
	mov eax, 4
	mov ebx, 1
	mov ecx, dir
	mov edx, dir_len
	int 80h


	jl _ulang


	mov eax, 1
	mov ebx, 0
	int 80h


_ulang:
	mov eax, 4
	mov ebx, 1
	mov ecx, counter
	mov edx, 2
	int 80h
	inc counter,1


section .data
dir	db	'/bin',10
dir_len	equ	$-dir
max	equ	100


section .bss
counter	resb	2
