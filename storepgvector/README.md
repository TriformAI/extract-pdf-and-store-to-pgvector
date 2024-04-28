# Triform.ai Template: Text Embedding and Storage Pipeline

## Overview
This template facilitates text ingestion, processing, and storage using the Cohere embedding model and PostgreSQL. It is optimized for use within the Triform platform to enable advanced text analysis and AI workflows.

In addition to an Anthropic account you need a remote Postgres PGVector database instance. You can [create a Postgres PGVector database instance to Supabase](https://supabase.com/docs/guides/database/extensions/pgvector). Setting it up is easy and it's free.  

## How it Works
The script initializes a connection to a PostgreSQL database and sets up an ingestion pipeline using Cohere's embedding API. Text data is processed, embedded, and stored in a specified database table. The process is secured with environment variables for sensitive credentials.

## Use Cases
- Storing embedded representations of text for quick retrieval and comparison.
- Building a searchable index of large text datasets.
- Enhancing data-driven applications with pre-processed and easily accessible text data.

## Customization
The module can be customized to:
- Use different embedding models or suppliers by modifying the Cohere model settings.
- Connect to various databases by adjusting the `PGVectorStore` parameters.
- Handle different text preprocessing requirements by changing the `SentenceSplitter` settings.

## Environment Setup
Set the following environment variables:
- `COHERE_API_KEY` for the Cohere API key.
- `DATABASE_USER` and `DATABASE_PASSWORD` for database credentials.