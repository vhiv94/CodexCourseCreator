def build_corpus(docs: list) -> list:
    seen = set()
    for id, text in docs:
        if id in seen:
            raise ValueError()
        seen.add(id)
    return docs.copy()

def get_document_text(corpus: list[tuple[int, str]], id_in: int) -> str:
    for id, text in corpus:
        if id == id_in:
            return text
    raise KeyError()