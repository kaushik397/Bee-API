from langchain import PromptTemplate, LLMChain
from langchain.chains import SequentialChain
import openai
from langchain.llms import OpenAI
import json
from secret import test_key

def questionGen(topic):
  template="""
  As a teacher with expertise knowledge on {topic} create 5 questions with distributed difficulty level being a scale of 0 to 3000 in which 0 is easiest and 3000 is hardest and 1500 is medium to test the knowledge of students and teach better and of type MCQ with four different options and one correctAanswer. and return everything in a JSON object with variables question, options, correct answer, and difficulty level of question.
  """
  prompt = PromptTemplate(template=template, input_variables=["topic"])
  llm=OpenAI(openai_api_key=test_key,temperature=0.6,max_tokens=1500)
  llm_chain=LLMChain(prompt=prompt, llm=llm)
  response=llm_chain.run({"topic":topic})
  # print(response)
  try:
    responseret=json.loads(response)
    return responseret
  except:
    return {"Error":"Unable to create JSON data format pls check logs"}