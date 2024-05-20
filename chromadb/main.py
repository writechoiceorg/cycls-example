from cycls import AsyncApp
from dotenv import load_dotenv
import chromadb
import os

load_dotenv()

chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="my_collection")

collection.add(
    documents=[
        "This is a document about pineapple",
        "This is a document about oranges",
    ],
    ids=["id1", "id2"],
)

secret = os.getenv("CYCLS_API_KEY")

app = AsyncApp(
    secret=secret,
    handler="@your-handler",
)


@app
async def entry_point(context):
    received_message = context.message.content.text

    results = collection.query(query_texts=[received_message], n_results=2)
    print(results)
    await context.send.text(str(results))


app.publish()
