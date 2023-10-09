#define a function named subarray.
def subarray(l):
    #using if statement to specify that if l is not there return 0.
    if not l:
        return 0
#define two variables msum and csum with the same values as the value with index 0 in l.
    msum = l[0]
    csum = l[0]

#using for loop to iterate a variable i in the whole lenght of the list l.
    for i in l[1:]:
        #using the max statements to get the current max and comparing it with maxsum to get the overall max sum.
        csum = max(i, csum + i)
        msum = max(msum, csum)

    return msum

#define a list l.
l = [-2, 1, -5, 5, -1, 3, 1, -2, 4]
#print the function which gives the maximum subarray sum.
print(f'Maximum subarray sum is: {subarray(l)}')
