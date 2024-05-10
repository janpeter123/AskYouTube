import { APIResponse } from "./APIResponse";

export default async function GetSummary(url :string) {

  // :Promise<APIResponse>
    const API_URL = process.env.NEXT_PUBLIC_API_URL;

    const complete_api_url = `${API_URL}/video_summary?url=${encodeURIComponent(url)}`;

    try {
      console.log(complete_api_url);
      const response = await fetch(complete_api_url);
  
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
  
      const data :APIResponse = await response.json();
      return data;
    } catch (error) {
      console.error('Error fetching data:', error);
      throw error;
    }
    
}