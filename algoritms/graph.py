class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph Routes Dict:", self.graph_dict)

    
    def get_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []
        paths= []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            print("path", path)
            print("graph",self.graph_dict[start])
            print("node",node)
            
            if node not in path:
                print("llego")
                sp = self.get_shortest_path(node, end, path)
                print("sp",sp)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path

    '''
    path ['Mumbai'] //llega al start
    graph ['Paris', 'Dubai'] //obtiene los valores conectado del start
    node Paris // empieza con el primer valor del star
    llego
    path ['Mumbai', 'Paris'] // almacena la primer ruta
    graph ['Dubai', 'New York'] // obtiene las posibilidades del primer valor conectado al start
    node Dubai // empieza con la primer ruta del primer valor conectado al start
    llego
    path ['Mumbai', 'Paris', 'Dubai'] // almacena la primer ruta
    graph ['New York'] // encuentra el destino ya que no hay otra posibilidad
    node New York // da el valor de destino
    llego
    sp ['Mumbai', 'Paris', 'Dubai', 'New York'] // guarda la ruta y la establece
    sp ['Mumbai', 'Paris', 'Dubai', 'New York']
    path ['Mumbai', 'Paris'] // regresa al primer valor conectado al start
    graph ['Dubai', 'New York'] // revisa la segunda posibilidad
    node New York // da el valor del siguiente paso
    llego
    sp ['Mumbai', 'Paris', 'New York'] // guarda la ruta y la establece como la mas corta
    sp ['Mumbai', 'Paris', 'New York']
    path ['Mumbai'] // como termino con la posibilidades con el primer valor conectado regresa y termina con el segundo valor conectado al start
    graph ['Paris', 'Dubai'] // revisa el segundo valor posible de rutas
    node Dubai // lo establece
    llego
    path ['Mumbai', 'Dubai'] // guarda la ruta
    graph ['New York'] // revisa los datos de las posibilidades de ruta
    node New York // establece el destino al encontrarlo
    llego
    sp ['Mumbai', 'Dubai', 'New York'] // guarda la ruta que encontro
    sp ['Mumbai', 'Dubai', 'New York']
    Shortest path between Mumbai and New York:  ['Mumbai', 'Paris', 'New York'] termina como ganadora a esta ruta debido a que fue la primera en ser mas corta y no encontro otra mejor
    '''

if __name__ == '__main__':

    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    route_graph = Graph(routes)
    start= "Mumbai"
    end = "Toronto"
    print(f"Paths Between {start} and {end}:", route_graph.get_paths(start, end))

    start = "Mumbai"
    end = "New York"
    print("///////////////")
    print(f"All paths between: {start} and {end}: ",route_graph.get_paths(start,end))
    print("///////////////")
    print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start,end))
    print("///////////////")
    start = "Dubai"
    end = "New York"

    print(f"All paths between: {start} and {end}: ",route_graph.get_paths(start,end))
    print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start,end))

    #creation
    d = {
        "Mumbai": ["Paris","Dubai"],
        "Paris": ["Dubai","New York"],
        "Dubai": ["Paris","Dubai"]
    }