import lista_adjacencia

def bfs(grafo, vi):
    if vi not in grafo:
        print("Vértice inicial não existe no grafo")
        return []

    visitados = []
    fila = [vi]

    while len(fila) > 0:
        atual = fila.pop(0)

        if atual not in visitados:
            visitados.append(atual)

            for visitado in grafo[atual]:
                if visitado not in visitados and visitado not in fila:
                    fila.append(visitado)

    return visitados

def menor_caminho_bfs(grafo, vi, vf):
    if vi not in grafo or vf not in grafo:
        print("Algum dos vértices não existe no grafo")
        return None

    fila = [{
        "vertice": vi,
        "caminho": [vi]
    }]

    visitados = []

    while len(fila) > 0:
        item = fila.pop(0)
        atual = item["vertice"]
        caminho = item["caminho"]

        if atual == vf:
            return caminho

        if atual not in visitados:
            visitados.append(atual)

            for visitado in grafo[atual]:
                if visitado not in visitados and not any(visitado == f["vertice"] for f in fila):
                    novo_caminho = caminho + [visitado]
                    fila.append({"vertice": visitado, "caminho": novo_caminho})

    return None

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
10 - Busca em Largura
11 - Busca em Largura para encontrar Menor Caminho
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
            vi = input("Início: ").strip()
            print("BFS:", bfs(grafo, vi))

        elif opcao == "11":
            vi = input("Início: ").strip()
            vf = input("Destino: ").strip()
            caminho = menor_caminho_bfs(grafo, vi, vf)
            print("Menor caminho:", caminho)

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
