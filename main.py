from cita import seleccionar_opcion, generar_cita, buscar_por_codigo, citas
continuar = True
while continuar:
    opcion = seleccionar_opcion()
    if opcion == 1:
        buscar_por_codigo(citas)

    elif opcion == 2:
        nuevas_citas = generar_cita()
        citas.extend(nuevas_citas)
    continuar = input("\n¿Desea realizar otra actividad en el sistema? (si/no): ").lower()=="si"
print("\n============== FIN DEL SISTEMA ================")
