	.file	"untitled3.c"
	.intel_syntax noprefix
	.text
	.section	.rodata
	.align 8
.LC0:
	.string	"Hello World! It's me, thread %d!\n"
	.text
	.globl	TaskCode
	.type	TaskCode, @function
TaskCode:
.LFB5:
	.cfi_startproc
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp
	.cfi_def_cfa_register 6
	sub	rsp, 32
	mov	QWORD PTR -24[rbp], rdi
	mov	rax, QWORD PTR -24[rbp]
	mov	eax, DWORD PTR [rax]
	mov	DWORD PTR -4[rbp], eax
	mov	eax, DWORD PTR -4[rbp]
	mov	esi, eax
	lea	rdi, .LC0[rip]
	mov	eax, 0
	call	printf@PLT
	mov	eax, 0
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE5:
	.size	TaskCode, .-TaskCode
	.section	.rodata
.LC1:
	.string	"In main: creating thread %d\n"
.LC2:
	.string	"untitled3.c"
.LC3:
	.string	"0 == rc"
	.text
	.globl	main
	.type	main, @function
main:
.LFB6:
	.cfi_startproc
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp
	.cfi_def_cfa_register 6
	sub	rsp, 96
	mov	rax, QWORD PTR fs:40
	mov	QWORD PTR -8[rbp], rax
	xor	eax, eax
	mov	DWORD PTR -88[rbp], 0
	jmp	.L4
.L6:
	mov	eax, DWORD PTR -88[rbp]
	cdqe
	mov	edx, DWORD PTR -88[rbp]
	mov	DWORD PTR -80[rbp+rax*4], edx
	mov	eax, DWORD PTR -88[rbp]
	mov	esi, eax
	lea	rdi, .LC1[rip]
	mov	eax, 0
	call	printf@PLT
	lea	rax, -80[rbp]
	mov	edx, DWORD PTR -88[rbp]
	movsx	rdx, edx
	sal	rdx, 2
	add	rdx, rax
	lea	rax, -48[rbp]
	mov	ecx, DWORD PTR -88[rbp]
	movsx	rcx, ecx
	sal	rcx, 3
	add	rax, rcx
	mov	rcx, rdx
	lea	rdx, TaskCode[rip]
	mov	esi, 0
	mov	rdi, rax
	call	pthread_create@PLT
	mov	DWORD PTR -84[rbp], eax
	cmp	DWORD PTR -84[rbp], 0
	je	.L5
	lea	rcx, __PRETTY_FUNCTION__.3290[rip]
	mov	edx, 32
	lea	rsi, .LC2[rip]
	lea	rdi, .LC3[rip]
	call	__assert_fail@PLT
.L5:
	add	DWORD PTR -88[rbp], 1
.L4:
	cmp	DWORD PTR -88[rbp], 4
	jle	.L6
	mov	DWORD PTR -88[rbp], 0
	jmp	.L7
.L9:
	mov	eax, DWORD PTR -88[rbp]
	cdqe
	mov	rax, QWORD PTR -48[rbp+rax*8]
	mov	esi, 0
	mov	rdi, rax
	call	pthread_join@PLT
	mov	DWORD PTR -84[rbp], eax
	cmp	DWORD PTR -84[rbp], 0
	je	.L8
	lea	rcx, __PRETTY_FUNCTION__.3290[rip]
	mov	edx, 38
	lea	rsi, .LC2[rip]
	lea	rdi, .LC3[rip]
	call	__assert_fail@PLT
.L8:
	add	DWORD PTR -88[rbp], 1
.L7:
	cmp	DWORD PTR -88[rbp], 4
	jle	.L9
	mov	edi, 0
	call	exit@PLT
	.cfi_endproc
.LFE6:
	.size	main, .-main
	.section	.rodata
	.type	__PRETTY_FUNCTION__.3290, @object
	.size	__PRETTY_FUNCTION__.3290, 5
__PRETTY_FUNCTION__.3290:
	.string	"main"
	.ident	"GCC: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
