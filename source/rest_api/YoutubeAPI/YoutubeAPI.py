from youtube_transcript_api import YouTubeTranscriptApi
from langchain.text_splitter import RecursiveCharacterTextSplitter
from Watsonxai.Prompts import *
from VectorDB.VectorDB import *
from Watsonxai.Watsonxai import watsonx_llm

videos = set()
video_summaries = dict()

def get_youtube_video_id(url :str)->str:
  """
  ### Summary
  Extracts the video ID from a YouTube watch URL.

  ### Parameters
  url: The YouTube watch URL.

  ### Returns
  The extracted video ID, or None if the URL is not a valid YouTube watch URL.
  """

  # Check if the URL is a valid YouTube watch URL
  if not url or not url.startswith("https://www.youtube.com/watch?"):
    return None

  # Split the URL by parameters
  params = url.split("?")[1].split("&")

  # Iterate over parameters to find the video ID
  for param in params:
    if param.startswith("v="):
      return param[2:]

  # Video ID not found in the URL
  return None



def get_full_text(video_lines :list[str])->str:
    '''
    ### Summary
    Function to get full text of Youtube Video

    ### Parameters
    video_lines - Chunks of youtube texts.

    ### Returns
    String of complete video text.
    '''

    full_text = ""

    for line in video_lines:
        full_text+=line['text']

    return full_text




def answer_question_about_video(video_id :str, question :str)->str:
    '''
    ### Summary
    Function to answer question about Youtube Videos

    ### Parameters
    Video_id - Youtube Video ID
    Question - user question about youtube video content

    ### Return
    string - Video Answer
    '''

    if video_id not in videos:  # If video not present in VectorDB Collections.
        videos.add(video_id)    # Add video id in VectorDB collection.
        video_content = YouTubeTranscriptApi.get_transcript(video_id,languages=['en'],preserve_formatting=False) # Get video transcript.
        full_text = get_full_text(video_content)          # Get full video text.
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200) # Text Splitter.
        chunks = text_splitter.split_text(full_text)      # Splits text in chunks of 1000 characters.
        setup_collection(name=video_id,documents=chunks)  # Sets vectordb collection.

    query_results = query_database(query=question,collection_name=video_id)[0]  # Query Documents database
    results = '\n\n'.join(query_results)  #Join results to insert into prompt
    prompt = generate_q_a_prompt_youtube_video(video_content=results,user_query=question) #Generate QA Video
    return watsonx_llm.invoke(prompt)

def summarize_video_chunks(chunks :list[str],steps=3)->list[str]:
    '''
    ### Summary
    Function to summarize a whole video into smaller chunks

    ### Parameters
    chunks - list of youtube video chunks to send
    steps - number of chunks to use at once.

    ### Return
    List of summaries
    '''
    summaries = []
    
    for element in range(steps,len(chunks)+1,steps):
        try:
            prompt = summarization_prompt(*chunks[element-steps:element]) #Generate summarization prompt
            summary= watsonx_llm.invoke(prompt) # Call LLM Model
            summaries.append(summary)  #Append answer to list of answers

        except Exception as err:
            print(err)
        
    return summaries

def get_video_summary(video_id:str)->str:
    '''
    ### Summary
    Gets Youtube Summary

    ### Parameters
    Video_id - string

    ### Returns
    Summary of video
    '''

    if(video_id not in video_summaries.keys()):    
        video_content = YouTubeTranscriptApi.get_transcript(video_id=video_id,languages=['en'],preserve_formatting=False) #Get Video Transcript
        full_text = get_full_text(video_content) #Get full text of video
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200) #Configuring text splitter
        
        chunks = text_splitter.split_text(full_text) # Split text into chunks
        resumos = summarize_video_chunks(chunks) # Function to summarize video
        
        complete_text_resumos = '\n'.join(resumos) #Joining complete texts
        text_length = min(len(complete_text_resumos), 3800) #Defining maximum text size as 3800 characters
        prompt = summarization_prompt(complete_text_resumos[:text_length]) #Generate Summarization Prompt
        complete_summary = watsonx_llm.invoke(prompt) #Generate video summary

        video_summaries[video_id] = complete_summary #Add to cache complete video Summary
    else:
       complete_summary = video_summaries[video_id]
       
    return complete_summary