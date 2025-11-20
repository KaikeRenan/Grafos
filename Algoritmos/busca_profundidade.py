import lista_adjacencia

def dfs(grafo, vi):
    if vi not in grafo:
        return []

    pilha = [vi]
    visitados = []

    while pilha:
        vertice = pilha.pop()

        if vertice not in visitados:
            visitados.append(vertice)

            vizinhos = grafo.get(vertice, [])

            for v in vizinhos:
                if v not in pilha and v not in visitados:
                    pilha.append(v)

    return visitados


def dfs_encontrar_ciclos(grafo, vi):
    if vi not in grafo:
        return False

    pilha = [{
        "vertice": vi,
        "pai": None
    }]

    visitados = []

    while pilha:
        item = pilha.pop()

        atual = item["vertice"]
        pai = item["pai"]

        if atual not in visitados:
            visitados.append(atual)

            vizinhos = grafo.get(atual, [])

            for v in vizinhos:
                if v not in visitados and all(v != p["vertice"] for p in pilha):
                    pilha.append({
                        "vertice": v,
                        "pai": atual
                    })
                else:
                    if v != pai:
                        return True

    return False


def main():
    grafo = lista_adjacencia.criar_grafo()
    nao_direcionado = input("É não direcionado? (s/n): ").strip().lower() == "s"

    while True:
        print(
            """
1 - Mostrar o Grafo
2 - Inserir vértice
3 - Inserir aresta
4 - Remover vértice
5 - Remover aresta
6 - Listar vizinhos
7 - Verificar aresta
8 - Calcular grau dos vértices
9 - Verificar percurso válido
10 - Busca em Profundidade (DFS)
11 - Buscar Ciclos com DFS
0 - Sair
"""
        )
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            lista_adjacencia.exibir_grafo(grafo)

        elif opcao == "2":
            v = input("Nome do vértice: ").strip()
            lista_adjacencia.adicionar_vertice(grafo, v)

        elif opcao == "3":
            vi = input("Vértice Inicial: ").strip()
            vf = input("Vértice Final: ").strip()
            lista_adjacencia.adicionar_aresta(grafo, vi, vf, nao_direcionado)

        elif opcao == "4":
            v = input("Vértice a remover: ").strip()
            lista_adjacencia.remover_vertice(grafo, v)

        elif opcao == "5":
            vi = input("Inicial: ").strip()
            vf = input("Final: ").strip()
            lista_adjacencia.remover_aresta(grafo, vi, vf, nao_direcionado)

        elif opcao == "6":
            v = input("Vértice: ").strip()
            lista_adjacencia.listar_vizinhos(grafo, v)

        elif opcao == "7":
            vi = input("Inicial: ").strip()
            vf = input("Final: ").strip()
            print("Existe aresta?", lista_adjacencia.existe_aresta(grafo, vi, vf))

        elif opcao == "8":
            graus = lista_adjacencia.grau_vertices(grafo)
            for v, g in graus.items():
                print(f"{v}: in={g['in']}, out={g['out']}, total={g['total']}")

        elif opcao == "9":
            caminho = input("Digite os vértices separados por espaço: ").split()
            print("Percurso válido?", lista_adjacencia.percurso_valido(grafo, caminho))

        elif opcao == "10":
            vi = input("Início da DFS: ").strip()
            print("DFS:", dfs(grafo, vi))

        elif opcao == "11":
            vi = input("Início para detectar ciclos: ").strip()
            ciclo = dfs_encontrar_ciclos(grafo, vi)
            print("Ciclo detectado?" , ciclo)

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
