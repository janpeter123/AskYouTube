import { APIResponse } from "./APIResponse";

export default async function SendMessage(url: string, question: string): Promise<APIResponse> {
    const API_URL = process.env.NEXT_PUBLIC_API_URL;
    const complete_api_url = `${API_URL}/ask_video`;

    const requestBody = {
        url: url,
        question: question
    };

    try {
        const response = await fetch(complete_api_url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data: APIResponse = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching data:', error);
        throw error;
    }
}
