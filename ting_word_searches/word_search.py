def exists_word(word, instance):
    results = []
    word_lower = word.lower()

    for file_info in instance.items:
        occurrences = []
        file_lines = file_info['linhas_do_arquivo']
        for index, line in enumerate(file_lines, start=1):
            if word_lower in line.lower():
                occurrences.append({"linha": index})

        if occurrences:
            results.append({
                "palavra": word,
                "arquivo": file_info['nome_do_arquivo'],
                "ocorrencias": occurrences
            })

    return results


def search_by_word(word, instance):
    results = []
    word_lower = word.lower()

    for file_info in instance.items:
        occurrences = []
        file_lines = file_info['linhas_do_arquivo']

        for index, line in enumerate(file_lines, start=1):
            if word_lower in line.lower():
                occurrences.append({
                    "linha": index,
                    "conteudo": line.strip()
                })

        if occurrences:
            results.append({
                "palavra": word,
                "arquivo": file_info['nome_do_arquivo'],
                "ocorrencias": occurrences
            })
    return results
