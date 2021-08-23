# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 20:28:27 2021

@author: adeel
"""

# Travelling Salesperson Problem - Airports
# 0 = PTY (Panama)
# 1 = BOG (Bogota)
# 2 = JFK (NYC)
# 3 = MIA (Miami)
# 4 = KIAH (Houston)
# 5 = ORD (Chicago)

from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp


def create_data_model():
    # Great circle distances obtenidas de http://www.gcmap.com/
    data = {}
    data['distance_matrix'] = [
        [0, 755, 3541, 1854, 2850, 3740],
        [755, 0, 3980, 2425, 3578, 4380],
        [3541, 3980, 0, 1753, 2280, 1191],
        [1854, 2425, 1753, 0, 1551, 1926],
        [2850, 3578, 2280, 1551, 0, 1489],
        [3740, 4380, 1191, 1926, 1489, 0],
    ]  # yapf: disable
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data

def print_solution(manager, routing, solution):
    # Funcion para imprimir la solucion en la consola
    print('Objetivo: {} kilometros'.format(solution.ObjectiveValue()))
    index = routing.Start(0)
    plan_output = 'Ruta para el vehiculo partiendo y regresando a 0:\n'
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output += ' {} ->'.format(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output += ' {}\n'.format(manager.IndexToNode(index))
    plan_output = plan_output.replace('0', 'PTY').replace('1', 'BOG').replace('2', 'JFK').replace('3', 'MIA').replace('4', 'KIAH').replace('5', 'ORD')
    print(plan_output)
    plan_output += 'Distancia de ruta: {}kilometros\n'.format(route_distance)
    
def get_routes(solution, routing, manager):
  # Funcion para guardar la solucion en un arreglo.
  routes = []
  for route_nbr in range(routing.vehicles()):
    index = routing.Start(route_nbr)
    route = [manager.IndexToNode(index)]
    while not routing.IsEnd(index):
      index = solution.Value(routing.NextVar(index))
      route.append(manager.IndexToNode(index))
    routes.append(route)
  return routes

def main():
    # Inicio del Programa
    # Crear modelo de datos.
    data = create_data_model()
    
    # Basado en la fila, cantidad de vehiculos y el nodo inicial, crea el manejador.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])

    # Crear modelo de rutas.
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        # Funcion para retornar distancia entre dos nodos
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Costo de viajar entre dos nodos, parecido a distance_callback pero puede variar.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Definir estrategia de solucion. "Cheapest Arc", agrega el menor costo por orden.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Llamar funcion para resolver.
    solution = routing.SolveWithParameters(search_parameters)

    # Llamar funcion para imprimir.
    if solution:
        print_solution(manager, routing, solution)

    # Funcion para almacenar en un arreglo la solucion.
    routes = get_routes(solution, routing, manager)
    print(routes)


if __name__ == '__main__':
    main()