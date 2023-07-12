

'''
    input : 
        - input comes as a python script path, which content is as follow :
            - input_data var, holding input array of SORTED data where target is to be found
            - target var, holding target value to be found
    output :
        - True : target found
        - False : target not found
'''

import math
import random


def mergeSort(arr) :

    # If arr length 1 or less
    if len(arr) < 2 :
        return arr
    
    middleIndex = math.floor(len(arr)/2)
    leftArr = arr[0:middleIndex]
    rightArr = arr[middleIndex:len(arr)]
 
    return merge(mergeSort(leftArr), mergeSort(rightArr))


def merge(leftArr, rightArr) :

    leftIndex = 0
    rightIndex = 0
    resultArr = []

    while ((leftIndex < len(leftArr)) and (rightIndex < len(rightArr))) :
        if (leftArr[leftIndex] < rightArr[rightIndex]) :
            resultArr.append(leftArr[leftIndex])
            leftIndex += 1
        else :
            resultArr.append(rightArr[rightIndex])
            rightIndex += 1

    resultArr = resultArr + leftArr[leftIndex:] + rightArr[rightIndex:]

    return resultArr


# if __name__ == "__main__":

#     argParser = argparse.ArgumentParser()
#     argParser.add_argument("-i", "--input", help="input python file/script where \
#                            input array to be sorted is expected to be defined under \
#                            \\'input_data\\' variable ")
#     args = argParser.parse_args()

#     data_file_path = Path(args.input)

#     # Confirm input path is valid
#     if data_file_path.is_file() and str(data_file_path).endswith('.py') :

#         # Retrieve data
#         exec(open(data_file_path).read())

#         input_array = locals()['input_data']

#         # Perform MergeSort
#         sorted_array = mergeSort(input_array)

#         print("********** ********** ********** ********** **********")
#         print("********** ***** S.O.R.T.E.D A.R.R.A.Y **** **********")
#         print(sorted_array)
#         print("********** ********** ********** ********** **********")
#         
#         exit(0)


if __name__ == "__main__":

    #input_data = [56, 204, 1, 39, 0, 56, 4, 8, 109, 5, 9, 97, 3, 2, 67]
    input_data = [random.randint(0,999) for x in range(15)]
    #input_data = [7]
    #input_data = []

    print("********** ********** ********** ********** **********")
    print("********** ****** I.N.P.U.T A.R.R.A.Y ***** **********")
    print(input_data)
    print("********** ********** ********** ********** **********")

    # This basic check is performed here in this way, for the sake of this demonstrative script
    # but same check is repeated in the actual mergeSort function as it would in a real case scenario configuration
    if len(input_data) == 0 :
        print("Empty Array : nothing to be sorted !!")
        exit(0)
    if len(input_data) == 1 :
        print("Array of size 1 : already sorted !!")
        exit(0)

    resultArr = mergeSort(input_data)

    print("********** ***** S.O.R.T.E.D A.R.R.A.Y **** **********")
    print(resultArr)
    print("********** ********** ********** ********** **********")

    exit(0)