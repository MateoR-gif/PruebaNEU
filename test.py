

def BuscarArrays(arr):
    sum = 0
    sub_arr = []
    temp_arr = []
    arr_id = 1
    for n in arr:
        sum += n
        if sum == 52:
            temp_arr.append(n)
            sub_arr.append({"arr_id": arr_id, "sub_arr": temp_arr})
            arr_id += 1
            sum = 0
            temp_arr = []
        elif sum > 52:
            sum -= n
        else:
            temp_arr.append(n)
    return sub_arr

