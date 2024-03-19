import random
random.seed(42)

#score_list = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def score_counter(score_list):
    negative_score = 0
    neutral_score = 0
    positive_score =0
    
    for scores in score_list:
        if scores >= 9:
            positive_score += 1
        elif scores in range(6, 8):
            neutral_score += 1
        else:
            negative_score += 1
    
    print("Negative: ", negative_score)
    print("Neutral: ", neutral_score)
    print("Positive: ", positive_score)
    
#score_counter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

possible_scores = list(range(1,11))
score_list1 = random.choices(possible_scores, weights=[8,8,8,8,8,3,3,4,20,30], k=10)
score_list2 = random.choices(possible_scores, weights=[1,2,3,4,5,10,15,15,7,9], k=450)
score_list3 = random.choices(possible_scores, weights=[1,2,3,4,4,5,5,10,15,25], k=10000)

print('Test 1:')            
score_counter(score_list1)  
