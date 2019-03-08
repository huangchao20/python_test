import os
import sys
import time
for i in range( 1000 ):
    t = i / 1000
#    sys.stdout.write( "%s %%"  %t )
    print( "%s %%" %t )
    time.sleep( 0.1 )
    sys.stdout.flush()