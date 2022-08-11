# 给你一个字符串数组 words ，数组中的每个字符串都可以看作是一个单词。请你按 任意 顺序返回 words 中是其他单词的子字符串的所有单词。
# 如果你可以删除 words[j] 最左侧和/或最右侧的若干字符得到 word[i] ，那么字符串 words[i] 就是 words[j] 的一个子字符串。
# words = ["a", "mass", "as", "hero", "superhero"]
# words = ["leetcode", "et", "code"]
# words = ["blue", "green", "bu"]
# 报错，我的输出为["am","leetcode"]，正确应该是["leetcode","od","am"]
# ['od', 'am', 'hamlet', 'leetcode', 'leetcoder']
words = ["leetcoder", "leetcode", "od", "hamlet", "am"]
# ['as', 'hero', 'mass', 'superhero']
# 之前错误是应为words[i]<words[index],表示比较他们字典数大小，应该比较其长度大小。
words = sorted(words, key=lambda x: len(x))
# sorted(words)
# words.sort()
print(words)
res = []
for i in range(len(words)-1):
    index = i+1
    while index < len(words):
        print(words[i], words[index])
        # 之前错误是应为words[i]<words[index],表示比较他们字典数大小，应该比较其长度大小。
        if len(words[i]) < len(words[index]) and words[i] in words[index]:  # 用if t in d:判断字符串包含情况
            res.append(words[i])
            break  # 题目要求找到子字符串就行，所以找到一个就退出循环，避免重复添加
        index += 1
print(res)
# return res
