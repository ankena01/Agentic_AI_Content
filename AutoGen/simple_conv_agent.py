import os
from autogen import ConversableAgent
from dotenv import load_dotenv

load_dotenv()

model = "gpt-3.5-turbo"
llm_config = {'model' : model,
              'api_key' : os.getenv('OPENAI_API_KEY')}

agent = ConversableAgent(
    name = 'chatbot',
    llm_config=llm_config,
    code_execution_config = False,
    human_input_mode = 'NEVER'
)


response = agent.generate_reply(
    messages = [{'role' : 'user' ,
                'content' : 'What is the capital of France?'}]
)

print(response)