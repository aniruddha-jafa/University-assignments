	.section	__TEXT,__text,regular,pure_instructions
	.globl	_sort

	# Function sort
	# Arguments:
	#   %rdi -- base address of the array
	#   %rsi -- number of elements in the array
	#
	# sort the elements of the array

_sort:
	pushq %rbx
	pushq %rbp
	pushq %r12
	pushq %r13
	pushq %r14
	pushq %r15

	# ====================
	# WRITE YOUR CODE HERE

  # this code implements bubble sort.
	# %r12: signifies i, used for loop1
	# %r13: signifies j, used for loop2, nested within loop1
	# %r14: used to index the address of the array element we're considering in the bubble sort iteration (say, k1)
	# %r15: used to the index the array element which follows the one indexed by %r14 (say, k2)

	# %rbx:
	# i)in loop1, %rbx used to hold the value 0 so that it can be compared to other registers, most notably %r12 (i)
	# ii) in the label 'update', %rbx is used to store element  k1, which is indicated by (%r14).
  #     it is also used to transfer the value of k1 to k2.

	# %rbp:
	# used to compare k1 to k2, i.e. (%r14) to (%r15). But since cmp cannot compare (%r14) and (%r15) directly, we used %rbp.


	movq %rsi, %r12  # i = n
	movq $0,%rbx      # move 0 to a register so that we can do comparisons (cmp) with 0


loop1:
	addq $-1,%r12    # i =n-1 in first iteration itself

	cmp %rbx, %r12   # check i=0.
	je done

	movq $0,%r13         #j = 0


loop2:
	cmp %r12, %r13       #see whether j=i. If so, exit.
	je loop1

	# find array[j] and array [j+1]

	movq %r13, %r14       # r14 = j
	imulq $8, %r14        # r14 = 8*j
	addq %rdi, %r14       # r14 = 8*j + base_address, { %rdi = base_address }, which is address of array[j]


	movq %r14,%r15
	addq $8,%r15             #r15 = 8*(j+1) + base_address. This gives us address of array[j+1]

	# We have address of array[j] and array[j+1]. To get the actual values, we use (%r14), and (%r15)

  # Now that we know how to find array[j] and array[j+1], compare them

	movq (%r15), %rbp        # element in array[8*(j+1)+ base_address] to register rbp, since cmp won't work with two values.
 	cmp (%r14), %rbp         # effectively compares (%r14) and (%r15), which compares array[j] and array[j+1]
	jl update								 # if array[j] > array[j+1], sign flag updated since it computes (%r15) - (%r14)

	addq $1,%r13          # j = j+1
	jmp loop2             # simulating our while loop


update:
  # Let array[j] and array[j+1] swap values.

  movq (%r14),%rbx    # if array[j] > array[j+1], move value in array[j] to array[j+1]
	movq %rbp, (%r14)   # %rbp has (%r15) i.e. array[j+1]. Move value in array[j+1] to array[j]
	movq %rbx, (%r15)   # move value is array[j], stored in %rbx, to array[j+1]


	movq $1,%r13          # j = j+1
	movq $0,%rbx          # re-initialize rbx, since it may be used in loop1.

	jmp loop2

done:
	# ====================

	popq %r15
	popq %r14
	popq %r13
	popq %r12
	popq %rbp
	popq %rbx

	retq
