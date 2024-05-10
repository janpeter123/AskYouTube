"use client";
import Head from "next/head";
import Image from "next/image";
import { Inter } from "next/font/google";
import styles from "@/styles/Home.module.css";
import YouTubeVideo from "@/ui/video/Video";
import Searchbar from "@/ui/searchbar/Searchbar";
import Summary from "@/ui/summary/Summary";
import Chat from "@/ui/chat/Chat";
import { useState } from "react";
import { Message } from "@/lib/Messages";
import {APIResponse} from "@/lib/APIResponse";

const inter = Inter({ subsets: ["latin"] });

export default function Home() {

  const [messages,setMessages] = useState<Message[]>([]);
  const [summary,setSummary] = useState<APIResponse|null>();
  const [videoURL,setVideoURL] = useState<String|null>(null);
  const [videoId,setVideoId] = useState<String|null>(null);

  // Function to add a new message to the messages array
  const addMessage = (newMessage: Message) => {
    setMessages(prevMessages => [...prevMessages, newMessage]);
  };


  return (
    <>
      <Head>
        <title>YouTube GPT</title>
        <meta name="description" content="YouTube GPT" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
        <link
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
          rel="stylesheet"
          integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
          crossOrigin="anonymous"
        ></link>
        <script
          src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
          integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
          crossOrigin="anonymous"
        ></script>
        <link
          rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css"
        ></link>
      </Head>
      <main className={`${styles.main} ${inter.className}`}>
      <Image src={"/app_logo.png"} width={200} height={200} alt="app logo"></Image>
        <p>Add a Video and Ask me anything!</p>
        <Searchbar setVideoURL={setVideoURL} setVideoId={setVideoId} setSummary={setSummary}/>
        <YouTubeVideo videoId={videoId}/>

        {videoId?<Summary summary={summary}/>:""}
        {videoId?<Chat messages={messages} addMessage={addMessage} videoURL={videoURL}/>:""}
      </main>
    </>
  );
}
