
#      ######################################################################
#      #################      CAE Assistant Company          ################
#      ##############         www CAEassistant com              #############
#      ###########   Copy right by CAE Assistant Company    ###############
#      ######################################################################
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

odb = session.openOdb("Fretting.odb", readOnly = False)

#Hidden Content Please purchase the full product to access the complete code. 
plane = odb.rootAssembly.instances['PLANE-1']

Emax = odb.steps['Max'].frames[-1].fieldOutputs['E']
Emin = odb.steps['Min'].frames[-1].fieldOutputs['E']
#Hidden Content Please purchase the full product to access the complete code. 

Emax_sub = Emax.getSubset(region = results)
Emin_sub = Emin.getSubset(region = results)
#Hidden Content Please purchase the full product to access the complete code. 

Sf = 835 # MPa

Data = []

for i, j, k, l in zip(Emax_sub.values, Emin_sub.values, Smax_sub.values, Coord_sub.values):
    
    Ex_max = i.data[0]
    #Hidden Content Please purchase the full product to access the complete code. 
    
    for o in range(-90, 91):
        
        Sp = (Sx_max + Sy_max)/2 + (Sx_max - Sy_max)*cos(2*radians(o))/2 + Sxy_max*sin(2*radians(o))
        #Hidden Content Please purchase the full product to access the complete code. 
    
    if any(cont.data[0] == coor[0] and cont.data[1] == coor[1] for cont in Coord_contact.values):
        Data.append([coor[0], FS_local])

with open("Data.txt", "w") as file:
    #Hidden Content Please purchase the full product to access the complete code. 

