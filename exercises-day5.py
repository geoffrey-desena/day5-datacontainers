#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 10:21:11 2026

@author: geoffreydesena
"""

# %% import packages

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson


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

# a. create a discrete random variable with poisson distro
# plot PMF
# plot CDF
# histogram of 1000 realizations

fig, ax = plt.subplots(1, 1)

mu = 2
lb, ub = poisson.support(mu)

mean, var, skew, kurt = poisson.stats(mu, moments='mvsk')

x = np.arange(poisson.ppf(0.01, mu),
              poisson.ppf(0.99, mu))
ax.plot(x, poisson.pmf(x, mu), 'bo', ms=8, label='poisson pmf')
ax.vlines(x, 0, poisson.pmf(x, mu), colors='b', lw=5, alpha=0.5)
ax.set_title("Exercise 1.statistics - poisson pdf")


# That was basically just the example code from the docs
# And now the cdf

fig, ax = plt.subplots(1, 1)
ax.plot(x, poisson.cdf(x, mu), 'bo', ms=8, label='poisson cdf')
ax.set_title("Exercise 1.statistics - poisson cdf")


# generate 1000 samples (help from ChatGPT)
samples = poisson.rvs(mu, size=1000)

# plot
fig, ax = plt.subplots(1, 1)

ax.hist(samples)

ax.set_title("Exercise 1.statistics - 1000 samples")

# I plausibly could have figured that out, but Chat just has something much nicer
fig, ax = plt.subplots()

ax.hist(samples, bins=range(min(samples), max(samples) + 2), 
        density=True, alpha=0.6, color='g', edgecolor='black')

ax.set_title("ChatGPT's version of Histogram of 1000 Poisson Samples")
ax.set_xlabel("Value")
ax.set_ylabel("Frequency")
x = np.arange(min(samples), max(samples) + 1)

ax.plot(x, poisson.pmf(x, mu), 'bo', ms=8, label='PMF')
ax.vlines(x, 0, poisson.pmf(x, mu), colors='b', lw=2, alpha=0.5)

ax.legend()

# %% Exercise 2. Pandas

print("My project relies heavily on pandas. I'm going to use the time to get started instead of finishing these exercises.")

# %% Exercise Bonus. Publishing code
# I have some other commitments this afternoon, and I think I'll actually do this
# as part of my project, so let's see if I can get Chat to create some boilerplate
# real quick.

# Wow. Much beauty. Chat do good. 

print("\nBonus:\nThere is now a directory called spam-eggs-math-spam with the modules of the simplemath package as structured by ChatGPT. In docs/_build, there is an html file with the documentation page. I wrote some simple docstrings and told ChatGPT to expand on them and give me the init code as well as the readme code. I did the directory/file creation manually, but I probably could've gotten Chat to do that do by asking it for commands.")

# Finally... 

# (base) geoffreydesena@Geoffreys-MacBook-Pro spam-eggs-math-spam % pip install . --user
# Processing /Users/geoffreydesena/Documents/advc-python/day5-datacontainers/spam-eggs-math-spam
#   Installing build dependencies ... done
#   Getting requirements to build wheel ... done
#   Preparing metadata (pyproject.toml) ... done
# Building wheels for collected packages: spam-eggs-math-spam
#   Building wheel for spam-eggs-math-spam (pyproject.toml) ... done
#   Created wheel for spam-eggs-math-spam: filename=spam_eggs_math_spam-1.0-py3-none-any.whl size=1159 sha256=6f1c7c638c10ff7ed736882484b68ccacc3f152771534f1b50a05f913a752126
#   Stored in directory: /Users/geoffreydesena/Library/Caches/pip/wheels/ff/92/6b/6aaf886a804644adc9c4ac210592db04ec9199ca8cd9a48eff
# Successfully built spam-eggs-math-spam
# Installing collected packages: spam-eggs-math-spam
# Successfully installed spam-eggs-math-spam-1.0

# and I did it!