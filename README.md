# AskYouTube

## Summary
AskYouTube is a project where the main scope is to summarize YouTube Videos and answer questions about the content of the video.

The project implements RAG Architecture with the ChromaDB Vector database to index text.


## Working Diagram
![Working Diagram](./documents/architecture/Working%20Diagram.png)

First we get the whole video transcription, then we transform the whole text into chunks, those chunks are transformed into embeddings and then we store it on the ChromaDB.

When a user asks a question we look for the top N documents related to that question and we add as context inside the prompt.

After that the LLM/Generative AI will generate an answer based on the text provided.

The project also counts with a simple caching system to process a video only once, after that the summary and the text embedding will never be done again. So when you search for a video that has been added to the application it will retrieve the summary instantly.

>Note: Known problems, Video Id's should not start with numbers or special characters such as '-' or '_'

## Project Demo

![Video](./AskYTDemo.mov)

## How to use it

1. First add the video URL

![Add Video URL](./documents/images/add_url.png)



2. Wait a couple of seconds

![Add Video URL](./documents/images/wait.png)


3. Get the Summary and ask questions about the video content

![Add Video URL](./documents/images/ask.png)


## How to setup the project

### Rest API Setup
Go to `./source/rest_api` folder and run the following command to install the project dependencies

`pip install -r requirements.txt`

Then, copy the `.env.example` file with the name `.env` and fill it with all the necessary credentials.

After that you can run the project in dev mode with

`uvicorn main:app --reload`

Or if you wish to run a containerized version of the application you can run

`docker build -t rest_api .`

After building your image you should run your application with

`docker run -p 8000:8000 rest_api`


### Front End Setup
Go to `./source/front_end` folder and run the following command to install the project dependencies

`npm i`

after that run

`npm run dev`

The project should be available at `http://localhost:3000`

Or if you wish to run a containerized version of the application you can run

`docker build -t front .`

After building your image you should run your application with

`docker run -p 3000:3000 front`


Have fun!

>Note: This builds are not suitable for production


