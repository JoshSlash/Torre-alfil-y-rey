def torre(f1,c1,f2,c2):
	if (f1==f2) and (c1==c2): return 0
	if (f1==f2) or (c1==c2): return 1
	else: return 2

def alfil(f1,c1,f2,c2):
	f,c,k=f1,c1,0
	if (f1==f2) or (c1==c2): return 0,k
	if (f2>f1) and (c2>c1):
		while(f<9 or c<9):
			if f==f2 and c==c2: return 1,k
			f=f+1
			c=c+1
			k=k+1
		return 0,k
	if (f2>f1) and (c2<c1):
		while(f<9 or c>0):
			if f==f2 and c==c2: return 1,k
			f=f+1
			c=c-1
			k=k+1
		return 0,k
	if (f2<f1) and (c2<c1):
		while(f>0 or c>0):
			if f==f2 and c==c2: return 1,k
			f=f-1
			c=c-1
			k=k+1
		return 0
	if (f2<f1) and (c2>c1):
		while(f>0 or c<9):
			if f==f2 and c==c2: return 1,k
			f=f-1
			c=c+1
			k=k+1
		return 0,k

def rey(f1,c1,f2,c2):
	if torre(f1,c1,f2,c2)==1:
		if f1==f2: return abs(c2-c1)
		if c1==c2: return abs(f2-f1)
	else:
		a,k=alfil(f1,c1,f2,c2)
		return k

def chess(f1,c1,f2,c2):
	a,k=alfil(f1,c1,f2,c2)
	print(torre(f1,c1,f2,c2), a, rey(f1,c1,f2,c2))

chess(8,8,8,8)