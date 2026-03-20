#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 10:21:11 2026

@author: geoffreydesena
"""

# %% import packages

import scipy as sp
import numpy as np

# %% Exercise 1: scipy

# a. define a matrix
# I was unsure about this so I asked ChatGPT. It encouraged me to use 
# np for setting up the arrays and scipy.linalg for the operation.
# That makes sense to me, but I was reluctant because I was unsure about
# combining the two.

# Was there a different way intended?
A = np.array([
     [1, -2, 3],
     [4, 5, 6],
     [7, 1, 9]
])
print(f"Part a: \n{A}\n")

# b. define b vector
b = np.array([1,2,3])
print(f"Part b: \n{b}\n")


# c. solve Ax=b
x = sp.linalg.solve(A,b)
print(f"Part c: \n{x}\n")

# d. check answer
b_check = np.matmul(A,x)
print(f"Part d: \nCheck that this is the same as in part b: \n{b_check}\n")

# e. Repeat but with a random matrix B
B = np.random.rand(3,3)
print(f"Part e: \nA random matrix: \n{B}\n")

x_parte = sp.linalg.solve(A,B)

B_check = np.matmul(A,x_parte)
print(f"Is this matrix the same as above? \n{B_check}\n")
# I could probably use some assert test, but then I would either need to round
# or give it an acceptable range
# That's more work than I want to put into this
# Visual inspection says yes.

# f. Eigenvalues and eigenvectors of A
A_eigs = sp.linalg.eig(A)
print(f"Part f:\nThe eigenvalues of A are \n{A_eigs[0]}\n")
print(f"The eigenectors of A are \n{A_eigs[1]}\n")

# g. Calculate the inverse, determinant of A
# I'm a bit unsure of what is desired, so I'm going to find both the
# inverse and then the determinant

# inverse
Ainv = sp.linalg.inv(A)
print(f"Part g: \nThe inverse of \n{A}\n is \n{Ainv}\n")
A_check = np.matmul(A,Ainv)
print(f"If that was correct, this is an identity matrix: \n{A_check}")
print("Close enough...\n")

# determinant
Adet = sp.linalg.det(A)
print(f"The determinant of \n{A}\n is \n{Adet}")
print("I'm not doing that by hand, so I'm just going to trust it.\n")

# h. norm of A
# I don't know what a norm is, but linalg has a norm function, 
# so let's see what comes out.
# Is it sad that an engineering PhD students doesn't know what a matrix norm is?

Anorm_fro = sp.linalg.norm(A)
Anorm_nuc = sp.linalg.norm(A,'nuc')
Anorm_inf = sp.linalg.norm(A,np.inf)

print(f"Part h: \nThe Frobenius, nuclear, and infinite norms of matrix A: \n{Anorm_fro}\n{Anorm_nuc}\n{Anorm_inf}\n")


# %% Exercise 1.statistics

