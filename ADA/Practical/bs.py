def binsearch(array,start,end,x):
    if start<=end:
        mid=(start+end)//2
        if array[mid]==x:
            return mid
        elif x<array[mid]:
            return binsearch(array=array,start=start,end=mid-1,x=x)
        elif x>array[mid]:
            return binsearch(array=array,start=mid+1,end=end,x=x)
        else:
            return -1
    else:
        return -1


print(binsearch([1,2,3,4,6,9],0,5,9))
