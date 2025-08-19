from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from dot_env import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
)

vector_store = Chroma(
    collection_name="exercise",
    embedding_function=embeddings,
    persist_directory="./excercise",
)

if not os.path_exist(./)

