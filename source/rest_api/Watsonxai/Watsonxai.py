import os
from dotenv import load_dotenv
from getpass import getpass
from langchain_ibm import WatsonxLLM
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from Watsonxai.Prompts import summarization_prompt


load_dotenv()

apikey = os.getenv("IBM_CLOUD_API_KEY")
project_id = os.getenv("WATSONXAI_PROJECT_ID")
watsonx_url = os.getenv("WATSONXAI_URL")

model_id = "meta-llama/llama-3-70b-instruct"

parameters = {
    "decoding_method": "greedy",
    "max_new_tokens": 1000,
    "min_new_tokens": 0
}

watsonx_llm = WatsonxLLM(
    apikey=apikey,
    model_id=model_id,
    url = watsonx_url,
    project_id= project_id,
    params=parameters
)




def summarize_prompts(chunks :list[str],steps=3)->list[str]:
    '''
    ### Summary
    Summarizes video content

    ### Parameters
    Chunks - List of strings to be summarized
    Steps - Number of prompts to use at once

    ### Returns
    List of summaries
    '''

    resumos = []
    
    for element in range(steps,len(chunks)+1,steps):
        try:
            prompt = summarization_prompt(*chunks[element-steps:element])
            resposta = watsonx_llm.invoke(prompt)
            resumos.append(resposta)

        except Exception as err:
            print(err)
        
    return resumos