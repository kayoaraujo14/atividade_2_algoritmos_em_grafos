class Aresta:
    def __init__(self, u, v, peso):
        self.u = u
        self.v = v
        self.peso = peso

    def __lt__(self, outra):
        return self.peso < outra.peso

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.arestas = []

    def adicionar_aresta(self, u, v, peso):
        self.arestas.append(Aresta(u, v, peso))

    def encontrar_pai(self, parent, i):
        if parent[i] == i:
            return i
        return self.encontrar_pai(parent, parent[i])

    def unir_subconjuntos(self, parent, rank, x, y):
        raiz_x = self.encontrar_pai(parent, x)
        raiz_y = self.encontrar_pai(parent, y)

        if rank[raiz_x] < rank[raiz_y]:
            parent[raiz_x] = raiz_y
        elif rank[raiz_x] > rank[raiz_y]:
            parent[raiz_y] = raiz_x
        else:
            parent[raiz_y] = raiz_x
            rank[raiz_x] += 1

    def kruskal(self):
        # Ordena as arestas pelo peso
        self.arestas.sort()
        parent = []
        rank = []
        arvore_geradora_minima = []
        peso_total = 0

        # Inicializa os conjuntos disjuntos para cada vértice
        for vertice in range(self.vertices):
            parent.append(vertice)
            rank.append(0)

        # Itera sobre as arestas
        for aresta in self.arestas:
            u, v, peso = aresta.u, aresta.v, aresta.peso
            raiz_u = self.encontrar_pai(parent, u)
            raiz_v = self.encontrar_pai(parent, v)

            # Verifica se adicionar essa aresta não formará um ciclo
            if raiz_u != raiz_v:
                arvore_geradora_minima.append(aresta)
                peso_total += peso
                self.unir_subconjuntos(parent, rank, raiz_u, raiz_v)

        return arvore_geradora_minima, peso_total

    def exibir_arvore_geradora(self, arvore, peso_total):
        print("\nArestas da Árvore Geradora Mínima:")
        for aresta in arvore:
            print(f"{aresta.u} - {aresta.v} com peso {aresta.peso}")
        print(f"\nPeso total da Árvore Geradora Mínima: {peso_total}")

# Função principal para execução
def main():
    vertices = int(input("Digite o número de vértices: "))
    arestas_count = int(input("Digite o número de arestas: "))
    grafo = Grafo(vertices)

    for _ in range(arestas_count):
        u, v, peso = map(int, input("Digite a aresta (vertice1 vertice2 peso): ").split())
        grafo.adicionar_aresta(u, v, peso)

    arvore_geradora_minima, peso_total = grafo.kruskal()
    grafo.exibir_arvore_geradora(arvore_geradora_minima, peso_total)

if __name__ == "__main__":
    main()
