def saludos():
    personas = [
        ("Diego", "formador"),
        ("Ana", "lider"),
        ("Luis", "trabajador"),
        ("Sofia", "trabajador"),
        ("Carlos", "visitante")
    ]

    for nombre, rol in personas:
        if rol == "formador":
            print(f"Saludos cordiales {nombre}, es todo un {rol}")
        elif rol == "lider":
            print(f"Bienvenido sea {nombre}, es todo un {rol}")
        elif rol == "trabajador":
            print(f"Buenos días {nombre}, es todo un {rol}")
        elif rol == "visitante":
            print(f"Buenos días, ¿qué se le ofrece {nombre}? Es todo un {rol}")
        else:
            print(f"Hola {nombre}, rol no identificado.")

saludos()