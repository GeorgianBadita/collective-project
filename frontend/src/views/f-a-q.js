import React from 'react'
import { Link } from 'react-router-dom'
import Helmet from 'react-helmet'

import styles from './f-a-q.module.css'

const FAQ = (props) => {
  return (
    <div className={styles.faq}>
      <Helmet>
        <title>proiect-colectiv</title>
      </Helmet>
      <div className={styles.container}>
        <div className={styles.container1}>
          <div className={styles.container2}>
            <svg viewBox="0 0 1024 1024" height="20" width="20" fill="#A51D18">
              <path d="M864.626 473.162c-65.754-183.44-205.11-348.15-352.626-473.162-147.516 125.012-286.87 289.722-352.626 473.162-40.664 113.436-44.682 236.562 12.584 345.4 65.846 125.14 198.632 205.438 340.042 205.438s274.196-80.298 340.040-205.44c57.27-108.838 53.25-231.962 12.586-345.398zM738.764 758.956c-43.802 83.252-132.812 137.044-226.764 137.044-55.12 0-108.524-18.536-152.112-50.652 13.242 1.724 26.632 2.652 40.112 2.652 117.426 0 228.668-67.214 283.402-171.242 44.878-85.292 40.978-173.848 23.882-244.338 14.558 28.15 26.906 56.198 36.848 83.932 22.606 63.062 40.024 156.34-5.368 242.604z"></path>
            </svg>
            <h1 className={styles.heading1}>Donate Blood</h1>
          </div>
          <div className={styles.container3}>
            <Link to="/" className={styles.navlink}>
              Home
            </Link>
            <Link to="/sign-up" className={styles.navlink1}>
              Donate
            </Link>
            <Link to="/" className={styles.navlink2}>
              How to donate
            </Link>
          </div>
        </div>
        <div className={styles.container4}>
          <h2 className={styles.heading2}>How to donate?</h2>
          <h2 className={styles.heading21}>Before donating</h2>
          <h2 className={styles.heading22}>Who can donate?</h2>
          <div className={styles.container5}>
            <span className={styles.text}>
              1. Eat something before you come to donate, but not anything too fatty.
            </span>
            <span className={styles.text1}>
              2. Do not consume any alcohol for 24h before donating.
            </span>
            <span className={styles.text2}>3. Do not smoke before and after donating.</span>
            <span className={styles.text3}> 4. Come rested.</span>
          </div>
          <p className={styles.textblock}>
            – vârsta cuprinsă între 18-60 ani; – greutate peste 50 Kg; – puls regulat, 60 -100
            bătăi/ minut; – tensiune arterială sistolică între 100 și 180 mmHg; – să nu fi suferit
            în ultimele 6 luni intervenții chirurgicale; – femeile să nu fie: însarcinate, în
            perioada de lăuzie, în perioada menstruală; – să nu fi consumat grăsimi sau băuturi
            alcoolice cu cel puțin 48 de ore înaintea donării; – să nu fii sub tratament pentru
            diferite afecțiuni: hipertensiune, boli de inimă, boli renale, boli psihice, boli
            hepatice, boli endocrine;
          </p>
          <button className={styles.button}>Donate</button>
        </div>
      </div>
    </div>
  )
}

export default FAQ
