import getYoutubeVideoId from '@/lib/Youtube';
import styles from './searchbar.module.css';
import GetSummary from '@/lib/GetSummary';

export default function Searchbar(props) {

  return (
    <div className={styles.searchbar}>
      <div className="input-group mb-3">
        <input
          type="text"
          className="form-control"
          placeholder={`https://www.youtube.com/watch?v=TiX8li69Hh8`}
          aria-label="Recipient's username"
          aria-describedby="button-addon2"
          id="videoURL"

          onChange={async (e)=>{
            let videoId = getYoutubeVideoId(e.target.value);
            const videoURL = e.target.value;
            if(videoId){
              props.setVideoId(videoId);
              props.setVideoURL(e.target.value);

            }
            const response = await GetSummary(videoURL);
            console.log(await response);
            props.setSummary(response);
            
          }}
        />
        <button
          className="btn btn-outline-secondary"
          type="button"
          id="button-addon2"

          onClick={(e)=>{
            e.preventDefault();
            let videoURL = document.getElementById("videoURL").value;
            let videoId = getYoutubeVideoId(videoURL);
            if(videoId)
            props.setVideoId(videoId);
          }}
        >
          <i className="bi bi-search"></i>
        </button>
      </div>
    </div>
  );
}
