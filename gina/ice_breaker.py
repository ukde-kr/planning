from dotenv import load_dotenv
import os

from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser


information = """"
Bong Joon Ho (born September 14, 1969) is a South Korean filmmaker. His work is characterized by emphasis on social and class themes, genre-mixing, dark comedy, and sudden tone shifts.[1] The recipient of numerous accolades, Bong has won three Academy Awards, two British Academy Film Awards, and five Asian Film Awards. In 2017, he was included on Metacritic's list of the 25 best film directors of the 21st century,[2] and in 2020, he was listed as one of the 100 most influential people in the world by Time[3] and among the Bloomberg 50.[4]

Bong first became known to audiences and gained a cult following with his feature directorial debut, the black comedy film Barking Dogs Never Bite (2000). He later achieved widespread critical success with his subsequent films: the crime thriller Memories of Murder (2003), the monster film The Host (2006), the science fiction action film Snowpiercer (2013), which served as Bong's English-language debut, and the black comedy thriller Parasite (2019). The latter three are also among the highest-grossing films in South Korea, with Parasite being the highest-grossing South Korean film in history.[5]

All of Bong's films have been South Korean productions, although Snowpiercer, Okja (2017) and Mickey 17 (2025) are Hollywood co-productions with major use of the English language. Two of his films have screened in competition at the Cannes Film Festival—Okja in 2017 and Parasite in 2019; the latter earned the Palme d'Or, which was a first for a South Korean film.[6][7] Bong won Academy Awards for Best Picture, Best Director, and Best Original Screenplay, making Parasite the first non-English language film to win Best Picture.[8][9]
"""

if __name__ == '__main__':
    
    load_dotenv()
    print('Hello, LangChain!')

    summary_template = """
      given the information {information} about a person or a fictional character, create the following:
      1. a short summary,
      2. two interesting facts about them.
      3. one lie about them.
    """
    summary_prompt_template = PromptTemplate(input_variables = ["information"], template=summary_template)

    llm = ChatGoogleGenerativeAI(temperature=0, model = 'gemini-2.0-flash-001', api_key = os.getenv("GEMINI_API_KEY"))
                     
    chain = summary_prompt_template | llm | StrOutputParser()

    res = chain.invoke(input = {"information": information})

    print(res)