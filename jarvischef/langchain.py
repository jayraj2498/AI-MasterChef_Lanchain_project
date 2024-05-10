from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI
import os



def askJarvisChef(recipe_message):
    # Initialize the ChatOpenAI model with the correct API key
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0)

    # Define the system message prompt
    systemMessagePrompt = SystemMessagePromptTemplate.from_template(
        """your name is MasterChef Jarvis. You are a Master Chef from India. 
        Introduce yourself as a Master Chef. You can write any type of food recipe that can be
        cooked easily using your knowledge. You are only allowed to answer food-related questions.
        If you don't know the answer, simply say "Sorry, I don't know the answer"."""
    )

    # Define the human message prompt
    HumanMessagePrompt = HumanMessagePromptTemplate.from_template('{asked_recipe}')

    # Combine the system and human prompts into a ChatPromptTemplate
    ChatPrompt = ChatPromptTemplate.from_messages([systemMessagePrompt, HumanMessagePrompt])

    # Format the chat prompt with the provided recipe message
    formattedChatPrompt = ChatPrompt.format_messages(asked_recipe=recipe_message)

    # Get the response from the language model
    response = llm(formattedChatPrompt)

    return response.content