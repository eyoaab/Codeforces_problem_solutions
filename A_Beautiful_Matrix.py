for i in range(5):
    rows = list(map(int,input().split()))
    if 1 in rows:
        row=i+1
        column=rows.index(1)+1
print(abs(row-3)+abs(column-3))        