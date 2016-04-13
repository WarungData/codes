section .text
	global _start


_start:
	mov eax, 5			;panggil sys_open
	mov ebx, filename		;filename 
	mov ecx, 0			;buka read only
	int 80h				;jalankan
					;perhatikan bahwa file 
					; descriptor ada di eax


	mov ebx, eax			;file descriptor eax
					; pindahkan ke ebx 
	mov eax, 3			;panggil sys_read
	mov ecx, buf			;read ke buf
	mov edx, len			;sepanjang len
	int 80h				;jalankan
					;sudah kita baca, 
					; belum kita tampilkan :)

	mov eax, 4			;panggil sys_write
	mov ebx, 1			;ke stdout
	mov ecx, buf			;tulis buf
	mov edx, len			;sepanjang len
	int 80h				;jalankan

	mov eax, 1			;panggil sys_exit
	mov ebx, 0			;return 0
	int 80h				;bye bye bye 



section .bss
buf	:	resb	255		;reserve byte


section .data
filename:	db	'/etc/passwd'	;namafile
len	:	equ	255		;panjang
