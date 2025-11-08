def criar_grafo():
    return {}


def adicionar_vertice(grafo, vertice):
    if vertice not in grafo:
        grafo[vertice] = []
    else:
        print(f"vértice {vertice} já existe")


def adicionar_aresta(grafo, vertice_inicial, vertice_final, nao_direcionado=False):
    if vertice_inicial not in grafo:
        adicionar_vertice(grafo, vertice_inicial)
    if vertice_final not in grafo:
        adicionar_vertice(grafo, vertice_final)

    if vertice_final not in grafo[vertice_inicial]:
        grafo[vertice_inicial].append(vertice_final)
    else:
        print(f"Aresta {vertice_inicial} -> {vertice_final} já existe")

    if nao_direcionado:
        if vertice_inicial not in grafo[vertice_final]:
            grafo[vertice_final].append(vertice_inicial)


def vizinhos(grafo, vertice):
    if vertice in grafo:
        return grafo[vertice]
    else:
        print(f"Vértice {vertice} não existe")
        return []


def listar_vizinhos(grafo, vertice):
    if vertice in grafo:
        print(f"Vizinhos de {vertice}: {grafo[vertice]}")
    else:
        print(f"Vértice {vertice} não encontrado")


def exibir_grafo(grafo):
    if not grafo:
        print("Grafo vazio")
    else:
        for vertice in grafo:
            print(f"{vertice} ---> {grafo[vertice]}")


def remover_vertice(grafo, vertice):
    if vertice not in grafo:
        print(f"Vértice {vertice} não existe")
        return

    del grafo[vertice]

    for origem in grafo:
        if vertice in grafo[origem]:
            grafo[origem].remove(vertice)

    print(f"Vértice {vertice} removido")


def remover_aresta(grafo, vertice_inicial, vertice_final, nao_direcionado=False):
    if vertice_inicial not in grafo:
        print(f"Vértice inicial {vertice_inicial} não existe")
        return

    if vertice_final in grafo[vertice_inicial]:
        grafo[vertice_inicial].remove(vertice_final)
        print(f"Aresta {vertice_inicial} -> {vertice_final} removida")
    else:
        print(f"Aresta {vertice_inicial} -> {vertice_final} não existe")

    if nao_direcionado:
        if vertice_final not in grafo:
            return
        if vertice_inicial in grafo[vertice_final]:
            grafo[vertice_final].remove(vertice_inicial)
            print(f"Aresta {vertice_final} -> {vertice_inicial} removida")


def existe_aresta(grafo, vertice_inicial, vertice_final):
    return vertice_inicial in grafo and vertice_final in grafo[vertice_inicial]


def grau_vertices(grafo):
    graus = {}

    for v in grafo:
        graus[v] = {"in": 0, "out": len(grafo[v]), "total": 0}

    for vertice_inicial in grafo:
        for vertice_final in grafo[vertice_inicial]:
            if vertice_final in graus:
                graus[vertice_final]["in"] += 1
            else:
                graus.setdefault(vertice_final, {"in": 1, "out": 0, "total": 0})

    for v in list(graus.keys()):
        graus[v]["total"] = graus[v]["in"] + graus[v]["out"]

    return graus


def percurso_valido(grafo, caminho):
    if len(caminho) < 2:
        return True

    for i in range(len(caminho) - 1):
        vertice_inicial = caminho[i]
        vertice_final = caminho[i + 1]
        if not existe_aresta(grafo, vertice_inicial, vertice_final):
            return False
    return True


def main():
    grafo = criar_grafo()
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
0 - Sair
"""
        )
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            exibir_grafo(grafo)

        elif opcao == "2":
            v = input("Nome do vértice: ").strip()
            adicionar_vertice(grafo, v)

        elif opcao == "3":
            vi = input("Vértice Inicial: ").strip()
            vf = input("Vértice Final: ").strip()
            adicionar_aresta(grafo, vi, vf, nao_direcionado)

        elif opcao == "4":
            v = input("Vértice a remover: ").strip()
            remover_vertice(grafo, v)

        elif opcao == "5":
            vi = input("Inicial: ").strip()
            vf = input("Final: ").strip()
            remover_aresta(grafo, vi, vf, nao_direcionado)

        elif opcao == "6":
            v = input("Vértice: ").strip()
            listar_vizinhos(grafo, v)

        elif opcao == "7":
            vi = input("Inicial: ").strip()
            vf = input("Final: ").strip()
            print("Existe aresta?", existe_aresta(grafo, vi, vf))

        elif opcao == "8":
            graus = grau_vertices(grafo)
            for v, g in graus.items():
                print(f"{v}: in={g['in']}, out={g['out']}, total={g['total']}")

        elif opcao == "9":
            caminho = input("Digite os vértices separados por espaço: ").split()
            print("Percurso válido?", percurso_valido(grafo, caminho))

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
