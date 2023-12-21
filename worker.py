import os
import chromadb
# Import necessary modules from langchain
from langchain import OpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

# Load environment variables
load_dotenv()

# Initialize global variables
conversation_retrieval_chain = None
chat_history = []
llm = None
llm_embeddings = None

# Function to initialize the language model and its embeddings
def init_llm():
    global llm, llm_embeddings
    # Initialize the language model with the OpenAI API key
    api_key="YOUR API KEY"
    llm = OpenAI(api_key=api_key)  # Initialize the language model here
    
    # Initialize the embeddings for the language model
    llm_embeddings = OpenAIEmbeddings(openai_api_key = api_key)

# Function to process a PDF document
def process_document(document_list, multiple = None ):
    global conversation_retrieval_chain, llm, llm_embeddings

    for file_ in document_list:

        loader   = PyPDFLoader(file_)
        pages    = loader.load()
        document = []
        for page in pages: 
            texts = text_splitter.split_documents(page)
            document.append(texts)
        db = Chroma.from_documents(documents, llm_embeddings)
    
    # Create a vector store from the document chunks
    retriever = client.as_retriever(search_type="similarity", search_kwargs={"k": 2})
    conversation_retrieval_chain = ConversationalRetrievalChain.from_llm(llm, retriever)

    
# Function to process a user prompt
def process_prompt(prompt):
    global conversation_retrieval_chain
    global chat_history
    # Pass the prompt and the chat history to the conversation_retrieval_chain object
    result = conversation_retrieval_chain({"question": prompt, "chat_history": chat_history})
    chat_history.append({"user": prompt, "assistant": result['answer']})  # Append the prompt and the bot's response to the chat history here

    # Return the model's response
    return result['answer']


# Initialize the language model
init_llm()
