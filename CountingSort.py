def countingSort(arr): 
        maxrange = max(arr)
        counting = [0 for x in range(maxrange+1)]

        for elem in arr:
                counting[elem] += 1
        
        result = []
        for i in range(len(counting)):
                if counting[i] > 0:
                        result.extend(counting[i]*[i])
        
        return result

arr = [1,1,3,2,1]
countingSort(arr)