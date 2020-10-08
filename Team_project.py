'''
===============================================================================
ENGR 133 Fa 2020
Assignment Information
	Assignment:     Python Project
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
import numpy as np
import matplotlib as lib
import matplotlib.pyplot as plt
# file_name = input("filename: ") #takes in a picture from the user who inputs the name of a file
variable = lib.image.imread("Coins.PNG") #matplot will read the image into an array
def greyscaleConverter(colorMatrix): #dotproduct will convert image into greyscale
    dot = np.dot(colorMatrix[...,:3], [0.2126, 0.7152, 0.0722]) #Formula for converting into greyscale, takes each term and calculates dotproduct
    return dot #returns dot product
def convolution(imageMatrix, convoluteMatrix):
    pad_length = (len(convoluteMatrix[0])-1)/2
    paddedImage = np.pad(imageMatrix, int(pad_length), mode="constant")
    finalImage = imageMatrix
    # print(imageMatrix)
    # print(paddedImage)
    # print(sk)
    
    # return paddedImage
    for row in imageMatrix:
        for pixel in row:
            pixelIndex = np.where(row == pixel)[0]+1
            rowIndex = np.where(imageMatrix == row)[0]+1
            sumOfConvolves = 0
            kernel = convoluteMatrix
            x=0
            y=0
            
            for krow in kernel:
                for kpixel in krow:
                    print(rowIndex[0])
                    # print(krow)
                    kernel[y][x] = paddedImage[rowIndex[0]+y][pixelIndex[0]+x]
                    x = x +1
                y=y+1
            print(kernel)  
            # for i in range(0, len(convoluteMatrix)):
            #     print(sumOfConvolves)
            #     sumOfConvolves += np.convolve(kernel, convoluteMatrix)
            finalImage[rowIndex-1][pixelIndex-1] = sumOfConvolves
                
    # print(finalImage)
                
            
            
        
             
sk = [[1,1,1],[1,1,1],[1,1,1]]

    
greyscalematrix = greyscaleConverter(variable)
blurred = convolution(greyscalematrix,sk)
# plt.imshow(blurred, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
# plt.show()


'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''
