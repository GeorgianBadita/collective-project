import React from 'react'
import { Link } from 'react-router-dom'
import Helmet from 'react-helmet'
import styles from './home.module.css'

const Home = (props) => {
  return (
    <div className={styles.page}>
      <Helmet>
        <title>proiect-colectiv</title>
      </Helmet>
      <div className={styles.container}>
        <div className={styles.container1}>
          <div className={styles.container2}>
            <Link to="/" className={styles.navlink}>
              Home
            </Link>
            <Link to="/" className={styles.navlink1}>
              People who need blood
            </Link>
            <Link to="/" className={styles.navlink2}>
              How to donate
            </Link>
          </div>
          <div className={styles.container3}>
            <button className={styles.button} onClick={(e)=>{ window.location.href='/signup'}}>Donate</button>
            <h1 className={styles.heading1} onClick={(e)=>{ window.location.href='/login'}}>Sign in</h1>
          </div>
        </div>
        <div className={styles.container4}>
          <h2 className={styles.heading2}>Why donate?</h2>
          <p className={styles.textblock}>
            One in ten patients in Romanian hospitals needs blood. Statistically, every person on
            the planet needs blood at least once throughout their lives. It's everyone's
            responsibility to make sure there is enough blood in Romanian hospitals.
          </p>
          <button className={styles.button1} onClick={(e)=>{ window.location.href='/signup'}}>Donate</button>
        </div>
      </div>
    </div>
  )
}

export default Home
