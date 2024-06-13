from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AzureOpenAI

from gpt4o_sandbox.config import settings

endpoint = settings.azure_openai_endpoint
deployment = settings.chat_completions_deployment_name
search_endpoint = settings.search_endpoint
search_index = settings.search_index
api_key = settings.api_key

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)

client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_version="2024-02-01",
    api_key=api_key,
)

completion = client.chat.completions.create(
    model=deployment,
    messages=[
        {"role": "system", "content": "あなたは世界史が大好きです。"},
        {
            "role": "user",
            "content": "土管でダジャレを作ってください。",
        },
        {
            "role": "assistant",
            "content": "土管がドッカン！",
        },
        {"role": "user", "content": "もっとアカデミックなダジャレを作ってください。"},
    ],
)

print(completion.to_json())
