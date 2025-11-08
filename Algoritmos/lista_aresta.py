def criar_grafo():
    return [], []


def adicionar_vertice(vertices, vertice):
    if vertice in vertices:
        print(f"Vértice {vertice} já existe")
    else:
        vertices.append(vertice)


def adicionar_aresta(vertices, arestas, vi, vf, nao_direcionado=False):
    if vi not in vertices:
        adicionar_vertice(vertices, vi)
    if vf not in vertices:
        adicionar_vertice(vertices, vf)

    if [vi, vf] in arestas:
        print(f"Aresta {vi} -> {vf} já existe")
        return

    arestas.append([vi, vf])

    if nao_direcionado:
        if [vf, vi] not in arestas:
            arestas.append([vf, vi])


def remover_aresta(arestas, vi, vf, nao_direcionado=False):
    if [vi, vf] in arestas:
        arestas.remove([vi, vf])
        print(f"Aresta {vi} -> {vf} removida")
    else:
        print(f"Aresta {vi} -> {vf} não existe")

    if nao_direcionado and [vf, vi] in arestas:
        arestas.remove([vf, vi])
        print(f"Aresta {vf} -> {vi} removida")


def remover_vertice(vertices, arestas, vertice):
    if vertice not in vertices:
        print(f"Vértice {vertice} não existe")
        return

    vertices.remove(vertice)

    arestas[:] = [a for a in arestas if vertice not in a]
    print(f"Vértice {vertice} removido")


def existe_aresta(arestas, vi, vf):
    return [vi, vf] in arestas


def vizinhos(vertices, arestas, vertice):
    if vertice not in vertices:
        print(f"Vértice {vertice} não existe")
        return []

    return [vf for vi, vf in arestas if vi == vertice]


def listar_vizinhos(vertices, arestas, vertice):
    if vertice not in vertices:
        print(f"Vértice {vertice} não encontrado")
        return
    print(f"Vizinhos de {vertice}: {vizinhos(vertices, arestas, vertice)}")


def exibir_grafo(vertices, arestas):
    if not vertices:
        print("Grafo vazio")
        return

    print("Vértices:", vertices)
    print("Arestas:")
    for vi, vf in arestas:
        print(f"{vi} -> {vf}")


def grau_vertices(vertices, arestas, nao_direcionado=False):
    graus = {v: {"in": 0, "out": 0, "total": 0} for v in vertices}

    for vi, vf in arestas:
        if vi in graus:
            graus[vi]["out"] += 1
        if vf in graus:
            graus[vi]["in"] += 1

    for v in graus:
        if nao_direcionado:
            graus[v]["total"] = graus[v]["out"]
        else:
            graus[v]["total"] = graus[v]["in"] + graus[v]["out"]

    return graus


def percurso_valido(arestas, caminho):
    if len(caminho) < 2:
        return True

    for i in range(len(caminho) - 1):
        if [caminho[i], caminho[i + 1]] not in arestas:
            return False
    return True


def main():
    vertices, arestas = criar_grafo()
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
            exibir_grafo(vertices, arestas)

        elif opcao == "2":
            v = input("Nome do vértice: ").strip()
            adicionar_vertice(vertices, v)

        elif opcao == "3":
            vi = input("Vértice Inicial: ").strip()
            vf = input("Vértice Final: ").strip()
            adicionar_aresta(vertices, arestas, vi, vf, nao_direcionado)

        elif opcao == "4":
            v = input("Vértice a remover: ").strip()
            remover_vertice(vertices, arestas, v)

        elif opcao == "5":
            vi = input("Inicial: ").strip()
            vf = input("Final: ").strip()
            remover_aresta(arestas, vi, vf, nao_direcionado)

        elif opcao == "6":
            v = input("Vértice: ").strip()
            listar_vizinhos(vertices, arestas, v)

        elif opcao == "7":
            vi = input("Inicial: ").strip()
            vf = input("Final: ").strip()
            print("Existe aresta?", existe_aresta(arestas, vi, vf))

        elif opcao == "8":
            graus = grau_vertices(vertices, arestas, nao_direcionado)
            for v, g in graus.items():
                print(f"{v}: in={g['in']}, out={g['out']}, total={g['total']}")

        elif opcao == "9":
            caminho = input("Digite os vértices separados por espaço: ").split()
            print("Percurso válido?", percurso_valido(arestas, caminho))

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente!")


if __name__ == "__main__":
    main()
