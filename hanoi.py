def moveTower(n, tFrom, tTo, tmp):
    if n > 0:
        moveTower(n-1, tFrom, tmp, tTo) #move to tmp
        print("Moving disk from",tFrom,"to",tTo)
        moveTower(n-1, tmp, tTo, tFrom) #move from tmp




def hanoiBinary(n):
   for x in range(1,1<<n):
       print( "move from",(x&x-1)%3,"to",((x|x-1)+1)%3 )

#hanoiBinary(3)
moveTower(2,6,3, 4)