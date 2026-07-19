	.text
	.def	@feat.00;
	.scl	3;
	.type	0;
	.endef
	.globl	@feat.00
.set @feat.00, 0
	.file	"untitled4.c"
	.def	main;
	.scl	2;
	.type	32;
	.endef
	.globl	main                            # -- Begin function main
	.p2align	4, 0x90
main:                                   # @main
.Lfunc_begin0:
	.cv_func_id 0
	.cv_file	1 "C:\\dev\\code\\learning\\c\\untitled4.c" "03B2357C215208DC5BB18728BA8F5CE9" 1
	.cv_loc	0 1 12 0                        # untitled4.c:12:0
.seh_proc main
# %bb.0:
	pushq	%rbp
	.seh_pushreg %rbp
	pushq	%rsi
	.seh_pushreg %rsi
	subq	$296, %rsp                      # imm = 0x128
	.seh_stackalloc 296
	leaq	128(%rsp), %rbp
	.seh_setframe %rbp, 128
	.seh_endprologue
	callq	__main
	movq	.refptr.__stack_chk_guard(%rip), %rax
	movq	(%rax), %rax
	xorq	%rbp, %rax
	movq	%rax, 160(%rbp)
	movl	$0, 140(%rbp)
.Ltmp0:
	.cv_loc	0 1 13 0                        # untitled4.c:13:0
	movl	$305419896, 156(%rbp)           # imm = 0x12345678
	.cv_loc	0 1 14 0                        # untitled4.c:14:0
	xorl	%eax, %eax
	movl	%eax, %ecx
	callq	_time64
	movq	%rax, 144(%rbp)
	.cv_loc	0 1 15 0                        # untitled4.c:15:0
	leaq	144(%rbp), %rcx
	callq	_localtime64
	movq	%rax, 128(%rbp)
.Ltmp1:
	.cv_loc	0 1 17 0                        # untitled4.c:17:0
	movl	$0, 124(%rbp)
.LBB0_1:                                # =>This Inner Loop Header: Depth=1
	movslq	124(%rbp), %rax
	cmpq	$4, %rax
	jae	.LBB0_12
# %bb.2:                                #   in Loop: Header=BB0_1 Depth=1
.Ltmp2:
	.cv_loc	0 1 18 0                        # untitled4.c:18:0
	movb	$1, %al
	testb	$1, %al
	jne	.LBB0_4
	jmp	.LBB0_3
.LBB0_3:                                #   in Loop: Header=BB0_1 Depth=1
	leaq	.L__unnamed_1(%rip), %rcx
	callq	__ubsan_handle_nonnull_arg
.LBB0_4:                                #   in Loop: Header=BB0_1 Depth=1
	movslq	124(%rbp), %r9
	movl	%r9d, %eax
	movl	%eax, 92(%rbp)                  # 4-byte Spill
	leaq	156(%rbp,%r9), %rcx
	movq	%rcx, 96(%rbp)                  # 8-byte Spill
	movq	%rcx, %rax
	movq	%rax, 104(%rbp)                 # 8-byte Spill
	leaq	156(%rbp), %r8
	movq	%r8, 112(%rbp)                  # 8-byte Spill
	testq	%r8, %r8
	setne	%al
	testq	%rcx, %rcx
	setne	%dl
	andb	%dl, %al
	movb	$1, %dl
	subq	%r8, %rcx
	setae	%r8b
	setb	%cl
	testq	%r9, %r9
	movzbl	%r8b, %r8d
	movzbl	%cl, %ecx
	cmovnsl	%r8d, %ecx
                                        # kill: def $cl killed $cl killed $ecx
	andb	%dl, %cl
	andb	%cl, %al
	testb	$1, %al
	jne	.LBB0_6
# %bb.5:                                #   in Loop: Header=BB0_1 Depth=1
	movq	96(%rbp), %r8                   # 8-byte Reload
	movq	112(%rbp), %rdx                 # 8-byte Reload
	leaq	.L__unnamed_2(%rip), %rcx
	callq	__ubsan_handle_pointer_overflow
.LBB0_6:                                #   in Loop: Header=BB0_1 Depth=1
	movq	104(%rbp), %rax                 # 8-byte Reload
	cmpq	$0, %rax
	jne	.LBB0_8
# %bb.7:                                #   in Loop: Header=BB0_1 Depth=1
	movq	104(%rbp), %rdx                 # 8-byte Reload
	leaq	.L__unnamed_3(%rip), %rcx
	callq	__ubsan_handle_type_mismatch_v1
.LBB0_8:                                #   in Loop: Header=BB0_1 Depth=1
	movl	92(%rbp), %edx                  # 4-byte Reload
	movq	104(%rbp), %rax                 # 8-byte Reload
	movsbl	(%rax), %r8d
	leaq	.L.str(%rip), %rcx
	callq	printf
.Ltmp3:
# %bb.9:                                #   in Loop: Header=BB0_1 Depth=1
	.cv_loc	0 1 17 0                        # untitled4.c:17:0
	movl	124(%rbp), %eax
	movl	%eax, 84(%rbp)                  # 4-byte Spill
	incl	%eax
	movl	%eax, 88(%rbp)                  # 4-byte Spill
	seto	%al
	xorb	$-1, %al
	testb	$1, %al
	jne	.LBB0_11
# %bb.10:                               #   in Loop: Header=BB0_1 Depth=1
	movl	84(%rbp), %eax                  # 4-byte Reload
	movl	%eax, %eax
	movl	%eax, %edx
	leaq	.L__unnamed_4(%rip), %rcx
	movl	$1, %r8d
	callq	__ubsan_handle_add_overflow
.LBB0_11:                               #   in Loop: Header=BB0_1 Depth=1
	movl	88(%rbp), %eax                  # 4-byte Reload
	movl	%eax, 124(%rbp)
	jmp	.LBB0_1
.Ltmp4:
.LBB0_12:
	.cv_loc	0 1 21 0                        # untitled4.c:21:0
	movb	$1, %al
	testb	$1, %al
	jne	.LBB0_14
	jmp	.LBB0_13
.LBB0_13:
	leaq	.L__unnamed_5(%rip), %rcx
	callq	__ubsan_handle_nonnull_arg
.LBB0_14:
	movq	144(%rbp), %rax
	movq	%rax, 64(%rbp)                  # 8-byte Spill
	movq	128(%rbp), %rcx
	movq	%rcx, 72(%rbp)                  # 8-byte Spill
	cmpq	$0, %rcx
	setne	%al
	andq	$3, %rcx
	cmpq	$0, %rcx
	sete	%cl
	andb	%cl, %al
	testb	$1, %al
	jne	.LBB0_16
# %bb.15:
	movq	72(%rbp), %rdx                  # 8-byte Reload
	leaq	.L__unnamed_6(%rip), %rcx
	callq	__ubsan_handle_type_mismatch_v1
.LBB0_16:
	movq	72(%rbp), %rcx                  # 8-byte Reload
	addq	$20, %rcx
	movq	%rcx, 56(%rbp)                  # 8-byte Spill
	cmpq	$0, %rcx
	setne	%al
	andq	$3, %rcx
	cmpq	$0, %rcx
	sete	%cl
	andb	%cl, %al
	testb	$1, %al
	jne	.LBB0_18
# %bb.17:
	movq	56(%rbp), %rdx                  # 8-byte Reload
	leaq	.L__unnamed_7(%rip), %rcx
	callq	__ubsan_handle_type_mismatch_v1
.LBB0_18:
	movq	56(%rbp), %rax                  # 8-byte Reload
	movl	(%rax), %eax
	movl	%eax, 48(%rbp)                  # 4-byte Spill
	addl	$1900, %eax                     # imm = 0x76C
	movl	%eax, 52(%rbp)                  # 4-byte Spill
	seto	%al
	xorb	$-1, %al
	testb	$1, %al
	jne	.LBB0_20
# %bb.19:
	movl	48(%rbp), %eax                  # 4-byte Reload
	movl	%eax, %eax
	movl	%eax, %edx
	leaq	.L__unnamed_8(%rip), %rcx
	movl	$1900, %r8d                     # imm = 0x76C
	callq	__ubsan_handle_add_overflow
.LBB0_20:
	movq	128(%rbp), %rcx
	movq	%rcx, 40(%rbp)                  # 8-byte Spill
	cmpq	$0, %rcx
	setne	%al
	andq	$3, %rcx
	cmpq	$0, %rcx
	sete	%cl
	andb	%cl, %al
	testb	$1, %al
	jne	.LBB0_22
# %bb.21:
	movq	40(%rbp), %rdx                  # 8-byte Reload
	leaq	.L__unnamed_9(%rip), %rcx
	callq	__ubsan_handle_type_mismatch_v1
.LBB0_22:
	movq	40(%rbp), %rcx                  # 8-byte Reload
	addq	$16, %rcx
	movq	%rcx, 32(%rbp)                  # 8-byte Spill
	cmpq	$0, %rcx
	setne	%al
	andq	$3, %rcx
	cmpq	$0, %rcx
	sete	%cl
	andb	%cl, %al
	testb	$1, %al
	jne	.LBB0_24
# %bb.23:
	movq	32(%rbp), %rdx                  # 8-byte Reload
	leaq	.L__unnamed_10(%rip), %rcx
	callq	__ubsan_handle_type_mismatch_v1
.LBB0_24:
	movq	32(%rbp), %rax                  # 8-byte Reload
	movl	(%rax), %eax
	movl	%eax, 24(%rbp)                  # 4-byte Spill
	incl	%eax
	movl	%eax, 28(%rbp)                  # 4-byte Spill
	seto	%al
	xorb	$-1, %al
	testb	$1, %al
	jne	.LBB0_26
# %bb.25:
	movl	24(%rbp), %eax                  # 4-byte Reload
	movl	%eax, %eax
	movl	%eax, %edx
	leaq	.L__unnamed_11(%rip), %rcx
	movl	$1, %r8d
	callq	__ubsan_handle_add_overflow
.LBB0_26:
	movq	128(%rbp), %rcx
	movq	%rcx, 16(%rbp)                  # 8-byte Spill
	cmpq	$0, %rcx
	setne	%al
	andq	$3, %rcx
	cmpq	$0, %rcx
	sete	%cl
	andb	%cl, %al
	testb	$1, %al
	jne	.LBB0_28
# %bb.27:
	movq	16(%rbp), %rdx                  # 8-byte Reload
	leaq	.L__unnamed_12(%rip), %rcx
	callq	__ubsan_handle_type_mismatch_v1
.LBB0_28:
	movq	16(%rbp), %rcx                  # 8-byte Reload
	addq	$12, %rcx
	movq	%rcx, 8(%rbp)                   # 8-byte Spill
	cmpq	$0, %rcx
	setne	%al
	andq	$3, %rcx
	cmpq	$0, %rcx
	sete	%cl
	andb	%cl, %al
	testb	$1, %al
	jne	.LBB0_30
# %bb.29:
	movq	8(%rbp), %rdx                   # 8-byte Reload
	leaq	.L__unnamed_13(%rip), %rcx
	callq	__ubsan_handle_type_mismatch_v1
.LBB0_30:
	movq	8(%rbp), %rax                   # 8-byte Reload
	movl	(%rax), %eax
	movl	%eax, -4(%rbp)                  # 4-byte Spill
	movq	128(%rbp), %rcx
	movq	%rcx, (%rbp)                    # 8-byte Spill
	cmpq	$0, %rcx
	setne	%al
	andq	$3, %rcx
	cmpq	$0, %rcx
	sete	%cl
	andb	%cl, %al
	testb	$1, %al
	jne	.LBB0_32
# %bb.31:
	movq	(%rbp), %rdx                    # 8-byte Reload
	leaq	.L__unnamed_14(%rip), %rcx
	callq	__ubsan_handle_type_mismatch_v1
.LBB0_32:
	movq	(%rbp), %rcx                    # 8-byte Reload
	addq	$8, %rcx
	movq	%rcx, -16(%rbp)                 # 8-byte Spill
	cmpq	$0, %rcx
	setne	%al
	andq	$3, %rcx
	cmpq	$0, %rcx
	sete	%cl
	andb	%cl, %al
	testb	$1, %al
	jne	.LBB0_34
# %bb.33:
	movq	-16(%rbp), %rdx                 # 8-byte Reload
	leaq	.L__unnamed_15(%rip), %rcx
	callq	__ubsan_handle_type_mismatch_v1
.LBB0_34:
	movq	-16(%rbp), %rax                 # 8-byte Reload
	movl	(%rax), %eax
	movl	%eax, -28(%rbp)                 # 4-byte Spill
	movq	128(%rbp), %rcx
	movq	%rcx, -24(%rbp)                 # 8-byte Spill
	cmpq	$0, %rcx
	setne	%al
	andq	$3, %rcx
	cmpq	$0, %rcx
	sete	%cl
	andb	%cl, %al
	testb	$1, %al
	jne	.LBB0_36
# %bb.35:
	movq	-24(%rbp), %rdx                 # 8-byte Reload
	leaq	.L__unnamed_16(%rip), %rcx
	callq	__ubsan_handle_type_mismatch_v1
.LBB0_36:
	movq	-24(%rbp), %rcx                 # 8-byte Reload
	addq	$4, %rcx
	movq	%rcx, -40(%rbp)                 # 8-byte Spill
	cmpq	$0, %rcx
	setne	%al
	andq	$3, %rcx
	cmpq	$0, %rcx
	sete	%cl
	andb	%cl, %al
	testb	$1, %al
	jne	.LBB0_38
# %bb.37:
	movq	-40(%rbp), %rdx                 # 8-byte Reload
	leaq	.L__unnamed_17(%rip), %rcx
	callq	__ubsan_handle_type_mismatch_v1
.LBB0_38:
	movq	-40(%rbp), %rax                 # 8-byte Reload
	movl	(%rax), %eax
	movl	%eax, -52(%rbp)                 # 4-byte Spill
	movq	128(%rbp), %rcx
	movq	%rcx, -48(%rbp)                 # 8-byte Spill
	cmpq	$0, %rcx
	setne	%al
	andq	$3, %rcx
	cmpq	$0, %rcx
	sete	%cl
	andb	%cl, %al
	testb	$1, %al
	jne	.LBB0_40
# %bb.39:
	movq	-48(%rbp), %rdx                 # 8-byte Reload
	leaq	.L__unnamed_18(%rip), %rcx
	callq	__ubsan_handle_type_mismatch_v1
.LBB0_40:
	movq	-48(%rbp), %rcx                 # 8-byte Reload
	cmpq	$0, %rcx
	setne	%al
	andq	$3, %rcx
	cmpq	$0, %rcx
	sete	%cl
	andb	%cl, %al
	testb	$1, %al
	jne	.LBB0_42
# %bb.41:
	movq	-48(%rbp), %rdx                 # 8-byte Reload
	leaq	.L__unnamed_19(%rip), %rcx
	callq	__ubsan_handle_type_mismatch_v1
.LBB0_42:
	movl	28(%rbp), %r9d                  # 4-byte Reload
	movl	52(%rbp), %r8d                  # 4-byte Reload
	movq	64(%rbp), %rdx                  # 8-byte Reload
	movl	-4(%rbp), %ecx                  # 4-byte Reload
	movl	-28(%rbp), %r10d                # 4-byte Reload
	movl	-52(%rbp), %r11d                # 4-byte Reload
	movq	-48(%rbp), %rax                 # 8-byte Reload
	movl	(%rax), %esi
	movq	%rsp, %rax
	movl	%esi, 56(%rax)
	movl	%r11d, 48(%rax)
	movl	%r10d, 40(%rax)
	movl	%ecx, 32(%rax)
	leaq	.L.str.2(%rip), %rcx
	callq	printf
	.cv_loc	0 1 25 0                        # untitled4.c:25:0
	xorl	%eax, %eax
	movl	%eax, -56(%rbp)                 # 4-byte Spill
	movq	160(%rbp), %rcx
	xorq	%rbp, %rcx
	movq	.refptr.__stack_chk_guard(%rip), %rax
	movq	(%rax), %rax
	subq	%rcx, %rax
	jne	.LBB0_44
	jmp	.LBB0_43
.LBB0_44:
	callq	__stack_chk_fail
.LBB0_43:
	movl	-56(%rbp), %eax                 # 4-byte Reload
	addq	$296, %rsp                      # imm = 0x128
	popq	%rsi
	popq	%rbp
	retq
.Ltmp5:
.Lfunc_end0:
	.seh_endproc
                                        # -- End function
	.section	.rdata,"dr"
.L.str:                                 # @.str
	.asciz	"\tmemory[%d] = 0x%02x\n"

.L.src:                                 # @.src
	.asciz	"untitled4.c"

.L.src.1:                               # @.src.1
	.asciz	"C:\\ProgramData\\chocolatey\\lib\\zig\\tools\\zig-windows-x86_64-0.14.0\\lib\\libc\\include\\any-windows-any/stdio.h"

	.data
	.p2align	4, 0x0                          # @0
.L__unnamed_1:
	.quad	.L.src
	.long	18                              # 0x12
	.long	14                              # 0xe
	.quad	.L.src.1
	.long	419                             # 0x1a3
	.long	61                              # 0x3d
	.long	1                               # 0x1
	.zero	4

	.p2align	3, 0x0                          # @1
.L__unnamed_2:
	.quad	.L.src
	.long	18                              # 0x12
	.long	44                              # 0x2c

	.section	.rdata,"dr"
	.p2align	3, 0x0                          # @2
.L__unnamed_20:
	.short	0                               # 0x0
	.short	7                               # 0x7
	.asciz	"'char'"
	.zero	1

	.data
	.p2align	4, 0x0                          # @3
.L__unnamed_3:
	.quad	.L.src
	.long	18                              # 0x12
	.long	44                              # 0x2c
	.quad	.L__unnamed_20
	.byte	0                               # 0x0
	.byte	0                               # 0x0
	.zero	6

	.section	.rdata,"dr"
	.p2align	3, 0x0                          # @4
.L__unnamed_21:
	.short	0                               # 0x0
	.short	11                              # 0xb
	.asciz	"'int'"

	.data
	.p2align	4, 0x0                          # @5
.L__unnamed_4:
	.quad	.L.src
	.long	17                              # 0x11
	.long	36                              # 0x24
	.quad	.L__unnamed_21

	.section	.rdata,"dr"
.L.str.2:                               # @.str.2
	.asciz	" (%ti) \342\227\274 %d-%d-%d \342\227\274 %02d:%02d:%02d\n"

	.data
	.p2align	4, 0x0                          # @6
.L__unnamed_5:
	.quad	.L.src
	.long	21                              # 0x15
	.long	12                              # 0xc
	.quad	.L.src.1
	.long	419                             # 0x1a3
	.long	61                              # 0x3d
	.long	1                               # 0x1
	.zero	4

	.section	.rdata,"dr"
	.p2align	3, 0x0                          # @7
.L__unnamed_22:
	.short	65535                           # 0xffff
	.short	0                               # 0x0
	.asciz	"'struct tm'"

	.data
	.p2align	4, 0x0                          # @8
.L__unnamed_6:
	.quad	.L.src
	.long	22                              # 0x16
	.long	15                              # 0xf
	.quad	.L__unnamed_22
	.byte	2                               # 0x2
	.byte	3                               # 0x3
	.zero	6

	.p2align	4, 0x0                          # @9
.L__unnamed_7:
	.quad	.L.src
	.long	22                              # 0x16
	.long	15                              # 0xf
	.quad	.L__unnamed_21
	.byte	2                               # 0x2
	.byte	0                               # 0x0
	.zero	6

	.p2align	4, 0x0                          # @10
.L__unnamed_8:
	.quad	.L.src
	.long	22                              # 0x16
	.long	22                              # 0x16
	.quad	.L__unnamed_21

	.p2align	4, 0x0                          # @11
.L__unnamed_9:
	.quad	.L.src
	.long	22                              # 0x16
	.long	33                              # 0x21
	.quad	.L__unnamed_22
	.byte	2                               # 0x2
	.byte	3                               # 0x3
	.zero	6

	.p2align	4, 0x0                          # @12
.L__unnamed_10:
	.quad	.L.src
	.long	22                              # 0x16
	.long	33                              # 0x21
	.quad	.L__unnamed_21
	.byte	2                               # 0x2
	.byte	0                               # 0x0
	.zero	6

	.p2align	4, 0x0                          # @13
.L__unnamed_11:
	.quad	.L.src
	.long	22                              # 0x16
	.long	39                              # 0x27
	.quad	.L__unnamed_21

	.p2align	4, 0x0                          # @14
.L__unnamed_12:
	.quad	.L.src
	.long	22                              # 0x16
	.long	47                              # 0x2f
	.quad	.L__unnamed_22
	.byte	2                               # 0x2
	.byte	3                               # 0x3
	.zero	6

	.p2align	4, 0x0                          # @15
.L__unnamed_13:
	.quad	.L.src
	.long	22                              # 0x16
	.long	47                              # 0x2f
	.quad	.L__unnamed_21
	.byte	2                               # 0x2
	.byte	0                               # 0x0
	.zero	6

	.p2align	4, 0x0                          # @16
.L__unnamed_14:
	.quad	.L.src
	.long	23                              # 0x17
	.long	11                              # 0xb
	.quad	.L__unnamed_22
	.byte	2                               # 0x2
	.byte	3                               # 0x3
	.zero	6

	.p2align	4, 0x0                          # @17
.L__unnamed_15:
	.quad	.L.src
	.long	23                              # 0x17
	.long	11                              # 0xb
	.quad	.L__unnamed_21
	.byte	2                               # 0x2
	.byte	0                               # 0x0
	.zero	6

	.p2align	4, 0x0                          # @18
.L__unnamed_16:
	.quad	.L.src
	.long	23                              # 0x17
	.long	24                              # 0x18
	.quad	.L__unnamed_22
	.byte	2                               # 0x2
	.byte	3                               # 0x3
	.zero	6

	.p2align	4, 0x0                          # @19
.L__unnamed_17:
	.quad	.L.src
	.long	23                              # 0x17
	.long	24                              # 0x18
	.quad	.L__unnamed_21
	.byte	2                               # 0x2
	.byte	0                               # 0x0
	.zero	6

	.p2align	4, 0x0                          # @20
.L__unnamed_18:
	.quad	.L.src
	.long	23                              # 0x17
	.long	36                              # 0x24
	.quad	.L__unnamed_22
	.byte	2                               # 0x2
	.byte	3                               # 0x3
	.zero	6

	.p2align	4, 0x0                          # @21
.L__unnamed_19:
	.quad	.L.src
	.long	23                              # 0x17
	.long	36                              # 0x24
	.quad	.L__unnamed_21
	.byte	2                               # 0x2
	.byte	0                               # 0x0
	.zero	6

	.section	.rdata$.refptr.__stack_chk_guard,"dr",discard,.refptr.__stack_chk_guard
	.p2align	3, 0x0
	.globl	.refptr.__stack_chk_guard
.refptr.__stack_chk_guard:
	.quad	__stack_chk_guard
	.section	.debug$S,"dr"
	.p2align	2, 0x0
	.long	4                               # Debug section magic
	.long	241
	.long	.Ltmp7-.Ltmp6                   # Subsection size
.Ltmp6:
	.short	.Ltmp9-.Ltmp8                   # Record length
.Ltmp8:
	.short	4353                            # Record kind: S_OBJNAME
	.long	0                               # Signature
	.asciz	"C:/Users/User/AppData/Local/zig/tmp/7cbfee9d02704fac-untitled4.s" # Object name
	.p2align	2, 0x0
.Ltmp9:
	.short	.Ltmp11-.Ltmp10                 # Record length
.Ltmp10:
	.short	4412                            # Record kind: S_COMPILE3
	.long	0                               # Flags and language
	.short	208                             # CPUType
	.short	19                              # Frontend version
	.short	1
	.short	7
	.short	0
	.short	19017                           # Backend version
	.short	0
	.short	0
	.short	0
	.asciz	"clang version 19.1.7 (https://github.com/ziglang/zig-bootstrap 1c3c59435891bc9caf8cd1d3783773369d191c5f)" # Null-terminated compiler version string
	.p2align	2, 0x0
.Ltmp11:
.Ltmp7:
	.p2align	2, 0x0
	.long	241                             # Symbol subsection for main
	.long	.Ltmp13-.Ltmp12                 # Subsection size
.Ltmp12:
	.short	.Ltmp15-.Ltmp14                 # Record length
.Ltmp14:
	.short	4423                            # Record kind: S_GPROC32_ID
	.long	0                               # PtrParent
	.long	0                               # PtrEnd
	.long	0                               # PtrNext
	.long	.Lfunc_end0-main                # Code size
	.long	0                               # Offset after prologue
	.long	0                               # Offset before epilogue
	.long	4098                            # Function type index
	.secrel32	main                    # Function section relative address
	.secidx	main                            # Function section index
	.byte	193                             # Flags
	.asciz	"main"                          # Function name
	.p2align	2, 0x0
.Ltmp15:
	.short	.Ltmp17-.Ltmp16                 # Record length
.Ltmp16:
	.short	4114                            # Record kind: S_FRAMEPROC
	.long	304                             # FrameSize
	.long	0                               # Padding
	.long	0                               # Offset of padding
	.long	8                               # Bytes of callee saved registers
	.long	0                               # Exception handler offset
	.short	0                               # Exception handler section
	.long	168192                          # Flags (defines frame register)
	.p2align	2, 0x0
.Ltmp17:
	.short	.Ltmp19-.Ltmp18                 # Record length
.Ltmp18:
	.short	4414                            # Record kind: S_LOCAL
	.long	117                             # TypeIndex
	.short	0                               # Flags
	.asciz	"x"
	.p2align	2, 0x0
.Ltmp19:
	.cv_def_range	 .Ltmp0 .Ltmp5, frame_ptr_rel, 156
	.short	.Ltmp21-.Ltmp20                 # Record length
.Ltmp20:
	.short	4414                            # Record kind: S_LOCAL
	.long	19                              # TypeIndex
	.short	0                               # Flags
	.asciz	"t0"
	.p2align	2, 0x0
.Ltmp21:
	.cv_def_range	 .Ltmp0 .Ltmp5, frame_ptr_rel, 144
	.short	.Ltmp23-.Ltmp22                 # Record length
.Ltmp22:
	.short	4414                            # Record kind: S_LOCAL
	.long	4100                            # TypeIndex
	.short	0                               # Flags
	.asciz	"tm"
	.p2align	2, 0x0
.Ltmp23:
	.cv_def_range	 .Ltmp0 .Ltmp5, frame_ptr_rel, 128
	.short	.Ltmp25-.Ltmp24                 # Record length
.Ltmp24:
	.short	4355                            # Record kind: S_BLOCK32
	.long	0                               # PtrParent
	.long	0                               # PtrEnd
	.long	.Ltmp4-.Ltmp1                   # Code size
	.secrel32	.Ltmp1                  # Function section relative address
	.secidx	.Lfunc_begin0                   # Function section index
	.byte	0                               # Lexical block name
	.p2align	2, 0x0
.Ltmp25:
	.short	.Ltmp27-.Ltmp26                 # Record length
.Ltmp26:
	.short	4414                            # Record kind: S_LOCAL
	.long	116                             # TypeIndex
	.short	0                               # Flags
	.asciz	"i"
	.p2align	2, 0x0
.Ltmp27:
	.cv_def_range	 .Ltmp1 .Ltmp4, frame_ptr_rel, 124
	.short	2                               # Record length
	.short	6                               # Record kind: S_END
	.short	2                               # Record length
	.short	4431                            # Record kind: S_PROC_ID_END
.Ltmp13:
	.p2align	2, 0x0
	.cv_linetable	0, main, .Lfunc_end0
	.long	241
	.long	.Ltmp29-.Ltmp28                 # Subsection size
.Ltmp28:
	.short	.Ltmp31-.Ltmp30                 # Record length
.Ltmp30:
	.short	4360                            # Record kind: S_UDT
	.long	117                             # Type
	.asciz	"uint32_t"
	.p2align	2, 0x0
.Ltmp31:
	.short	.Ltmp33-.Ltmp32                 # Record length
.Ltmp32:
	.short	4360                            # Record kind: S_UDT
	.long	19                              # Type
	.asciz	"__time64_t"
	.p2align	2, 0x0
.Ltmp33:
	.short	.Ltmp35-.Ltmp34                 # Record length
.Ltmp34:
	.short	4360                            # Record kind: S_UDT
	.long	19                              # Type
	.asciz	"time_t"
	.p2align	2, 0x0
.Ltmp35:
	.short	.Ltmp37-.Ltmp36                 # Record length
.Ltmp36:
	.short	4360                            # Record kind: S_UDT
	.long	4102                            # Type
	.asciz	"tm"
	.p2align	2, 0x0
.Ltmp37:
.Ltmp29:
	.p2align	2, 0x0
	.cv_filechecksums                       # File index to string table offset subsection
	.cv_stringtable                         # String table
	.long	241
	.long	.Ltmp39-.Ltmp38                 # Subsection size
.Ltmp38:
	.short	.Ltmp41-.Ltmp40                 # Record length
.Ltmp40:
	.short	4428                            # Record kind: S_BUILDINFO
	.long	4110                            # LF_BUILDINFO index
	.p2align	2, 0x0
.Ltmp41:
.Ltmp39:
	.p2align	2, 0x0
	.section	.debug$T,"dr"
	.p2align	2, 0x0
	.long	4                               # Debug section magic
	# ArgList (0x1000)
	.short	0x6                             # Record length
	.short	0x1201                          # Record kind: LF_ARGLIST
	.long	0x0                             # NumArgs
	# Procedure (0x1001)
	.short	0xe                             # Record length
	.short	0x1008                          # Record kind: LF_PROCEDURE
	.long	0x74                            # ReturnType: int
	.byte	0x0                             # CallingConvention: NearC
	.byte	0x0                             # FunctionOptions
	.short	0x0                             # NumParameters
	.long	0x1000                          # ArgListType: ()
	# FuncId (0x1002)
	.short	0x12                            # Record length
	.short	0x1601                          # Record kind: LF_FUNC_ID
	.long	0x0                             # ParentScope
	.long	0x1001                          # FunctionType: int ()
	.asciz	"main"                          # Name
	.byte	243
	.byte	242
	.byte	241
	# Struct (0x1003)
	.short	0x1a                            # Record length
	.short	0x1505                          # Record kind: LF_STRUCTURE
	.short	0x0                             # MemberCount
	.short	0x80                            # Properties ( ForwardReference (0x80) )
	.long	0x0                             # FieldList
	.long	0x0                             # DerivedFrom
	.long	0x0                             # VShape
	.short	0x0                             # SizeOf
	.asciz	"tm"                            # Name
	.byte	243
	.byte	242
	.byte	241
	# Pointer (0x1004)
	.short	0xa                             # Record length
	.short	0x1002                          # Record kind: LF_POINTER
	.long	0x1003                          # PointeeType: tm
	.long	0x1000c                         # Attrs: [ Type: Near64, Mode: Pointer, SizeOf: 8 ]
	# FieldList (0x1005)
	.short	0xb6                            # Record length
	.short	0x1203                          # Record kind: LF_FIELDLIST
	.short	0x150d                          # Member kind: DataMember ( LF_MEMBER )
	.short	0x3                             # Attrs: Public
	.long	0x74                            # Type: int
	.short	0x0                             # FieldOffset
	.asciz	"tm_sec"                        # Name
	.byte	243
	.byte	242
	.byte	241
	.short	0x150d                          # Member kind: DataMember ( LF_MEMBER )
	.short	0x3                             # Attrs: Public
	.long	0x74                            # Type: int
	.short	0x4                             # FieldOffset
	.asciz	"tm_min"                        # Name
	.byte	243
	.byte	242
	.byte	241
	.short	0x150d                          # Member kind: DataMember ( LF_MEMBER )
	.short	0x3                             # Attrs: Public
	.long	0x74                            # Type: int
	.short	0x8                             # FieldOffset
	.asciz	"tm_hour"                       # Name
	.byte	242
	.byte	241
	.short	0x150d                          # Member kind: DataMember ( LF_MEMBER )
	.short	0x3                             # Attrs: Public
	.long	0x74                            # Type: int
	.short	0xc                             # FieldOffset
	.asciz	"tm_mday"                       # Name
	.byte	242
	.byte	241
	.short	0x150d                          # Member kind: DataMember ( LF_MEMBER )
	.short	0x3                             # Attrs: Public
	.long	0x74                            # Type: int
	.short	0x10                            # FieldOffset
	.asciz	"tm_mon"                        # Name
	.byte	243
	.byte	242
	.byte	241
	.short	0x150d                          # Member kind: DataMember ( LF_MEMBER )
	.short	0x3                             # Attrs: Public
	.long	0x74                            # Type: int
	.short	0x14                            # FieldOffset
	.asciz	"tm_year"                       # Name
	.byte	242
	.byte	241
	.short	0x150d                          # Member kind: DataMember ( LF_MEMBER )
	.short	0x3                             # Attrs: Public
	.long	0x74                            # Type: int
	.short	0x18                            # FieldOffset
	.asciz	"tm_wday"                       # Name
	.byte	242
	.byte	241
	.short	0x150d                          # Member kind: DataMember ( LF_MEMBER )
	.short	0x3                             # Attrs: Public
	.long	0x74                            # Type: int
	.short	0x1c                            # FieldOffset
	.asciz	"tm_yday"                       # Name
	.byte	242
	.byte	241
	.short	0x150d                          # Member kind: DataMember ( LF_MEMBER )
	.short	0x3                             # Attrs: Public
	.long	0x74                            # Type: int
	.short	0x20                            # FieldOffset
	.asciz	"tm_isdst"                      # Name
	.byte	241
	# Struct (0x1006)
	.short	0x1a                            # Record length
	.short	0x1505                          # Record kind: LF_STRUCTURE
	.short	0x9                             # MemberCount
	.short	0x0                             # Properties
	.long	0x1005                          # FieldList: <field list>
	.long	0x0                             # DerivedFrom
	.long	0x0                             # VShape
	.short	0x24                            # SizeOf
	.asciz	"tm"                            # Name
	.byte	243
	.byte	242
	.byte	241
	# StringId (0x1007)
	.short	0x72                            # Record length
	.short	0x1605                          # Record kind: LF_STRING_ID
	.long	0x0                             # Id
	.asciz	"C:\\ProgramData\\chocolatey\\lib\\zig\\tools\\zig-windows-x86_64-0.14.0\\lib\\libc\\include\\any-windows-any\\time.h" # StringData
	.byte	242
	.byte	241
	# UdtSourceLine (0x1008)
	.short	0xe                             # Record length
	.short	0x1606                          # Record kind: LF_UDT_SRC_LINE
	.long	0x1006                          # UDT: tm
	.long	0x1007                          # SourceFile: C:\ProgramData\chocolatey\lib\zig\tools\zig-windows-x86_64-0.14.0\lib\libc\include\any-windows-any\time.h
	.long	0x64                            # LineNumber
	# StringId (0x1009)
	.short	0x1e                            # Record length
	.short	0x1605                          # Record kind: LF_STRING_ID
	.long	0x0                             # Id
	.asciz	"C:/dev/code/learning/c"        # StringData
	.byte	241
	# StringId (0x100A)
	.short	0x12                            # Record length
	.short	0x1605                          # Record kind: LF_STRING_ID
	.long	0x0                             # Id
	.asciz	"untitled4.c"                   # StringData
	# StringId (0x100B)
	.short	0xa                             # Record length
	.short	0x1605                          # Record kind: LF_STRING_ID
	.long	0x0                             # Id
	.byte	0                               # StringData
	.byte	243
	.byte	242
	.byte	241
	# StringId (0x100C)
	.short	0x52                            # Record length
	.short	0x1605                          # Record kind: LF_STRING_ID
	.long	0x0                             # Id
	.asciz	"C:/ProgramData/chocolatey/lib/zig/tools/zig-windows-x86_64-0.14.0/zig.exe" # StringData
	.byte	242
	.byte	241
	# StringId (0x100D)
	.short	0x20a6                          # Record length
	.short	0x1605                          # Record kind: LF_STRING_ID
	.long	0x0                             # Id
	.asciz	"\"-cc1\" \"-triple\" \"x86_64-unknown-windows-gnu\" \"-S\" \"-disable-free\" \"-clear-ast-before-backend\" \"-disable-llvm-verifier\" \"-discard-value-names\" \"-mrelocation-model\" \"pic\" \"-pic-level\" \"2\" \"-mframe-pointer=all\" \"-fmath-errno\" \"-ffp-contract=on\" \"-fno-rounding-math\" \"-mconstructor-aliases\" \"-mms-bitfields\" \"-funwind-tables=2\" \"-fno-sized-deallocation\" \"-fno-use-init-array\" \"-target-cpu\" \"x86-64\" \"-tune-cpu\" \"generic\" \"-gno-column-info\" \"-gcodeview\" \"-debug-info-kind=constructor\" \"-debugger-tuning=gdb\" \"-fdebug-compilation-dir=C:/dev/code/learning/c\" \"-fcoverage-compilation-dir=C:/dev/code/learning/c\" \"-nostdsysteminc\" \"-nobuiltininc\" \"-resource-dir\" \"C:/ProgramData/chocolatey/lib/zig/tools/lib/clang/19\" \"-dependency-file\" \"C:\\\\Users\\\\User\\\\AppData\\\\Local\\\\zig\\\\tmp\\\\7cbfee9d02704fac-untitled4.s.d\" \"-MT\" \"C:\\\\Users\\\\User\\\\AppData\\\\Local\\\\zig\\\\tmp\\\\7cbfee9d02704fac-untitled4.s\" \"-sys-header-deps\" \"-MV\" \"-isystem\" \"C:\\\\ProgramData\\\\chocolatey\\\\lib\\\\zig\\\\tools\\\\zig-windows-x86_64-0.14.0\\\\lib\\\\include\" \"-isystem\" \"C:\\\\ProgramData\\\\chocolatey\\\\lib\\\\zig\\\\tools\\\\zig-windows-x86_64-0.14.0\\\\lib\\\\libc\\\\include\\\\x86_64-windows-gnu\" \"-isystem\" \"C:\\\\ProgramData\\\\chocolatey\\\\lib\\\\zig\\\\tools\\\\zig-windows-x86_64-0.14.0\\\\lib\\\\libc\\\\include\\\\generic-mingw\" \"-isystem\" \"C:\\\\ProgramData\\\\chocolatey\\\\lib\\\\zig\\\\tools\\\\zig-windows-x86_64-0.14.0\\\\lib\\\\libc\\\\include\\\\x86_64-windows-any\" \"-isystem\" \"C:\\\\ProgramData\\\\chocolatey\\\\lib\\\\zig\\\\tools\\\\zig-windows-x86_64-0.14.0\\\\lib\\\\libc\\\\include\\\\any-windows-any\" \"-D\" \"__MSVCRT_VERSION__=0xE00\" \"-D\" \"_WIN32_WINNT=0x0a00\" \"-D\" \"_DEBUG\" \"-O0\" \"-Wno-pragma-pack\" \"-ferror-limit\" \"19\" \"-fsanitize=alignment,array-bounds,bool,builtin,enum,float-cast-overflow,integer-divide-by-zero,nonnull-attribute,null,pointer-overflow,return,returns-nonnull-attribute,shift-base,shift-exponent,signed-integer-overflow,unreachable,vla-bound\" \"-fsanitize-recover=alignment,array-bounds,bool,builtin,enum,float-cast-overflow,integer-divide-by-zero,nonnull-attribute,null,pointer-overflow,returns-nonnull-attribute,shift-base,shift-exponent,signed-integer-overflow,vla-bound\" \"-fno-sanitize-memory-param-retval\" \"-fno-sanitize-address-use-odr-indicator\" \"-stack-protector\" \"2\" \"-stack-protector-buffer-size\" \"4\" \"-fno-use-cxa-atexit\" \"-fgnuc-version=4.2.1\" \"-fskip-odr-check-in-gmf\" \"-exception-model=seh\" \"-fcolor-diagnostics\" \"-fno-spell-checking\" \"-target-cpu\" \"tigerlake\" \"-target-feature\" \"-16bit-mode\" \"-target-feature\" \"-32bit-mode\" \"-target-feature\" \"+64bit\" \"-target-feature\" \"+adx\" \"-target-feature\" \"+aes\" \"-target-feature\" \"+allow-light-256-bit\" \"-target-feature\" \"-amx-bf16\" \"-target-feature\" \"-amx-complex\" \"-target-feature\" \"-amx-fp16\" \"-target-feature\" \"-amx-int8\" \"-target-feature\" \"-amx-tile\" \"-target-feature\" \"+avx\" \"-target-feature\" \"-avx10.1-256\" \"-target-feature\" \"-avx10.1-512\" \"-target-feature\" \"+avx2\" \"-target-feature\" \"-avx512bf16\" \"-target-feature\" \"+avx512bitalg\" \"-target-feature\" \"+avx512bw\" \"-target-feature\" \"+avx512cd\" \"-target-feature\" \"+avx512dq\" \"-target-feature\" \"+avx512f\" \"-target-feature\" \"-avx512fp16\" \"-target-feature\" \"+avx512ifma\" \"-target-feature\" \"+avx512vbmi\" \"-target-feature\" \"+avx512vbmi2\" \"-target-feature\" \"+avx512vl\" \"-target-feature\" \"+avx512vnni\" \"-target-feature\" \"+avx512vp2intersect\" \"-target-feature\" \"+avx512vpopcntdq\" \"-target-feature\" \"-avxifma\" \"-target-feature\" \"-avxneconvert\" \"-target-feature\" \"-avxvnni\" \"-target-feature\" \"-avxvnniint16\" \"-target-feature\" \"-avxvnniint8\" \"-target-feature\" \"+bmi\" \"-target-feature\" \"+bmi2\" \"-target-feature\" \"-branch-hint\" \"-target-feature\" \"-branchfusion\" \"-target-feature\" \"-ccmp\" \"-target-feature\" \"-cf\" \"-target-feature\" \"-cldemote\" \"-target-feature\" \"+clflushopt\" \"-target-feature\" \"+clwb\" \"-target-feature\" \"-clzero\" \"-target-feature\" \"+cmov\" \"-target-feature\" \"-cmpccxadd\" \"-target-feature\" \"+crc32\" \"-target-feature\" \"+cx16\" \"-target-feature\" \"+cx8\" \"-target-feature\" \"-egpr\" \"-target-feature\" \"-enqcmd\" \"-target-feature\" \"+ermsb\" \"-target-feature\" \"+evex512\" \"-target-feature\" \"+f16c\" \"-target-feature\" \"-false-deps-getmant\" \"-target-feature\" \"-false-deps-lzcnt-tzcnt\" \"-target-feature\" \"-false-deps-mulc\" \"-target-feature\" \"-false-deps-mullq\" \"-target-feature\" \"-false-deps-perm\" \"-target-feature\" \"-false-deps-popcnt\" \"-target-feature\" \"-false-deps-range\" \"-target-feature\" \"-fast-11bytenop\" \"-target-feature\" \"+fast-15bytenop\" \"-target-feature\" \"-fast-7bytenop\" \"-target-feature\" \"-fast-bextr\" \"-target-feature\" \"-fast-dpwssd\" \"-target-feature\" \"+fast-gather\" \"-target-feature\" \"-fast-hops\" \"-target-feature\" \"-fast-imm16\" \"-target-feature\" \"-fast-lzcnt\" \"-target-feature\" \"-fast-movbe\" \"-target-feature\" \"+fast-scalar-fsqrt\" \"-target-feature\" \"-fast-scalar-shift-masks\" \"-target-feature\" \"+fast-shld-rotate\" \"-target-feature\" \"+fast-variable-crosslane-shuffle\" \"-target-feature\" \"+fast-variable-perlane-shuffle\" \"-target-feature\" \"+fast-vector-fsqrt\" \"-target-feature\" \"-fast-vector-shift-masks\" \"-target-feature\" \"-faster-shift-than-shuffle\" \"-target-feature\" \"+fma\" \"-target-feature\" \"-fma4\" \"-target-feature\" \"+fsgsbase\" \"-target-feature\" \"+fsrm\" \"-target-feature\" \"+fxsr\" \"-target-feature\" \"+gfni\" \"-target-feature\" \"-harden-sls-ijmp\" \"-target-feature\" \"-harden-sls-ret\" \"-target-feature\" \"-hreset\" \"-target-feature\" \"-idivl-to-divb\" \"-target-feature\" \"+idivq-to-divl\" \"-target-feature\" \"-inline-asm-use-gpr32\" \"-target-feature\" \"+invpcid\" \"-target-feature\" \"-kl\" \"-target-feature\" \"-lea-sp\" \"-target-feature\" \"-lea-uses-ag\" \"-target-feature\" \"-lvi-cfi\" \"-target-feature\" \"-lvi-load-hardening\" \"-target-feature\" \"-lwp\" \"-target-feature\" \"+lzcnt\" \"-target-feature\" \"+macrofusion\" \"-target-feature\" \"+mmx\" \"-target-feature\" \"+movbe\" \"-target-feature\" \"+movdir64b\" \"-target-feature\" \"+movdiri\" \"-target-feature\" \"-mwaitx\" \"-target-feature\" \"-ndd\" \"-target-feature\" \"-nf\" \"-target-feature\" \"-no-bypass-delay\" \"-target-feature\" \"+no-bypass-delay-blend\" \"-target-feature\" \"+no-bypass-delay-mov\" \"-target-feature\" \"+no-bypass-delay-shuffle\" \"-target-feature\" \"+nopl\" \"-target-feature\" \"-pad-short-functions\" \"-target-feature\" \"+pclmul\" \"-target-feature\" \"-pconfig\" \"-target-feature\" \"-pku\" \"-target-feature\" \"+popcnt\" \"-target-feature\" \"-ppx\" \"-target-feature\" \"-prefer-128-bit\" \"-target-feature\" \"+prefer-256-bit\" \"-target-feature\" \"-prefer-mask-registers\" \"-target-feature\" \"-prefer-movmsk-over-vtest\" \"-target-feature\" \"-prefer-no-gather\" \"-target-feature\" \"-prefer-no-scatter\" \"-target-feature\" \"-prefetchi\" \"-target-feature\" \"+prfchw\" \"-target-feature\" \"-ptwrite\" \"-target-feature\" \"-push2pop2\" \"-target-feature\" \"-raoint\" \"-target-feature\" \"+rdpid\" \"-target-feature\" \"-rdpru\" \"-target-feature\" \"+rdrnd\" \"-target-feature\" \"+rdseed\" \"-target-feature\" \"-retpoline\" \"-target-feature\" \"-retpoline-external-thunk\" \"-target-feature\" \"-retpoline-indirect-branches\" \"-target-feature\" \"-retpoline-indirect-calls\" \"-target-feature\" \"-rtm\" \"-target-feature\" \"+sahf\" \"-target-feature\" \"-sbb-dep-breaking\" \"-target-feature\" \"-serialize\" \"-target-feature\" \"-seses\" \"-target-feature\" \"-sgx\" \"-target-feature\" \"+sha\" \"-target-feature\" \"-sha512\" \"-target-feature\" \"+shstk\" \"-target-feature\" \"-slow-3ops-lea\" \"-target-feature\" \"-slow-incdec\" \"-target-feature\" \"-slow-lea\" \"-target-feature\" \"-slow-pmaddwd\" \"-target-feature\" \"-slow-pmulld\" \"-target-feature\" \"-slow-shld\" \"-target-feature\" \"-slow-two-mem-ops\" \"-target-feature\" \"-slow-unaligned-mem-16\" \"-target-feature\" \"-slow-unaligned-mem-32\" \"-target-feature\" \"-sm3\" \"-target-feature\" \"-sm4\" \"-target-feature\" \"+sse\" \"-target-feature\" \"+sse2\" \"-target-feature\" \"+sse3\" \"-target-feature\" \"+sse4.1\" \"-target-feature\" \"+sse4.2\" \"-target-feature\" \"-sse4a\" \"-target-feature\" \"-sse-unaligned-mem\" \"-target-feature\" \"+ssse3\" \"-target-feature\" \"-tagged-globals\" \"-target-feature\" \"-tbm\" \"-target-feature\" \"-tsxldtrk\" \"-target-feature\" \"+tuning-fast-imm-vector-shift\" \"-target-feature\" \"-uintr\" \"-target-feature\" \"-use-glm-div-sqrt-costs\" \"-target-feature\" \"-use-slm-arith-costs\" \"-target-feature\" \"-usermsr\" \"-target-feature\" \"+vaes\" \"-target-feature\" \"+vpclmulqdq\" \"-target-feature\" \"+vzeroupper\" \"-target-feature\" \"-waitpkg\" \"-target-feature\" \"-wbnoinvd\" \"-target-feature\" \"-widekl\" \"-target-feature\" \"+x87\" \"-target-feature\" \"-xop\" \"-target-feature\" \"+xsave\" \"-target-feature\" \"+xsavec\" \"-target-feature\" \"+xsaveopt\" \"-target-feature\" \"+xsaves\" \"-target-feature\" \"-zu\" \"-faddrsig\" \"-x\" \"c\"" # StringData
	# BuildInfo (0x100E)
	.short	0x1a                            # Record length
	.short	0x1603                          # Record kind: LF_BUILDINFO
	.short	0x5                             # NumArgs
	.long	0x1009                          # Argument: C:/dev/code/learning/c
	.long	0x100c                          # Argument: C:/ProgramData/chocolatey/lib/zig/tools/zig-windows-x86_64-0.14.0/zig.exe
	.long	0x100a                          # Argument: untitled4.c
	.long	0x100b                          # Argument
	.long	0x100d                          # Argument: "-cc1" "-triple" "x86_64-unknown-windows-gnu" "-S" "-disable-free" "-clear-ast-before-backend" "-disable-llvm-verifier" "-discard-value-names" "-mrelocation-model" "pic" "-pic-level" "2" "-mframe-pointer=all" "-fmath-errno" "-ffp-contract=on" "-fno-rounding-math" "-mconstructor-aliases" "-mms-bitfields" "-funwind-tables=2" "-fno-sized-deallocation" "-fno-use-init-array" "-target-cpu" "x86-64" "-tune-cpu" "generic" "-gno-column-info" "-gcodeview" "-debug-info-kind=constructor" "-debugger-tuning=gdb" "-fdebug-compilation-dir=C:/dev/code/learning/c" "-fcoverage-compilation-dir=C:/dev/code/learning/c" "-nostdsysteminc" "-nobuiltininc" "-resource-dir" "C:/ProgramData/chocolatey/lib/zig/tools/lib/clang/19" "-dependency-file" "C:\\Users\\User\\AppData\\Local\\zig\\tmp\\7cbfee9d02704fac-untitled4.s.d" "-MT" "C:\\Users\\User\\AppData\\Local\\zig\\tmp\\7cbfee9d02704fac-untitled4.s" "-sys-header-deps" "-MV" "-isystem" "C:\\ProgramData\\chocolatey\\lib\\zig\\tools\\zig-windows-x86_64-0.14.0\\lib\\include" "-isystem" "C:\\ProgramData\\chocolatey\\lib\\zig\\tools\\zig-windows-x86_64-0.14.0\\lib\\libc\\include\\x86_64-windows-gnu" "-isystem" "C:\\ProgramData\\chocolatey\\lib\\zig\\tools\\zig-windows-x86_64-0.14.0\\lib\\libc\\include\\generic-mingw" "-isystem" "C:\\ProgramData\\chocolatey\\lib\\zig\\tools\\zig-windows-x86_64-0.14.0\\lib\\libc\\include\\x86_64-windows-any" "-isystem" "C:\\ProgramData\\chocolatey\\lib\\zig\\tools\\zig-windows-x86_64-0.14.0\\lib\\libc\\include\\any-windows-any" "-D" "__MSVCRT_VERSION__=0xE00" "-D" "_WIN32_WINNT=0x0a00" "-D" "_DEBUG" "-O0" "-Wno-pragma-pack" "-ferror-limit" "19" "-fsanitize=alignment,array-bounds,bool,builtin,enum,float-cast-overflow,integer-divide-by-zero,nonnull-attribute,null,pointer-overflow,return,returns-nonnull-attribute,shift-base,shift-exponent,signed-integer-overflow,unreachable,vla-bound" "-fsanitize-recover=alignment,array-bounds,bool,builtin,enum,float-cast-overflow,integer-divide-by-zero,nonnull-attribute,null,pointer-overflow,returns-nonnull-attribute,shift-base,shift-exponent,signed-integer-overflow,vla-bound" "-fno-sanitize-memory-param-retval" "-fno-sanitize-address-use-odr-indicator" "-stack-protector" "2" "-stack-protector-buffer-size" "4" "-fno-use-cxa-atexit" "-fgnuc-version=4.2.1" "-fskip-odr-check-in-gmf" "-exception-model=seh" "-fcolor-diagnostics" "-fno-spell-checking" "-target-cpu" "tigerlake" "-target-feature" "-16bit-mode" "-target-feature" "-32bit-mode" "-target-feature" "+64bit" "-target-feature" "+adx" "-target-feature" "+aes" "-target-feature" "+allow-light-256-bit" "-target-feature" "-amx-bf16" "-target-feature" "-amx-complex" "-target-feature" "-amx-fp16" "-target-feature" "-amx-int8" "-target-feature" "-amx-tile" "-target-feature" "+avx" "-target-feature" "-avx10.1-256" "-target-feature" "-avx10.1-512" "-target-feature" "+avx2" "-target-feature" "-avx512bf16" "-target-feature" "+avx512bitalg" "-target-feature" "+avx512bw" "-target-feature" "+avx512cd" "-target-feature" "+avx512dq" "-target-feature" "+avx512f" "-target-feature" "-avx512fp16" "-target-feature" "+avx512ifma" "-target-feature" "+avx512vbmi" "-target-feature" "+avx512vbmi2" "-target-feature" "+avx512vl" "-target-feature" "+avx512vnni" "-target-feature" "+avx512vp2intersect" "-target-feature" "+avx512vpopcntdq" "-target-feature" "-avxifma" "-target-feature" "-avxneconvert" "-target-feature" "-avxvnni" "-target-feature" "-avxvnniint16" "-target-feature" "-avxvnniint8" "-target-feature" "+bmi" "-target-feature" "+bmi2" "-target-feature" "-branch-hint" "-target-feature" "-branchfusion" "-target-feature" "-ccmp" "-target-feature" "-cf" "-target-feature" "-cldemote" "-target-feature" "+clflushopt" "-target-feature" "+clwb" "-target-feature" "-clzero" "-target-feature" "+cmov" "-target-feature" "-cmpccxadd" "-target-feature" "+crc32" "-target-feature" "+cx16" "-target-feature" "+cx8" "-target-feature" "-egpr" "-target-feature" "-enqcmd" "-target-feature" "+ermsb" "-target-feature" "+evex512" "-target-feature" "+f16c" "-target-feature" "-false-deps-getmant" "-target-feature" "-false-deps-lzcnt-tzcnt" "-target-feature" "-false-deps-mulc" "-target-feature" "-false-deps-mullq" "-target-feature" "-false-deps-perm" "-target-feature" "-false-deps-popcnt" "-target-feature" "-false-deps-range" "-target-feature" "-fast-11bytenop" "-target-feature" "+fast-15bytenop" "-target-feature" "-fast-7bytenop" "-target-feature" "-fast-bextr" "-target-feature" "-fast-dpwssd" "-target-feature" "+fast-gather" "-target-feature" "-fast-hops" "-target-feature" "-fast-imm16" "-target-feature" "-fast-lzcnt" "-target-feature" "-fast-movbe" "-target-feature" "+fast-scalar-fsqrt" "-target-feature" "-fast-scalar-shift-masks" "-target-feature" "+fast-shld-rotate" "-target-feature" "+fast-variable-crosslane-shuffle" "-target-feature" "+fast-variable-perlane-shuffle" "-target-feature" "+fast-vector-fsqrt" "-target-feature" "-fast-vector-shift-masks" "-target-feature" "-faster-shift-than-shuffle" "-target-feature" "+fma" "-target-feature" "-fma4" "-target-feature" "+fsgsbase" "-target-feature" "+fsrm" "-target-feature" "+fxsr" "-target-feature" "+gfni" "-target-feature" "-harden-sls-ijmp" "-target-feature" "-harden-sls-ret" "-target-feature" "-hreset" "-target-feature" "-idivl-to-divb" "-target-feature" "+idivq-to-divl" "-target-feature" "-inline-asm-use-gpr32" "-target-feature" "+invpcid" "-target-feature" "-kl" "-target-feature" "-lea-sp" "-target-feature" "-lea-uses-ag" "-target-feature" "-lvi-cfi" "-target-feature" "-lvi-load-hardening" "-target-feature" "-lwp" "-target-feature" "+lzcnt" "-target-feature" "+macrofusion" "-target-feature" "+mmx" "-target-feature" "+movbe" "-target-feature" "+movdir64b" "-target-feature" "+movdiri" "-target-feature" "-mwaitx" "-target-feature" "-ndd" "-target-feature" "-nf" "-target-feature" "-no-bypass-delay" "-target-feature" "+no-bypass-delay-blend" "-target-feature" "+no-bypass-delay-mov" "-target-feature" "+no-bypass-delay-shuffle" "-target-feature" "+nopl" "-target-feature" "-pad-short-functions" "-target-feature" "+pclmul" "-target-feature" "-pconfig" "-target-feature" "-pku" "-target-feature" "+popcnt" "-target-feature" "-ppx" "-target-feature" "-prefer-128-bit" "-target-feature" "+prefer-256-bit" "-target-feature" "-prefer-mask-registers" "-target-feature" "-prefer-movmsk-over-vtest" "-target-feature" "-prefer-no-gather" "-target-feature" "-prefer-no-scatter" "-target-feature" "-prefetchi" "-target-feature" "+prfchw" "-target-feature" "-ptwrite" "-target-feature" "-push2pop2" "-target-feature" "-raoint" "-target-feature" "+rdpid" "-target-feature" "-rdpru" "-target-feature" "+rdrnd" "-target-feature" "+rdseed" "-target-feature" "-retpoline" "-target-feature" "-retpoline-external-thunk" "-target-feature" "-retpoline-indirect-branches" "-target-feature" "-retpoline-indirect-calls" "-target-feature" "-rtm" "-target-feature" "+sahf" "-target-feature" "-sbb-dep-breaking" "-target-feature" "-serialize" "-target-feature" "-seses" "-target-feature" "-sgx" "-target-feature" "+sha" "-target-feature" "-sha512" "-target-feature" "+shstk" "-target-feature" "-slow-3ops-lea" "-target-feature" "-slow-incdec" "-target-feature" "-slow-lea" "-target-feature" "-slow-pmaddwd" "-target-feature" "-slow-pmulld" "-target-feature" "-slow-shld" "-target-feature" "-slow-two-mem-ops" "-target-feature" "-slow-unaligned-mem-16" "-target-feature" "-slow-unaligned-mem-32" "-target-feature" "-sm3" "-target-feature" "-sm4" "-target-feature" "+sse" "-target-feature" "+sse2" "-target-feature" "+sse3" "-target-feature" "+sse4.1" "-target-feature" "+sse4.2" "-target-feature" "-sse4a" "-target-feature" "-sse-unaligned-mem" "-target-feature" "+ssse3" "-target-feature" "-tagged-globals" "-target-feature" "-tbm" "-target-feature" "-tsxldtrk" "-target-feature" "+tuning-fast-imm-vector-shift" "-target-feature" "-uintr" "-target-feature" "-use-glm-div-sqrt-costs" "-target-feature" "-use-slm-arith-costs" "-target-feature" "-usermsr" "-target-feature" "+vaes" "-target-feature" "+vpclmulqdq" "-target-feature" "+vzeroupper" "-target-feature" "-waitpkg" "-target-feature" "-wbnoinvd" "-target-feature" "-widekl" "-target-feature" "+x87" "-target-feature" "-xop" "-target-feature" "+xsave" "-target-feature" "+xsavec" "-target-feature" "+xsaveopt" "-target-feature" "+xsaves" "-target-feature" "-zu" "-faddrsig" "-x" "c"
	.byte	242
	.byte	241
	.addrsig
	.addrsig_sym _time64
	.addrsig_sym _localtime64
	.addrsig_sym printf
	.addrsig_sym __ubsan_handle_nonnull_arg
	.addrsig_sym __ubsan_handle_pointer_overflow
	.addrsig_sym __ubsan_handle_type_mismatch_v1
	.addrsig_sym __ubsan_handle_add_overflow
