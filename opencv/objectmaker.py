import threeDpoint
import numpy as np



data = threeDpoint.get3d()

arrdata = np.asarray(list(data))

np.savetxt("out.obj", arrdata, delimiter=' ', newline='\nv ')
	
	
