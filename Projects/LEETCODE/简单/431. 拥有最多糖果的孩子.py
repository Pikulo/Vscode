# Given a list of candies, check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.
# 
# Args:
#   candies: an array of integers representing the number of candies that each child has.
#   extraCandies: the number of candies that the person brings to the class
# Returns:
#   A list of boolean values.
candies = [12,12]

extraCandies = 1
max_candy=max(candies)
list_out=[]*len(candies)
for i in candies:
    if i+extraCandies>=max_candy:
        list_out.append(True)
    else:
        list_out.append(False)
print(list_out)

