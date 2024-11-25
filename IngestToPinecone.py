

from dotenv import load_dotenv
load_dotenv()

from langchain_text_splitters import RecursiveCharacterTextSplitter

# import ReadTheDocsLoaders used to pull doumentation directly from sites built with Read the Docs


from langchain_community.document_loaders import ReadTheDocsLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

##create openai embedding object that will be used to turn the documents into vectors

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

#function to hold all ingestion document


def ingest_docs():
    print("I am here")
    loader = ReadTheDocsLoader("./store-docs",encoding="latin-1")
    raw_documents = loader.load()
    print(f"loaded {len(raw_documents)} documents")

   # loader =ReadTheDocsLoader("./langchain-docs/langchain-docs/api.python.langchain.com/en/latest",encoding="utf-8")
    #loader = ReadTheDocsLoader("./store-docs", encoding="utf-8")
    #loader = ReadTheDocsLoader("./store-docs")

    print("I am here 2")

    print("I am here 3")


    #becuase the document is big we need to split into chunck
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=600,chunk_overlap=50)

    #text_splitter = RecursiveCharacterTextSplitter(chunk_size=30, chunk_overlap=5)
    documents = text_splitter.split_documents(raw_documents)

    #iterate through the document and for each document I want to create a new url
    #it will be a string we will add to the document metadata indicating where it will take the chunch from

    for  doc in documents:
        new_url =doc.metadata["source"]
        new_url =new_url.replace("langchain-docs","https:/")
        #update document metadata
        doc.metadata.update({"source":new_url})

    print(f"Going to add {len(documents)} to pinecone")

    #this functions takes the documents and embeds them into vector store and indexes the document as "langchain_doc_index"
    PineconeVectorStore.from_documents(
        documents,embeddings, index_name="psoriasis-doc-index-latest"
    )
    print("loaded to vector store done")



if __name__ == "__main__":
    ingest_docs()
