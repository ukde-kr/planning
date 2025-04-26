import os
from dotenv import load_dotenv
from langchain.agents import (create_react_agent, AgentExecutor,)
from langchain import hub
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
import tools

load_dotenv()

def lookup(name: str)-> str:
    llm = ChatOpenAI(
        temperature = 0, 
        model_name = 'gpt-3.5-turbo',
    )

    template = """given the full name {name_of_person} I want you to get me a link to their wikipedia page.
                your answer should only contain a URL. """
    
    prompt_template = PromptTemplate(
        template = template, input_variables=['name_of_person']
    )

    tools_for_agent = [
        Tool(
            name = 'Crawl google for wiki page',
            func = get_url_tavily
            description = "useful for when you get the wikipedia URL",
        )
    ]

    react_prompt = hub.pull('hschase12/react')
    agent = create_react_agent(llm = llm, tools = tools_for_agent, prompt = react_prompt)
    agent_executor = AgentExecutor(agent = agent, tools = tools_for_agent, verbose=True)
    
    result = agent_executor.invoke(
        input = {"input": prompt_template.format_prompt(name_of_person=name)}
    )


if __name__ == "__main__":
    wiki_url = lookup(name= 'Bong Joon Ho')
    print(wiki_url)