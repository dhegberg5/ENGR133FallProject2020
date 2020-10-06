'''
===============================================================================
ENGR 133 Fa 2020
Assignment Information
	Assignment:     Py4 Task 4
	Author:         Tejas Chandrasekhar, tlchandr@purdue.edu
                    Zachary Chen, chen3652@purdue 
                    Rajan Phadnis, rphadnis@purdue 
                    David Hegeburg, dhegberg@purdue 
	Team ID:        LC3-05 
	
	My contributor(s) helped me:	
	[ ] understand the assignment expectations without
		telling me how they will approach it.
	[ ] understand different ways to think about a solution
		without helping me plan my solution.
	[ ] think through the meaning of a specific error or
		bug present in my code without looking at my code.
	Note that if you helped somebody else with their code, you
	have to list that person as a contributor here as well.
===============================================================================
'''
import numpy
import matplotlib as lib
import matplotlib.pyplot as plt
file_name = input("filename: ") #takes in a picture from the user who inputs the name of a file
variable = lib.image.imread(file_name) #matplot will read the image into an array
def dotproduct(color): #dotproduct will convert image into greyscale
    dot = numpy.dot(color[...,:3], [0.2989, 0.587, 0.114]) #Formula for converting into greyscale, takes each term and calculates dotproduct
    return dot #returns dot product

greyscalematrix = dotproduct(variable)

plt.imshow(greyscalematrix, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
plt.show()


'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''
