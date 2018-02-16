# def merge_sort(li):
#     if len(li) < 2: return li
#     m = len(li) / 2
#     return merge(merge_sort(li[:m]), merge_sort(li[m:]))

# def merge(l, r):
#     result = []
#     i = j = 0
#     while i < len(l) and j < len(r):
#         if l[i] < r[j]:
#             result.append(l[i])
#             i += 1
#         else:
#             result.append(r[j])
#             j += 1            
#     result += l[i:]
#     result += r[j:]
#     return result

nList = []
kList = []
result = []
finalResult = []
index = []
n, k, FinishCoordination = map(int, raw_input().split())
nList = map(int, raw_input().split())
kList = map(int, raw_input().split())
# kList = merge_sort(kList)
# nList = merge_sort(nList)
kList = sorted(kList)
nList = sorted(nList)
j = 0
for i in xrange(0, n):
	result = []
	x = 0
	while (j+x) < k:
		while x != (n) and (j+x) < k:
			
			if (nList[i] < kList[j+x] and kList[j+x] < FinishCoordination) or (kList[j+x] > FinishCoordination and nList[i] > kList[j+x]): 	# ja'be beyne n , k
				result.append((abs(nList[i] - FinishCoordination)))
			elif (kList[j+x] > FinishCoordination and kList > nList[i]):
				result.append(abs(nList[i] - kList[j+x]) + abs(FinishCoordination - kList[j+x]))
			elif kList[j+x] < FinishCoordination and kList[j+x] < nList[i]:
				result.append(abs(nList[i] - kList[j+x]) + abs(FinishCoordination - kList[j+x]))
			x += 1
		j += 1
	finalResult.append(min(result))
	# kList.remove(min(result))
print max(finalResult)







