import glob
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

def load_code(path="my_codes/**/*.*"):
    files = glob.glob(path, recursive=True)
    docs = []
    for f in files:
        try:
            with open(f, "r", encoding="utf-8") as fh:
                docs.append({"content": fh.read(), "source": f})
        except:
            pass
    return docs

def chunk_docs(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100,
        separators=["\nclass ", "\ndef ", "\n\n", "\n"]
    )
    out = []
    for d in docs:
        chunks = splitter.split_text(d["content"])
        for c in chunks:
            out.append({"content": c, "source": d["source"]})
    return out

emb = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def build_store():
    docs = load_code()
    chunks = chunk_docs(docs)
    texts = [c["content"] for c in chunks]
    metas = [{"source": c["source"]} for c in chunks]

    store = Chroma.from_texts(
        texts=texts,
        embedding=emb,
        metadatas=metas,
        persist_directory="rag_store"
    )
    store.persist()
    print("RAG adatbázis elkészült. Chunkok száma:", len(texts))

if __name__ == "__main__":
    build_store()
