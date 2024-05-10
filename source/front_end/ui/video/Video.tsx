import getYoutubeVideoId from '@/lib/Youtube';
import styles from './video.module.css';

export default function YouTubeVideo(props :any){

    return <div className={styles.video}>{props.videoId? <iframe
        width="100%"
        height="100%"
        src={`https://www.youtube.com/embed/${props.videoId}`}
      ></iframe>:""

    }</div>

}