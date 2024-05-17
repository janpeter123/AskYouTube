from typing import Union
from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from YoutubeAPI.YoutubeAPI import get_youtube_video_id, answer_question_about_video,get_video_summary


app = FastAPI()

# Set up CORS
origins = ["*"] #Enabling requests from all origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)   #Adding cors rules

videos = set() #cache of processed videos, this need to be upgraded with a real database


@app.get("/")       #Get route to see Application Status
def read_root():
    return {"Status": "Up"}


@app.post("/ask_video")
def query_video(request :dict):
    try:
        url = request['url']                    #Get request URL
        user_query = request['question']        # Get User Query
        video_id = get_youtube_video_id(url)    #Get YouTube VideoId   

        if(video_id!=None):
            llm_answer = answer_question_about_video(video_id, user_query)  #If video ID is not none, process Video text
            return {"generated_text":llm_answer}
        else:
            raise HTTPException(500,"No Video ID detected")     #Throw Meaningful message in case of error
    
    except Exception as error:
        raise HTTPException(500,f"Problem video q and a service:\n{error}") #Throw complete error

@app.get("/video_summary")
def summarize_video(url :str):
    try:

        video_id = get_youtube_video_id(url)  #Get YouTube VideoId  

        if(video_id!=None):
            summary = get_video_summary(video_id=video_id) #Process video chunks and get summary
            return {"generated_text":summary}    
        else:
            raise HTTPException(500,"No Video ID detected")
        
    except Exception as error:
        raise HTTPException(500,f"Problem video q and a service:\n{error}")



 # running the application
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)