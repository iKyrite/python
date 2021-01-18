pollaplasia= []
nonpollaplasia = []
for i in range(100,1000):
    #i += 1
    
    if i % 9 == 0:
        pollaplasia.append(i)
        
    elif i % 9 != 0:
        nonpollaplasia.append(i)
        
print ("pollaplasia: ", "("+str(len(pollaplasia))+")", pollaplasia),
print ("mh pollaplasia ", "("+str(len(nonpollaplasia))+")",nonpollaplasia),
