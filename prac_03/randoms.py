"""
Trial 1
"""
# 9
# 7
# 3.84231042331867

"""
Trial 2
"""
# 12
# 3
# 4.372112652489189

"""
Trial 3
"""
# 15
# 9
# 3.168614456511046

"""
Trial 4
"""
# 7
# 9
# 4.719829913547093

"""
Trial 5
"""
# 19
# 5
# 5.099198218691881

# What did you see on line 1?
# The smallest number that could have been produced is 5, and the largest was 20

# What did you see on line 2?
# the smallest number that could have been produced was 3, and the largest 9. Line 2 cannot
# have produced a 4, because the string is asking to pick a number between 3 and 10, in intervals of 2
# this means only a 3, 5, 7, or 9 could have been produced

# What did you see on Line 3?
# smallest number was 2.5, largest was less than 5.5

# Write code that prints between 1 and 100 inclusive

import random
print(random.randint(1, 100))

