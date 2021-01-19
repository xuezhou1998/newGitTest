class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
    	ctr_sqr=[(x1+x2)/2,(y1+y2)/2]
    	sqr_nw=[x1,y2]
    	sqr_ne=[x2,y2]
    	sqr_sw=[x1,y1]
    	sqr_se=[x2,y1]
    	result=False
    	if [x_center,y_center] in [sqr_nw,sqr_sw,sqr_se,sqr_ne]:
    		print(1)
    		return True
    	if x_center<=x1 and y_center>=y2:
    		print(2)
    		distance=(x_center-x1)**2+ (y_center-y2)**2
    		if distance<=radius**2:
    			result=True
    			return result
    	elif x_center>=x2 and y_center>=y2:
    		print(3)
    		distance=(x_center-x2)**2+ (y_center-y2)**2
    		if distance<=radius**2:
    			result=True
    			return result
    	elif x_center>=x2 and y_center<=y1:
    		print(4)
    		distance=(x_center-x2)**2+ (y_center-y1)**2
    		if distance<=radius**2:
    			result=True
    			return result
    	elif x_center<=x1 and y_center<=y1:
    		print(5)
    		distance=(x_center-x1)**2+ (y_center-y1)**2
    		if distance<=radius**2:
    			result=True
    			return result
    	elif x1<=x_center<=x2:
    		print(6)
    		if y1-radius<=y_center<=y2+radius:
    			return True
    	elif y1<=y_center<=y2:
    		print(7)
    		if x1-radius<=x_center<=x2+radius:
    			return True
    	
    	else:
    		print(8)
    		return result
# 5
# 8
# 8
# 9
# 5
# 12
# 8

# Output
    	# if ctr_sqr[0]==x_center and ctr_sqr[1]==y_center:
    	# 	return True
    	# elif ctr_sqr[0]>=x_center and ctr_sqr[1]>=y_center:
    	# 	#circle in the south west
    	# 	#do circle's north east

    	# elif ctr_sqr[0]<x_center and ctr_sqr[1]<y_center:
    	# elif ctr_sqr[0]>=x_center and ctr_sqr[1]<y_center:
    	# elif ctr_sqr[0]<x_center and ctr_sqr[1]>=y_center:

