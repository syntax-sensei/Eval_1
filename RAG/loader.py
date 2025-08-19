from langchain_community.document_loaders.csv_loader import UnstructuredCSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

loader = UnstructuredCSVLoader(
    file_path="../RAG/docs/exercises.csv", mode="elements"
)

docs = loader.load()

# print(docs[0].metadata["text_as_html"])

html_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.HTML, chunk_size=500, chunk_overlap=100
)
html_docs = html_splitter.create_documents([str(docs)])

# print(html_docs)

