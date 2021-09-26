# author: Purushottam Panta (purupanta@uky.edu)
# proj: Improved NaiveSearch v0
# last updated: 09162021
#

class NaiveSearch:
    
    def MySearch(strX = "", strY = ""):

        finalIndices = []
        xLen = len(strX)
        yLen = len(strY)

        for i in range(0, xLen-yLen+1):
            
            counter = 0
            for j in range(0, yLen):
                i_temp = i+j
                if(strX[i_temp] != strY[j]):
                    break
                else:
                    counter = counter+1

                if(counter == yLen):
                    finalIndices.append(i)

        return finalIndices

