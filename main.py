#Сортировка с помощью двоичного дерева
zed = [1,23,11,43,5,57,12]
def sort_sliyaniye(massive):
    if len(massive)>2:
        left_sort=sort_sliyaniye(massive[:len(massive)//2])
        right_sort = sort_sliyaniye(massive[len(massive) // 2:])
        massive=left_sort+right_sort
        max_index=len(massive)-1
        for x in range(max_index):
            min=x
            minmassive=massive[x]
            for f in range(x+1,max_index+1):
                if minmassive>massive[f]:
                    minmassive=massive[f]
                    min=f
            if min!=x:
                massive[x],massive[min]=massive[min],massive[x]

    elif len(massive)>1:
        if massive[0]>massive[1]:
            massive[0],massive[1]=massive[1],massive[0]
    return massive
print(sort_sliyaniye(zed))
