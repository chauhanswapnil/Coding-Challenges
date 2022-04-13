from unittest import skip


# def danceScore(scores, wait, k, skipTotal, chooseTotal):
#     if (k == len(scores) - 1):
#         print("Scores last", scores[k])
#         return scores[k] # Selecting
    
#     if (k+wait[k]+1 > len(scores) - 1):
#         print("Can't go further", scores[k])
#         return scores[k] # Selecting

#     skipTotal = skipTotal + danceScore(scores, wait, k+1, skipTotal, chooseTotal)
    
#     chooseTotal = chooseTotal + danceScore(scores,wait, k+wait[k]+1, skipTotal, chooseTotal)
    
#     print(skipTotal, chooseTotal)
#     return max(skipTotal, chooseTotal)

def danceScore(scores, wait, k):
    if k > len(scores) - 1:
        return 0
    
    dtotal = 0
    stotal = 0
    dtotal = max(dtotal, scores[k] + danceScore(scores, wait, k+1))

    stotal = max(stotal, scores[k] + danceScore(scores, wait, k+wait[k]+1))
    
    # chooseTotal = chooseTotal + danceScore(scores,wait, k+wait[k]+1, skipTotal, chooseTotal)
    
    # print(skipTotal, chooseTotal)
    return min(dtotal,stotal)


print(danceScore([7,1,5,3,30],[3,0,1,2,3],0))
# 7    
    