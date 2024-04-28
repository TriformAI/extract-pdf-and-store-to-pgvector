import os
import json
from llama_index.vector_stores.postgres import PGVectorStore
from llama_index.embeddings.cohere import CohereEmbedding
from llama_index.core.readers import StringIterableReader
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import SentenceSplitter

# Retrieve Cohere API key from environment variables for secure access
COHERE_API_KEY = os.environ['COHERE_API_KEY']
# Retrieve database user and password from environment variables for secure access
DATABASE_HOST = os.environ['DATABASE_HOST']
DATABASE_USER = os.environ['DATABASE_USER']
DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']

# Initialize the PGVectorStore to connect to a PostgreSQL database with specific parameters
vector_store = PGVectorStore.from_params(
    database='postgres',
    host=DATABASE_HOST,
    password= DATABASE_PASSWORD,
    port=5432,
    user=DATABASE_USER,
    table_name='text_storage_table',
    embed_dim=1024  # Set the embedding dimension to 1024
)

# Set up the ingestion pipeline with text processing and embedding transformations
pipeline = IngestionPipeline(
    transformations=[
        SentenceSplitter(chunk_size=512, chunk_overlap=10),  # Split text into sentences with specified chunk size and overlap
        CohereEmbedding(
          cohere_api_key=COHERE_API_KEY,
          model_name='embed-multilingual-v3.0',  # Use specified Cohere model for embeddings
          input_type='search_query'  # Specify the type of input for the embedding model
        )
    ],
    vector_store=vector_store  # Use the initialized vector store for storing embeddings
)
pipeline.disable_cache = True  # Disable caching to ensure all operations are run live

def handler(event, context):
    # Retrieve text from the event object, defaulting to an empty string if not found
    text = event.get('input_0', "")
    
    if not text:
        return {'error': "No text to store provided"}  # Return an error if no text is provided

    # Use the StringIterableReader to load the text into the pipeline
    documents = StringIterableReader().load_data(
        texts=[text]
    )

    # Run the ingestion pipeline with the provided documents
    pipeline.run(documents=documents)

    # Return a success message after successfully processing the text
    return json.dumps({'output_0': "SUCCESS"})
