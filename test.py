import numpy as np

arr = np.loadtxt("data_vector.csv")

sum = 0
sub_arr = []
temp_arr = []
for n in arr:
    sum += n
    if sum == 52:
        temp_arr.append(n)
        sub_arr.append(temp_arr)
        sum = 0
        temp_arr = []
    elif sum > 52:
        sum -= n
    else:
        temp_arr.append(n)

print(sub_arr)
print(f"Total de Sub Arrays encontrados: {len(sub_arr)}")