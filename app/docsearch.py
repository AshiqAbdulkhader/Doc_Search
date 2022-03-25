from docarray import Document, DocumentArray
from jina import Executor

encoder = Executor.load_config(
    'DPRTextEncoder/config.yml', uses_with={'device': 'cuda'})
indexer = Executor.load_config(
    'SimpleIndexer/config.yml', uses_metas={'workspace': './workspace'})
ranker = Executor.load_config(
    'DPRReaderRanker/config.yml', uses_metas={'workspace': './workspace'})

with open("./data/tp_encoded.json", "r") as f:
    encoder_json = f.read()

da = DocumentArray.from_json(encoder_json)

encoder.encode(docs=da)
indexer.index(docs=da)


def query(question):
    q_da = DocumentArray([Document(text=question)])
    encoder.encode(docs=q_da)
    indexer.search(docs=q_da)
    ranker.rank(docs=q_da)
    return q_da[0].matches[:1][0].text
