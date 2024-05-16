int_array = [2,7,11,15]
target = 9

result_dic = {}#hash alg to use key and value for mapping(dic in py)

for i,v in enumerate(int_array):#to extract value and index
    comp = target - v
    if comp in result_dic:
        print("Target is ",[result_dic[comp],i])
    result_dic[v] = i