from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

'''
Temperature:-
It is a parameter that controls the randomness of a language model's output. 
It affects how creative or deterministic the responses are.
-> Lower values (0.00.3) More deterministic and predictable.
-> Higher values (0.71.5)More random, creative, and diverse.
'''

model = ChatOpenAI(model='gpt-4o-mini', temperature=0, max_completion_tokens=10)

result = model.invoke("What is the capital of India")

print(result)