from constraint import * 
problem = Problem()  C
problem.addVariable('a', range(5+1))
problem.addConstraint(lambda a, b: a + b == 5) # Tell the computer that a+b=5
problem.addConstraint(lambda a, b: a * b == 6) #tell the computer that a*b=6
print problem.getSolutions()
