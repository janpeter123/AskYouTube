export default function getYoutubeVideoId(url: string): string | null {
    // Regular expression to match YouTube video IDs
    const youtubeRegex = /(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})/;
  
    // Match the video ID using the regular expression
    const match = String(url).match(youtubeRegex);
  
    // If there's a match, return the video ID, otherwise return null
    return match ? match[1] : null;
  }
  
  // Example usage
  const youtubeUrl = "https://www.youtube.com/watch?v=TiX8li69Hh8";
  const videoId = getYoutubeVideoId(youtubeUrl);
  console.log("YouTube Video ID:", videoId);