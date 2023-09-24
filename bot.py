from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
import pandas as pd
import chainlit as cl
from dotenv import load_dotenv
import os
import io

OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")
llm = OpenAI()


def create_agent(data: str, llm):

    # Create a Pandas DataFrame agent.
    return create_pandas_dataframe_agent(llm, data, verbose=False)


@cl.on_chat_start
async def on_chat_start():

    # Sending an image with the local file path
    elements = [
    cl.Image(name="image1", display="inline", path="./robot.jpeg")
    ]
    await cl.Message(content="Hello there, Welcome to AskAnyQuery related to Data!", elements=elements).send()

    files = []

    # Waits for user to upload csv data
    for idx in range(2):
        file = None
        while file is None:
            file = await cl.AskFileMessage(
                content=f"Please upload a CSV file (File {idx + 1}) to begin!",
                accept=["text/csv"],
                max_size_mb=100,
                timeout=180,
            ).send()
        files.append(file)

    # load the csv data and store in user_session
    data_frames = []
    for file in files:
        file=file[0]
        msg = cl.Message(content=f"Processing `{file.name}`...")
        await msg.send()

        # Read CSV file with pandas
        csv_file = io.BytesIO(file.content)
        df = pd.read_csv(csv_file, encoding="utf-8")
        data_frames.append(df)

        msg.content = f"Processing `{file.name}` done."

        await msg.update()
    # combined_data = pd.concat(data_frames, ignore_index=True)
    data_frames[0].to_csv("file.csv")
    csv_file = io.BytesIO(file.content)
    df = pd.read_csv(csv_file, encoding="utf-8")

    # creating user session to store data
    cl.user_session.set('data', df)

    # Send response back to user
    await cl.Message(
        content="Now you ask me anything related to your data"
    ).send()


@cl.on_message
async def main(message: str):
    try:
        # Get data
        df = cl.user_session.get('data')

        # Agent creation
        agent = create_agent(df, llm)

        # Run model 
        response = agent.run(message)

        # Check if the response contains information from the CSV data
        if response and any(df.apply(lambda row: any(row.str.contains(response, case=False)), axis=1)):

            # Send a response back to the user
            await cl.Message(content=response).send()
        else:
            # Response does not contain information from the CSV data
            await cl.Message(content="Sorry, I cannot find the answer").send()

    except Exception as e:
        print(e)
        await cl.Message(content="An error occurred. Please try again later.").send()