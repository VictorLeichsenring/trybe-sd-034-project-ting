import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for item in instance.items:
        if item['nome_do_arquivo'] == path_file:
            return
    linhas_do_arquivo = txt_importer(path_file)
    if linhas_do_arquivo is None:
        return
    conteudo_arquivo = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(linhas_do_arquivo),
        "linhas_do_arquivo": linhas_do_arquivo
    }
    instance.enqueue(conteudo_arquivo)
    print(conteudo_arquivo)


def remove(instance):
    if len(instance) == 0:
        print('Não há elementos')
        return

    removed_file = instance.dequeue()
    if removed_file:
        print(
            f"Arquivo {removed_file['nome_do_arquivo']} removido com sucesso"
            )
    else:
        print("Não há elementos")


def file_metadata(instance, position):
    try:
        file_info = instance.search(position)
        print({
            "nome_do_arquivo": file_info['nome_do_arquivo'],
            "qtd_linhas": file_info['qtd_linhas'],
            "linhas_do_arquivo": file_info['linhas_do_arquivo']
        })
    except IndexError:
        print('Posição inválida', file=sys.stderr)
