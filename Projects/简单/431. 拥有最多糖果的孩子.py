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

