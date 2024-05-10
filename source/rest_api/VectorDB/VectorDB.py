import chromadb
import uuid

print("Initializing VectorDB ...")
chroma_client = chromadb.Client()

def setup_collection(name :str,documents :list[str]):
    '''
    ### Summary
    Function to create db collections and store video chunks in database

    ### Parameters
    name - collection name, video id.
    documents - video chunks

    ### Returns
    Collection id
    '''

    collection = chroma_client.create_collection(name=name) #Creates Collection ID
    video_ids = [str(uuid.uuid4()) for i in range(len(documents))]  #Generates random IDs to all video chunks
    collection.add(documents=documents,ids=video_ids)   #Add to collection video chunks and video ids.
    return collection   #return collection_id


def query_database(query :str,collection_name :str,n_results=3)->list[str]:
    '''
    ### Summary
    Query Database with natural language

    ### Parameters
    collection_name - string, Youtube Video Id
    n_results - Number of database results to use

    ### Returns
    List of chunks
    '''

    collection = chroma_client.get_collection(collection_name)
    return collection.query(query_texts=[query],n_results=n_results)['documents']