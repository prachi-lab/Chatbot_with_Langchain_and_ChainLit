# Chatbot_with_Langchain_and_ChainLit
## Langchain:
Langchain is an open-source library that provides developers the tools to build applications backed by large language models (LLMs). It provides a standard interface for chaining together different components to create more advanced use cases around LLMs. These components include:

- **Prompt templates:** Templates for different types of prompts, such as "chatbot" style templates, ELI5 question-answering, etc.
- **LLMs:** Large language models like OpenAI Models, Anthropic, Azure, BLOOM, etc.
- **Agents:** Use LLMs to decide what actions should be taken.
- **Memory:** It refers to persisting state between calls of a chain/agent.
- **Evaluation:** Evaluates the performance of chains and agents.
Langchain also provides a number of integrations with other tools, such as:

- **OpenAI API:** OpenAI API provide access to its models.
- **Hugging Face Transformers:** It is a library for working with LLMs & custom models.
- **Chainlit:** Chainlit is a library for creating user interfaces for chatbots expecially for LLMs.
## Chainlit:
Chainlit is an open-source library that makes it easy to create user interfaces for chatbots powered by large language models (LLMs). It is built on top of the React framework and provides a number of features that make it easy to create interactive and engaging chatbot experiences.

Some of the key features of Chainlit include:

- **Easy integration with LLMs:** Chainlit can be easily integrated with any LLM that supports the OpenAI API. This makes it easy to create chatbots that can generate text, translate languages, answer questions, and more.
- **Flexible UI components:** Chainlit provides a number of flexible UI components that can be used to create a variety of chatbot experiences. These components include text boxes, buttons, dropdown menus, and more.
- **Support for custom styling:** Chainlit supports custom styling, so you can easily customize the look and feel of your chatbot.
- **Easy deployment:** Chainlit can be deployed to any web server, making it easy to share your chatbot with others.

## Getting Started
### - Set up a virtual environment
### Requirements:
**`pip install chainlit langchain tabulate pandas openai`**
### Use
> Python Version: 3.10
### To run UI:
**`chainlit run bot.py -w`**
![image](https://github.com/prachi-lab/Chatbot_with_Langchain_and_ChainLit/assets/63344962/97176879-56da-49ed-a45e-e55f50def974)

#### When question is related to the data from the provided files
![image](https://github.com/prachi-lab/Chatbot_with_Langchain_and_ChainLit/assets/63344962/20cdb653-c95a-41c5-af75-1388cb024d77)
#### When question is not related to the data from the provided files
![image](https://github.com/prachi-lab/Chatbot_with_Langchain_and_ChainLit/assets/63344962/9df7fc16-a8b7-447f-bea9-a2298d33e758)


# Note:
**Error will be there because of using free OPENAI_API_KEY**
![image](https://github.com/prachi-lab/Chatbot_with_Langchain_and_ChainLit/assets/63344962/d8394a50-9d5e-4e87-b6a5-7b074a727ce6)

**To avoid this use paid OPENAI_API_KEY**








