def strcounter(s):
    for sym in set(s) :
        count=0
        for sub_sym in s:
            if sym==sub_sym:
                count +=1
        print(f'{sym}-{count}')

strcounter('aaaaaaaaaaassssssssssssdgvknuhgeuhgwh')

















