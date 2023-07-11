

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


def mergeSort(arr, startI, endI) :

    # If arr length 1 or less
    if len(arr) == 0 :
        return
    if len(arr[startI:endI+1]) == 1 :
        return
 
    
    if (startI < endI) :
    
        middleI = math.floor((startI + endI) / 2)

        # Divide each side of array until divided arrays are of size 1, then Conquer by sorting + merging back

        # Divide left side of array
        mergeSort(arr, startI, middleI)

        # Divide right side of array
        mergeSort(arr, middleI+1, endI)

        # Then Conquer : sort + merge
        merge(arr, startI, middleI, endI)

    return


def merge(array, left_index, middle_index, right_index) :

    i = left_index
    j = middle_index+1
    tmp = []

    while((i < middle_index+1) and (j < right_index+1)) :
        if array[i] < array[j]:
            tmp.append(array[i])
            i+=1
        else :
            tmp.append(array[j])
            j+=1

    while(i < middle_index+1) :
        tmp.append(array[i])
        i+=1
    
    while(j < right_index+1) :
        tmp.append(array[j])
        j+=1

    # Save sorting
    m = left_index
    n = 0
    while ( (m < right_index+1) and (n < ((right_index - left_index)+1)) ) :
        array[m] = tmp[n]
        n +=1
        m +=1

    return


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

    mergeSort(input_data, 0, len(input_data)-1)

    print("********** ***** S.O.R.T.E.D A.R.R.A.Y **** **********")
    print(input_data)
    print("********** ********** ********** ********** **********")

    exit(0)