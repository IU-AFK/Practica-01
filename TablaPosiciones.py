teams = {}
#teams tiene key equipos y valor integer (puntos)

print("""
1. Agregar equipo
2. Eliminar equipo
3. Registrar partido
4. Mostrar tabla
5. Cerrar programa
      
""")

while True:
    menu = (input(" "))
    if menu.isdigit():
        menu = int(menu)
        break
    else:
        print("Solo se aceptan numeros. Intente otra vez")

while True:
    match menu:

        case 1:
            #agregar equipo
            team_name = input("Nombre del equipo: ").lower()
            if team_name not in teams:
                teams [team_name] = 0
            else:
                print("Ese equipo ya fue registrado")
        case 2:
            #eliminar equipo
            team_name = input("Nombre del equipo: ").lower()
            if team_name not in teams:
                print("No se encontro el equipo")
            else:
                del (teams[team_name])
        case 3:
            #registrar partido
            local = input("Ingresar equipo local o Salir: ").lower()
            while local not in teams and local != "salir":
                local = input("Error. Ingresar equipo local o Salir: ").lower()
            if local != "salir":
                visitante = input("Ingresar equipo visitante: ").lower()
                while True:
                    if visitante == "salir":
                        break
                    if visitante not in teams or visitante == local:
                        visitante = input("Error. Ingresar equipo visitante o Salir: ").lower()
                    else:
                        break
            if local != "salir" and visitante != "salir":
                while True:
                    puntos = input("Ingresar resultado del partido en formato 4-2: ")
                    if "-" in puntos:
                        puntos = puntos.split("-")
                        if len(puntos)==2 and all(p.isdigit() for p in puntos):
                          break
                    print("Formato incorrecto. El formato no contempla espacios ")
                res1 = int(puntos[0])
                res2 = int(puntos[1])
                if res1>res2:
                    teams[local] += 3
                elif res2>res1:
                    teams[visitante] += 3
                else:
                    teams[local] += 1
                    teams[visitante] += 1
        case 4:
            #mostrar tabla
            teams = dict(sorted(teams.items(), key=lambda x: x[1], reverse=True))
            for equipo in teams:
               print(f"{equipo}: {teams[equipo]} ")
        case 5:
            #cerrar programa
            break
        case _:
            #volver a ingresar/ingreso no valido
            menu = int(input("El numero ingresado no es valido "))

    print("""
    1. Agregar equipo
    2. Eliminar equipo
    3. Registrar partido
    4. Mostrar tabla
    5. Cerrar programa
        
    """)

    while True:
        menu = (input(" "))
        if menu.isdigit():
            menu = int(menu)
            break
        else:
            print("Solo se aceptan numeros. Intente otra vez")