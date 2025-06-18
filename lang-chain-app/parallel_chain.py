from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

model = ChatGroq(model="llama3-8b-8192")

def get_entity_chain():
    entity_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an information extractor."),
        ("human", "Extract key entities from the following text:\n{text}")
    ])
    return entity_prompt | model | StrOutputParser()

def get_summary_chain():
    summary_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a summarizer."),
        ("human", "Summarize the following text:\n{text}")
    ])
    return summary_prompt | model | StrOutputParser()

parallel_chain = RunnableParallel({
    "entities": get_entity_chain(),
    "summary": get_summary_chain()
})