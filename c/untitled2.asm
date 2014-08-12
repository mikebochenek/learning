; generated 12.08.2014 22:05:38 with:
;    gcc untitled2.c -o untitled2.asm -S -masm=intel 
	.file	"untitled2.c"
	.intel_syntax noprefix
	.section	.rodata
	.align 4
.LC0:
	.string	"Nano sleep system call failed "
.LC1:
	.string	"%10d.%d\n"
	.align 4
.LC2:
	.string	"end tdiff tv_sec:%ld tv_usec:%ld\n"
.LC3:
	.string	"Nano sleep successfull "
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	push	ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	mov	ebp, esp
	.cfi_def_cfa_register 5
	push	ebx
	and	esp, -16
	sub	esp, 64
	mov	DWORD PTR [esp+20], 0
	mov	DWORD PTR [esp+24], 100000000
	mov	DWORD PTR [esp+60], 0
	mov	DWORD PTR [esp+4], 0
	lea	eax, [esp+36]
	mov	DWORD PTR [esp], eax
	.cfi_offset 3, -12
	call	gettimeofday
	mov	DWORD PTR [esp+60], 0
	jmp	.L2
.L5:
	lea	eax, [esp+28]
	mov	DWORD PTR [esp+4], eax
	lea	eax, [esp+20]
	mov	DWORD PTR [esp], eax
	call	nanosleep
	test	eax, eax
	jns	.L3
	mov	DWORD PTR [esp], OFFSET FLAT:.LC0
	call	puts
	mov	eax, -1
	jmp	.L4
.L3:
	mov	ebx, DWORD PTR [esp+60]
	mov	edx, 1717986919
	mov	eax, ebx
	imul	edx
	sar	edx, 2
	mov	eax, ebx
	sar	eax, 31
	mov	ecx, edx
	sub	ecx, eax
	mov	eax, ecx
	sal	eax, 2
	add	eax, ecx
	add	eax, eax
	mov	ecx, ebx
	sub	ecx, eax
	mov	ebx, DWORD PTR [esp+60]
	mov	edx, 1717986919
	mov	eax, ebx
	imul	edx
	sar	edx, 2
	mov	eax, ebx
	sar	eax, 31
	sub	edx, eax
	mov	eax, OFFSET FLAT:.LC1
	mov	DWORD PTR [esp+8], ecx
	mov	DWORD PTR [esp+4], edx
	mov	DWORD PTR [esp], eax
	call	printf
	mov	eax, DWORD PTR stdout
	mov	DWORD PTR [esp], eax
	call	fflush
	add	DWORD PTR [esp+60], 1
.L2:
	cmp	DWORD PTR [esp+60], 9999
	jle	.L5
	mov	DWORD PTR [esp+4], 0
	lea	eax, [esp+44]
	mov	DWORD PTR [esp], eax
	call	gettimeofday
	mov	edx, DWORD PTR [esp+44]
	mov	eax, DWORD PTR [esp+36]
	mov	ecx, edx
	sub	ecx, eax
	mov	eax, ecx
	mov	DWORD PTR [esp+52], eax
	mov	eax, DWORD PTR [esp+48]
	mov	edx, DWORD PTR [esp+40]
	mov	ecx, 1000000
	mov	ebx, ecx
	sub	ebx, edx
	mov	edx, ebx
	add	eax, edx
	mov	DWORD PTR [esp+56], eax
	mov	ecx, DWORD PTR [esp+56]
	mov	edx, DWORD PTR [esp+52]
	mov	eax, OFFSET FLAT:.LC2
	mov	DWORD PTR [esp+8], ecx
	mov	DWORD PTR [esp+4], edx
	mov	DWORD PTR [esp], eax
	call	printf
	mov	DWORD PTR [esp], OFFSET FLAT:.LC3
	call	puts
	mov	eax, 0
.L4:
	mov	ebx, DWORD PTR [ebp-4]
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	.cfi_restore 3
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 4.6.3-1ubuntu5) 4.6.3"
	.section	.note.GNU-stack,"",@progbits
