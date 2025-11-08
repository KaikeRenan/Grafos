def criar_grafo():
    return [], []


def adicionar_vertice(matriz, vertices, vertice):
    if vertice in vertices:
        print(f"Vértice {vertice} já existe")
        return

    vertices.append(vertice)
    n = len(vertices)

    for linha in matriz:
        linha.append(0)
    
    matriz.append([0] * n)


def adicionar_aresta(matriz, vertices, vi, vf, nao_direcionado=False):
    if vi not in vertices:
        adicionar_vertice(matriz, vertices, vi)
    if vf not in vertices:
        adicionar_vertice(matriz, vertices, vf)

    i = vertices.index(vi)
    j = vertices.index(vf)

    if matriz[i][j] == 1:
        print(f"Aresta {vi} -> {vf} já existe")
        return

    matriz[i][j] = 1
    if nao_direcionado:
        matriz[j][i] = 1


def remover_vertice(matriz, vertices, vertice):
    if vertice not in vertices:
        print(f"Vértice {vertice} não existe")
        return

    i = vertices.index(vertice)

    matriz.pop(i)

    for linha in matriz:
        linha.pop(i)

    vertices.remove(vertice)
    print(f"Vértice {vertice} removido")


def remover_aresta(matriz, vertices, vi, vf, nao_direcionado=False):
    if vi not in vertices or vf not in vertices:
        print("Um dos vértices não existe")
        return

    i = vertices.index(vi)
    j = vertices.index(vf)

    if matriz[i][j] == 0:
        print(f"Aresta {vi} -> {vf} não existe")
    else:
        matriz[i][j] = 0
        print(f"Aresta {vi} -> {vf} removida")

    if nao_direcionado:
        matriz[j][i] = 0


def existe_aresta(matriz, vertices, vi, vf):
    if vi not in vertices or vf not in vertices:
        return False
    i = vertices.index(vi)
    j = vertices.index(vf)
    return matriz[i][j] == 1


def vizinhos(matriz, vertices, vertice):
    if vertice not in vertices:
        print(f"Vértice {vertice} não existe")
        return []
    i = vertices.index(vertice)
    return [vertices[j] for j in range(len(vertices)) if matriz[i][j] == 1]


def listar_vizinhos(matriz, vertices, vertice):
    if vertice not in vertices:
        print(f"Vértice {vertice} não encontrado")
        return
    print(f"Vizinhos de {vertice}: {vizinhos(matriz, vertices, vertice)}")


def exibir_grafo(matriz, vertices):
    if not vertices:
        print("Grafo vazio")
        return

    print("Matriz de Adjacência:")
    print("    " + "  ".join(vertices))
    for i, v in enumerate(vertices):
        linha = "  ".join(str(x) for x in matriz[i])
        print(f"{v}: {linha}")


def grau_vertices(matriz, vertices, nao_direcionado=False):
    graus = {}
    for i, v in enumerate(vertices):
        out_ = sum(matriz[i])
        in_ = sum(matriz[j][i] for j in range(len(vertices)))
        if nao_direcionado:
            total = out_
        else:
            total = in_ + out_
        graus[v] = {"in": in_, "out": out_, "total": total}
    return graus


def percurso_valido(matriz, vertices, caminho):
    if len(caminho) < 2:
        return True

    for i in range(len(caminho) - 1):
        if not existe_aresta(matriz, vertices, caminho[i], caminho[i + 1]):
            return False
    return True


def main():
    matriz, vertices = criar_grafo()
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
            exibir_grafo(matriz, vertices)

        elif opcao == "2":
            v = input("Nome do vértice: ").strip()
            adicionar_vertice(matriz, vertices, v)

        elif opcao == "3":
            vi = input("Vértice Inicial: ").strip()
            vf = input("Vértice Final: ").strip()
            adicionar_aresta(matriz, vertices, vi, vf, nao_direcionado)

        elif opcao == "4":
            v = input("Vértice a remover: ").strip()
            remover_vertice(matriz, vertices, v)

        elif opcao == "5":
            vi = input("Inicial: ").strip()
            vf = input("Final: ").strip()
            remover_aresta(matriz, vertices, vi, vf, nao_direcionado)

        elif opcao == "6":
            v = input("Vértice: ").strip()
            listar_vizinhos(matriz, vertices, v)

        elif opcao == "7":
            vi = input("Inicial: ").strip()
            vf = input("Final: ").strip()
            print("Existe aresta?", existe_aresta(matriz, vertices, vi, vf))

        elif opcao == "8":
            graus = grau_vertices(matriz, vertices, nao_direcionado)
            for v, g in graus.items():
                print(f"{v}: in={g['in']}, out={g['out']}, total={g['total']}")

        elif opcao == "9":
            caminho = input("Digite os vértices separados por espaço: ").split()
            print("Percurso válido?", percurso_valido(matriz, vertices, caminho))

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
