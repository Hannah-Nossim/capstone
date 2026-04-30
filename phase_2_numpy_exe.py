import numpy as np

# exam scores for 8 students
scores = np.array([88, 72, 95, 61, 79, 91, 55, 83])

# your tasks:
# 1. find the class average
# 2. find all scores above the average
# 3. how many students passed (score >= 70)?
# 4. replace every failing score with 0 using np.where
# 5. what is the highest score in the top half of the class?

# 1. find the class average
average = np.mean(scores) 

# 2. find all scores above the average
above_avg = scores[scores > average]

# 3. how many students passed (score >= 70)?
passed_count = np.sum(scores >= 70)

# 4. replace every failing score with 0 using np.where
modified_scores = np.where(scores < 70, 0, scores)

# 5. what is the highest score in the top half of the class?
sorted_scores = np.sort(scores)
top_half = sorted_scores[len(scores)//2:]
highest_top_half = np.max(top_half)

average, above_avg, passed_count, modified_scores, highest_top_half