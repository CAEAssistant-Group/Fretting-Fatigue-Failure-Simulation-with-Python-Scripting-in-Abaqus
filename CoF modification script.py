
#      ######################################################################
#      #################      CAE Assistant Company          ################
#      ##############         www CAEassistant com              #############
#      ###########   Copy right by CAE Assistant Company    ###############
##      ######################################################################
#      ONLY the BUYER  of this package has permission to use its codes.
#	   Any distribution of this subroutine is illegal and will be prosecuted 
#      ######################################################################
#      ######################################################################
#      CAE Assisitant Services: 
#      Toturial Packages,Consultancy,Articles,Q&A,Video Gallery,Online Course
#      ######################################################################
#      Need help with your project? 
#      You can get initial free consultation from (Support CAEassistant com)
#      ######################################################################

from abaqusConstants import SCALAR, CENTROID
from numpy import sin, cos, sqrt

COF = [0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65]

Sf = 835 # MPa

damage = []
angle = []

for cof in COF:
    

    #Hidden Content Please purchase the full product to access the complete code. 
    mdb.jobs['Fretting'].submit()
    mdb.jobs['Fretting'].waitForCompletion()
    
    odb = session.openOdb("Fretting.odb")

    results = odb.rootAssembly.instances['PLANE-1'].elementSets['RESULTS']
    
    #Hidden Content Please purchase the full product to access the complete code. 
    
    for i, j, k in zip(Emax_sub.values, Emin_sub.values, Smax_sub.values):
        
        Ex_max = i.data[0]
        Ey_max = i.data[1]

        #Hidden Content Please purchase the full product to access the complete code. 
        
        for o in range(-90, 91):
            
            #Hidden Content Please purchase the full product to access the complete code. 
            Ymin = (-(Ex_min - Ey_min)*sin(2*radians(o))/2 + Exy_min*cos(2*radians(o))/2)*2
            
            #Hidden Content Please purchase the full product to access the complete code. 
            
            if FS > FS_local:
                
                FS_local = FS
                #Hidden Content Please purchase the full product to access the complete code. 

