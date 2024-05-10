def generate_q_a_prompt_youtube_video(video_content :str,user_query :str):
    '''
    ### Summary:
    Prompt to answer question about Youtube Videos.

    ### Parameters:
    video_content - Pieces of text to base Assistant answer.
    user_query - User question about the video content
    '''
    
    return f"""You are a helpful and honest assistant and you should answer only based on the text below:

    {video_content}

    Question:
    {user_query}

    Answer:"""



def summarization_prompt(*chunks):
    '''
    ### Summary
    Prompt to summarize content about Youtube Video

    ### Parameters
    Chunks: Pieces of text
    '''

    prompt_resumo = f"""Always base yourself on the text provided below, do not invent any information.
Write a summary of up to 1000 characters of the following paragraphs:\n\n"""

    for chunk in chunks:
        prompt_resumo+=f"{chunk}\n"

    prompt_resumo+="Summary:"

    return prompt_resumo