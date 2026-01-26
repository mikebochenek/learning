	.file	"untitled1.c"
	.intel_syntax noprefix
	.text
	.globl	bsort
	.type	bsort, @function
bsort:
.LFB5:
	.cfi_startproc
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp
	.cfi_def_cfa_register 6
	nop
	pop	rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE5:
	.size	bsort, .-bsort
	.section	.rodata
.LC0:
	.string	"blah"
	.align 8
.LC1:
	.string	"welcome to my world of pointers %p"
.LC2:
	.string	"\n%d %d"
.LC3:
	.string	"\n%s"
	.text
	.globl	play
	.type	play, @function
play:
.LFB6:
	.cfi_startproc
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp
	.cfi_def_cfa_register 6
	sub	rsp, 48
	mov	rax, QWORD PTR fs:40
	mov	QWORD PTR -8[rbp], rax
	xor	eax, eax
	mov	DWORD PTR -40[rbp], 0
	jmp	.L3
.L4:
	mov	edi, 10
	call	malloc@PLT
	mov	QWORD PTR -32[rbp], rax
	add	DWORD PTR -40[rbp], 1
.L3:
	cmp	DWORD PTR -40[rbp], 999
	jle	.L4
	mov	DWORD PTR -36[rbp], 10
	lea	rax, .LC0[rip]
	mov	QWORD PTR -24[rbp], rax
	lea	rax, -32[rbp]
	mov	rsi, rax
	lea	rdi, .LC1[rip]
	mov	eax, 0
	call	printf@PLT
	mov	eax, DWORD PTR -36[rbp]
	mov	edx, eax
	mov	esi, 8
	lea	rdi, .LC2[rip]
	mov	eax, 0
	call	printf@PLT
	mov	rax, QWORD PTR -24[rbp]
	mov	rsi, rax
	lea	rdi, .LC3[rip]
	mov	eax, 0
	call	printf@PLT
	mov	rax, QWORD PTR -32[rbp]
	mov	rdi, rax
	call	free@PLT
	nop
	mov	rax, QWORD PTR -8[rbp]
	xor	rax, QWORD PTR fs:40
	je	.L5
	call	__stack_chk_fail@PLT
.L5:
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE6:
	.size	play, .-play
	.globl	main
	.type	main, @function
main:
.LFB7:
	.cfi_startproc
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp
	.cfi_def_cfa_register 6
	mov	eax, 0
	call	play
	mov	eax, 0
	call	bsort
	mov	eax, 0
	pop	rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE7:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
