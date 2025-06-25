#      This is just a demo to show how the code is structured. For the full, working version, please visit our website.
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
odb = session.openOdb("Fretting.odb", readOnly = False)

contact = odb.rootAssembly.instances['PLANE-1'].elementSets['CONTACT']

#Hidden Content Please purchase the full product to access the complete code. 

Stress_r = Stress.getSubset(region = contact)
#Hidden Content Please purchase the full product to access the complete code. 

S11 = []
S12 = []
S22 = []

for i, j, k in zip(Stress_r.values, Pressure_r.values, Coord_contact.values):
    
    Sx = i.data[0]
    #Hidden Content Please purchase the full product to access the complete code. 


with open("S11.txt", "w") as file:
    for i in S11:
        file.write()#Hidden Content Please purchase the full product to access the complete code. )

