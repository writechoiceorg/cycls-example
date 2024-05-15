from cycls import AsyncApp
from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

secret = os.getenv("CYCLS_API_KEY")

app = AsyncApp(
    secret=secret,
    handler="@write-choice-ai",
    name="Write Choice's AI",
    image="https://media.licdn.com/dms/image/D4D0BAQFm99CGLCggEQ/company-logo_200_200/0/1707828960215/write_choice_technical_writing_services_logo?e=1723680000&v=beta&t=fpOZeqrgbXd-beQI7LyZC7LcXJJMzttKiftcMWDWX30",
)


client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


@app
async def entry_point(context):
    received_message = context.message.content.text

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": received_message,
            }
        ],
        model="llama3-8b-8192",
    )

    await context.send.text(chat_completion.choices[0].message.content)


app.publish()
