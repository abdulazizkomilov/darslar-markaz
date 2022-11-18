import avto_dars_mod # avto_info_mod faylini (modulini) chaqiramiz

avto1 = avto_dars_mod.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
avto_dars_mod.info_print(avto1)



import avto_dars_mod as adm # avto_info_mod ni qisqa nom aim bilan chaqiramiz

avto1 = adm.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
adm.info_print(avto1)




import avto_dars_mod as adm # avto_info_mod ni qisqa nom aim bilan chaqiramiz

avto1 = adm.avto_kirit()

for avto in avto1:
    adm.info_print(avto)


# from avto_info_mod import avto_info, info_print

# avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# info_print(avto1)


# from avto_info_mod import avto_info as ainfo, info_print as iprint

# avto1 = ainfo("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# iprint(avto1)



# from avto_info_mod import *

# avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# info_print(avto1)
