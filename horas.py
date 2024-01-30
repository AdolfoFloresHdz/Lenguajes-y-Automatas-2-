# Viaje por carretera con búsqueda de coste uniforme
import functools
from BFS import Nodo

def compara(x, y):
    return x.get_coste() - y.get_coste()

def buscar_solucion_UCS(conexiones, estado_inicial, solucion):
    solucionado=False
    nodos_visitados=[]
    nodos_frontera=[]
    nodo_inicial = Nodo(estado_inicial)
    nodo_inicial.set_coste(0) #costo
    nodos_frontera.append(nodo_inicial)
    while (not solucionado) and len(nodos_frontera)!=0:
        # ordenar la lista de nodos frontera
        nodos_frontera = sorted(nodos_frontera, key= functools.cmp_to_key(compara))
        nodo=nodos_frontera[0]
        # extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))
        if nodo.get_datos() == solucion:
            # solución encontrada
            solucionado=True
            return nodo
        else:
            # expandir nodos hijo (ciudades con conexión)
            dato_nodo = nodo.get_datos()
            lista_hijos=[]
            for un_hijo in conexiones[dato_nodo]:
                hijo=Nodo(un_hijo)
                coste = conexiones[dato_nodo][un_hijo]
                hijo.set_coste(nodo.get_coste() + coste)
                
                lista_hijos.append(hijo)
                if not hijo.en_lista(nodos_visitados):
                    # si está en la lista lo sustituimos con
                    # el nuevo valor de coste si es menor
                    if hijo.en_lista(nodos_frontera):
                        for n in nodos_frontera:
                            if n.igual(hijo) and n.get_coste()>hijo.get_coste():
                                nodos_frontera.remove(n)
                                nodos_frontera.append(hijo)
                    else:
                        nodos_frontera.append(hijo)
                    nodo.set_hijos(lista_hijos)

if __name__ == "__main__":
    conexiones = {
        'CDMX': {'SLP':111,'MEXICALI':123,'CHIHUAHUA':515},
        'SAPOPAN': {'ZACATECAS':614,'MEXICALI':223},
        'GUADALAJARA':{'CHIAPAS':223},
        'CHIAPAS':{'CHIHUAHUA':534},
        'MEXICALI':{'SLP':561,'SAPOPAN':232,'CDMX':459,'CHIHUAHUA':675,'SONORA':982},
        'SLP':{'CDMX':674,'MEXICALI':843},
        'ZACATECAS':{'SAPOPAN':754,'SONORA':322,'CHIHUAHUA':631},  
        'SONORA':{'ZACATECAS':951,'MEXICALI':762},
        'MICHOACAN':{'CHIHUAHUA':652},
        'CHIHUAHUA':{'MICHOACAN':542,'ZACATECAS':544,'MEXICALI':435,'CDMX':951,'CHIAPAS':435}
    }
    estado_inicial='CDMX'
    solucion='SONORA'
    pies = '80ft'
    nodo_solucion = buscar_solucion_UCS(conexiones, estado_inicial, solucion)
    # mostrar resultado
    resultado=[]
    nodo=nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print("Ruta más Corta:")
    print(resultado)
    print("Distancia: " + str(nodo_solucion.get_coste()) +"km")
    peaje ={
        'CDMX': {'SLP':111,'MEXICALI':123,'CHIHUAHUA':515},
        'SAPOPAN': {'ZACATECAS':614,'MEXICALI':223},
        'GUADALAJARA':{'CHIAPAS':223},
        'CHIAPAS':{'CHIHUAHUA':534},
        'MEXICALI':{'SLP':561,'SAPOPAN':232,'CDMX':459,'CHIHUAHUA':675,'SONORA':982},
        'SLP':{'CDMX':674,'MEXICALI':843},
        'ZACATECAS':{'SAPOPAN':754,'SONORA':322,'CHIHUAHUA':631},  
        'SONORA':{'ZACATECAS':951,'MEXICALI':762},
        'MICHOACAN':{'CHIHUAHUA':652},
        'CHIHUAHUA':{'MICHOACAN':542,'ZACATECAS':544,'MEXICALI':435,'CDMX':951,'CHIAPAS':435}
    }
    suma = 0
    for i in range(len(resultado)-1):
        suma += peaje[resultado[i]][resultado[i+1]]
    
    if pies=='30ft':
        print("Costo: $" + str(suma))
    elif pies=='60ft':
        print("Costo: $" + str(suma*1.30))
    else:
        print("Costo: $" + str(suma*1.60))
    print("Volumen: " + pies)
    print()
    
    nodo_solucion = buscar_solucion_UCS(peaje, estado_inicial, solucion)
    # mostrar resultado
    resultado=[]
    nodo=nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
#    print("Ruta mas Barata:")
    suma = 0
    for i in range(len(resultado)-1):
        suma += conexiones[resultado[i]][resultado[i+1]]
#    print(resultado)
#    print("Distancia: " + str(suma) + "km")
#    if pies=='30ft':
#        print("Costo: $" + str(nodo_solucion.get_coste()))
#    elif pies=='60ft':
#        print("Costo: $" + str(nodo_solucion.get_coste()*1.30))
#    else:
#        print("Costo: $" + str(nodo_solucion.get_coste()*1.60))
#    print("Volumen: " + pies)