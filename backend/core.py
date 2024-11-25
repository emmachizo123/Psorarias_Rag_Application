from dotenv import load_dotenv
from langchain.chains.retrieval import create_retrieval_chain # the class that performs the Augmentation


load_dotenv()

from langchain import hub
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_pinecone import PineconeVectorStore


from langchain_openai import ChatOpenAI, OpenAIEmbeddings


INDEX_NAME = "psoriasis-doc-index-latest"


def run_llm(query: str):

    print(f"The query is {query}" )
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    docsearch = PineconeVectorStore(index_name=INDEX_NAME, embedding=embeddings)# does the similarity search

    chat = ChatOpenAI(verbose=True, temperature=0)

    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
    stuff_documents_chain = create_stuff_documents_chain(chat, retrieval_qa_chat_prompt)

    qa = create_retrieval_chain(
        retriever=docsearch.as_retriever(), combine_docs_chain=stuff_documents_chain
    )
    result = qa.invoke(input={"input": query})
    #return result
    # note that result is a dictionary with 3 keys ---input,context, answer)
    # you can see this when you run in debug mode/threads and variables

    #lets create result as a dictonary with the keys renamed

    new_result={
        "query" :result["input"],
        "result":result["answer"],
        "source_documents":result["context"]
    }
    return new_result


if __name__ == "__main__":
    #res = run_llm(query="What is a LangChain Chain?")
    #res = run_llm(query="What is an LLM?")
    #res = run_llm(query="what is Psoriatic arthritis (PsA)")
    #res= run_llm(query=" what are the symptions of Psoriatic arthritis")
    #res = run_llm(query=" what is the severity of PsA ")
    res = run_llm(query="what does PSA stand for")
    print(res["result"])
