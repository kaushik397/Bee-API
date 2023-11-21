from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
import openai
import json
from langchain.llms import OpenAI
# from secret import test_key


def TopicGen(topic,difficulty,apiKey):
  template="""As a expert teacher on {topic} prepare list of required important sub-topics to teach students who are {difficulty}. return it in a JSON object with variables topic and sub_topics."""
  prompt = PromptTemplate(template=template, input_variables=["topic","difficulty"])
  llm=OpenAI(openai_api_key=apiKey,temperature=0.6,max_tokens=800)
  llm_chain=LLMChain(prompt=prompt, llm=llm)
  response=llm_chain.run({"topic":topic,"difficulty":difficulty})
  # print(response)
  responseret=json.loads(response)
  try:
    return responseret
  except:
    return {"Error":"Unable to create JSON data format pls check logs"}