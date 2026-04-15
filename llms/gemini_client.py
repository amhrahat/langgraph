from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model
from langchain_core.language_models.chat_models import BaseChatModel
load_dotenv()

os.environ['GEMINI_API_KEY']


def get_llm_instance() -> BaseChatModel:
    return init_chat_model(
    "gemini-3-flash-preview",
    model_provider="google_genai",
    temperature=0
)


llm = get_llm_instance()
# response = llm.invoke("hello")
# print(response.content)