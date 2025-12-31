from collections import Counter
def recovery(log,pattern):
    result=''
    pattern_count=Counter(pattern)

    window_count=Counter()
    left=0



    for right in range(len(log)):

        window_count[log[right]]+=1

        is_valid=True
        for c in pattern_count:
            if window_count[c]<pattern_count[c]:
                is_valid=False
                break
        if is_valid:
            window=log[left:right+1]
            if result=="" or len(window)<len(result):
                result=window
            while left<right and window_count[log[left]]>pattern_count[log[left]]:
                window_count[log[left]] -= 1
                left += 1

    return result





print(recovery("ADOBECODEBANC","ABC"))

