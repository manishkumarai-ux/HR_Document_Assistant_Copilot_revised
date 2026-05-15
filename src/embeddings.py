from langchain_google_genai import GoogleGenerativeAIEmbeddings


def get_embedding_model() -> GoogleGenerativeAIEmbeddings:
    """Return a Google Generative AI embedding model instance.

    The API key is read automatically from the GOOGLE_API_KEY
    environment variable.
    """
    return GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004"
    )
