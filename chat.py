from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_classic.chains import RetrievalQA
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="aron_persona")

emb = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

store = Chroma(
    embedding_function=emb,
    persist_directory="rag_store"
)

retriever = store.as_retriever(search_kwargs={"k": 5})

rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff"
)

print("\n\n\nCHAT starts. (type 'exit' to leave)\n")

while True:
    q = input("Question: ")
    if q.strip().lower() == "exit":
        break
    
    answer = rag_chain.invoke({"query": q})
    print("\nAnswer:")
    print(answer["result"])
    print("-" * 40)