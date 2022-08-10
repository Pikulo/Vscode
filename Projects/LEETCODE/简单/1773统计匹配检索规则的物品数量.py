items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"
sum=0
dict_rekey={"type":0, "color":1,"name":2}
print(dict_rekey.get('color'))
print(list(dict_rekey.items()))
print(dict_rekey.keys())
print(dict_rekey.values())
for i in items:
    print(i[dict_rekey.get(ruleKey)])
    if i[dict_rekey.get(ruleKey)]==ruleValue:
        sum+=1
print(sum)