from typing import Iterable

from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AzureOpenAI
from openai.types.chat import ChatCompletionMessageParam

from gpt4o_sandbox.config import settings

endpoint = settings.azure_openai_endpoint
deployment = settings.chat_completions_deployment_name
api_key = settings.api_key

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)

client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_version="2024-02-01",
    api_key=api_key,
)

message_madori: Iterable[ChatCompletionMessageParam] = [
    {"role": "system", "content": "あなたは建築のプロです。"},
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "この間取り図の解説と、良いところ・懸念点を教えて下さい。",
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": "https://images.edrawsoft.com/jp/articles/edraw-max/architectural-design05.png"
                },
            },
        ],
    },
]

message_db: Iterable[ChatCompletionMessageParam] = [
    {"role": "system", "content": "あなたはDB設計のプロです。"},
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "ER図をもとに、DB定義を表で作成してください。",
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": "https://storage.googleapis.com/studio-cms-assets/projects/G3qboNYbaJ/s-1918x1338_v-frms_webp_a65deca3-3076-4f72-b7ad-d2e95e3c9de5_middle.webp",
                },
            },
        ],
    },
]

message_wara: Iterable[ChatCompletionMessageParam] = [
    {"role": "system", "content": "あなたは大喜利が得意です"},
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "大喜利です。画像で一言お願いします。",
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": "https://www.min-breeder.com/data/magazine/16384/main_16384_75588_detail.jpg",
                },
            },
        ],
    },
]

message_meishi: Iterable[ChatCompletionMessageParam] = [
    {"role": "system", "content": "名刺の情報を整理するシステムです。"},
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "名刺の内容を整理してください。",
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": "https://www.graphic.jp/smapri_design/preview_template/12050121010184421415048314103018245",
                },
            },
        ],
    },
]

response = client.chat.completions.create(model=deployment, messages=message_meishi)

print(response.to_json())
print(response.choices[0].message.content)
