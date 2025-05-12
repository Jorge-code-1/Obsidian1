ingreso_mensual= 84000
gasto_mensual = 80000

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif ingreso_mensual -gasto_mensual > 3000:
        print("estas bien")
    else:
        print("estas gastando demasiado ")

elif ingreso_mensual > 1000:
    print("esta bien en latinoamerica")

elif ingreso_mensual > 500:
    print("estas bien en argentina ")

elif ingreso_mensual > 200 :
    print("estas bien en venezuela")

else:
    print("sos pobre")