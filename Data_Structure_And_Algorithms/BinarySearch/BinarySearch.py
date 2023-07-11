

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
import argparse
from pathlib import Path


def binarySearch(arr, left, right, target) :

    # print("current array searched : {}".format(arr[left:right+1]))

    # If arr length 1 or less
    if len(arr) == 0 :
        formatting_output(False)
        return
    elif len(arr) == 1 :
        if arr[0] == target :
            formatting_output(True, 0, target)
        else :
            formatting_output(False)
        return

    # Else :
    # if middle value is target value
    middle_index = math.floor((left + right) / 2)

    if arr[middle_index] == target :
        formatting_output(True, middle_index, target)
        return
    # Perform Recursive binary search until value found or return False if not found
    else :
        if target < arr[middle_index] :
            binarySearch(arr, left, middle_index-1, target)
        else :
            binarySearch(arr, middle_index+1, right, target)

    return


def formatting_output(found, index=None, target = None) :

    print(" ********** ********** ********** ********** **********")

    if found == False :
        print("False")
        print("Target value {} NOT FOUND in input data/array provided")
    else :
        print("True")
        print("Target value {} FOUND at index {}".format(target, index))

    print(" ********** ********** ********** ********** **********")
    print(" ********** ********** ********** ********** **********")

    return


# if __name__ == "__main__":

#     print("--------------/\\--------------")
#     print("-------------/  \\-------------")
#     print("------------/ || \\------------     ATTENTION")
#     print("-----------/  ||  \\----------- INPUT ARRAY MUST BE")
#     print("----------/   ||   \\----------    A SORTED ARRAY")
#     print("---------/    ||    \\---------")
#     print("--------/_____OO_____\\--------")

#     argParser = argparse.ArgumentParser()
#     argParser.add_argument("-i", "--input", help="input python file/script where \
#                            input set of data and target value to be found are define respectively under \
#                            \\'input_data\\' and \\'target\\' variables ")
#     args = argParser.parse_args()

#     data_file_path = Path(args.input)

#     # Confirm input path is valid
#     if data_file_path.is_file() and str(data_file_path).endswith('.py') :

#         # Retrieve data
#         exec(open(data_file_path).read())

#         input_array = locals()['input_data']
#         target_val = locals()['target']

#         # Check input values valid for binary search
#         if target_val == None  or target_val == "" :
#             print("ERROR : no valid target value provided !! target = {}".format(target_val))
#         else :
#             target_val = int(target_val)
        
#         print("Input data length : {} - target value = {}".format(len(input_array), target_val))

#         binarySearch(input_array, 0, len(input_array)-1, target_val)


if __name__ == "__main__":

    print("--------------/\\--------------")
    print("-------------/  \\-------------")
    print("------------/ || \\------------     ATTENTION")
    print("-----------/  ||  \\----------- INPUT ARRAY MUST BE")
    print("----------/   ||   \\----------    A SORTED ARRAY")
    print("---------/    ||    \\---------")
    print("--------/_____OO_____\\--------")

    input_data = [x for x in range(20, 99683467)]
    target = 5649

    # Check input values valid for binary search
    if target == None  or target == "" :
        print("ERROR : no valid target value provided !! target = {}".format(target))
        exit(1)
    
    # print("Input data length : {} - target value = {}".format(len(input_data), target))

    binarySearch(input_data, 0, len(input_data)-1, target)

    exit(0)    