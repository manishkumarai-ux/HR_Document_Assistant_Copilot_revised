from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


def get_llm_model() -> ChatGoogleGenerativeAI:
    """Return a Google Gemini chat model instance.

    The API key is read automatically from the GOOGLE_API_KEY
    environment variable.
    """
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0
    )
