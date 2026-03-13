import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

prompt = PromptTemplate.from_template("""
You are a senior software architect.

Convert the following requirement into development tasks.

Requirement:
{req}

Return step-by-step tasks for a developer.
""")
shahziab kelwkekwejjkkj;kkjkljjjkljk
--requirement = input("Enter requirement: ")

formatted_prompt = prompt.format(req=requirement)

response = llm.invoke(formatted_prompt)

print("\nDevelopment Plan:\n")
print(response.content)
