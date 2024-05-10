import styles from './summary.module.css';

export default function Summary(props){
   return <div className={styles.summary}>
    <h4>Summary</h4>
    {
        props.summary?<p>{props.summary.generated_text}</p>: <p class="card-text placeholder-glow">
        <span class="placeholder col-7"></span>
        <span class="placeholder col-6"></span>
        <span class="placeholder col-7"></span>
        <span class="placeholder col-6"></span>
        <span class="placeholder col-3"></span>
      </p>
    }
  </div>
}