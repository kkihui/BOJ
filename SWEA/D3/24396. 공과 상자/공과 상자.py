T = int(input())
  
for _ in range(T):
    b,w,x,y,z = map(int,input().split())
    ans = -(10**10)
 
    # 더 적은 상자에서 하나씩 옮겨서 채워넣는 경우 계산
    if b < w:
        for bbox_b in range(b+1):
            dif_color = b - bbox_b
            wbox_w = w - dif_color
            cost = bbox_b*x + wbox_w*y + dif_color*z*2
            ans = max(ans,cost)
    else:
        for wbox_w in range(w+1):
            dif_color = w - wbox_w
            bbox_b = b - dif_color
            cost = bbox_b*x + wbox_w*y + dif_color*z*2
            ans = max(ans,cost)
     
    print(ans)