'''
python classe and objects 

A class  is a blueprint or templete for creating objects providing nitial values for state 
(member variable or attributes ) a nd implementstion  of behavior (member funtions or methodes )
the user-defined obejcts are creating using the class keyword. 

'''


class parson: 
    name       =     "vishal"
    Lastname   =     "rajput"
    Age        =        18
    address    =    "bharatput"
    PhoneNo    =     969419321
    occupation   =     "web developer"
    def info(self):
        print(f"{self.name} is a  {self.occupation}" )
             


delets = parson()
delets.info()
# delets.name = "yoegsh"
# delets.occupation = "shop wala "

# print(delets.name)
# print(delets.occupation)

