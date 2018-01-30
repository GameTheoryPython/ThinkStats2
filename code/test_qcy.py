def PercentileRank(scores, your_score):
    count = 0
    for score in scores:
        if score <= your_score:
            count += 1
    
    percentile_rank = 100.0 * count / len(scores)
    return percentile_rank
    
def Percentile(scores, percentile_rank):
    scores.sort()
    print(scores)
    for score in scores:
        if PercentileRank(scores, score) >= percentile_rank:
            return score
        
def Percentile2(scores, percentile_rank):
    scores.sort()
    index = percentile_rank * (len(scores)-1) / 100
    print(scores)
    print(index)
    return scores[int(index)]

test_scores = [56, 66, 77, 88, 99]
print(Percentile(test_scores, 80))
print(Percentile2(test_scores, 80))