# AskYouTube

## Summary
AskYouTube is a project where the main scope is to summarize YouTube Videos and answer questions about the content of the video.

The project implements RAG Architecture with the ChromaDB Vector database to index text.


## Working Diagram
![Working Diagram](./documents/architecture/Working%20Diagram.png)

First we get the whole video transcription, then we transform the whole text into chunks, those chunks are transformed into embeddings and then we store it on the ChromaDB.

When a user asks a question we look for the top N documents related to that question and we add as context inside the prompt.

After that the LLM/Generative AI will generate an answer based on the text provided.

## Project Demo

![Video](./AskYTDemo.mov)