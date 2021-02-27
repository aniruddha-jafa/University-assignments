	.section	__TEXT,__text,regular,pure_instructions
	.globl	_max


  # goal: output the biggest element in the array

	# Function max
	# Arguments:
	#   %rdi -- base address of the array
	#   %rsi -- number of elements in the array
	# Return:
	#   %rax -- max of the elements of the array


_max:
	pushq %rbx
	pushq %rbp
	pushq %r12
	pushq %r13
	pushq %r14
	pushq %r15

	# ====================
	# WRITE YOUR CODE HERE


	  # initializing max = 0, i =0

		movq $0, %rax
		movq $0, %r12



	loop:
		cmp %rsi, %r12    # check whether i < n.  we need i from 0 to (n-1) for n elements in array [x1,x2......xn]
		je done           # condition: equal. Zero Flag. If i=n, we're done.


		# compute array[i] = value at base_address + 8*i

		movq %r12, %r14       # r14 = i
		imulq $8, %r14        # r14 = 8*i
		addq %rdi, %r14       # r14 = 8*i + base_address, { %rdi = base_address }

    # If xi > max, let max = xi.  Here  xi = (%r14), max = %rax

		cmp (%r14), %rax           # internally %rax - (%r14)
		jl update                  # check whether sign flag activated i.e. if %rax - (%r14) gave a negative value.



    # increment i

		addq $1, %r12
		jmp loop


	update:
	  # let max = xi
	  movq (%r14),%rax

		# increment i before going back to the loop

		addq $1, %r12
		jmp loop


	done:

	# ====================

	popq %r15
	popq %r14
	popq %r13
	popq %r12
	popq %rbp
	popq %rbx

	retq
