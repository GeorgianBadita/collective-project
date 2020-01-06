import React from 'react'
import { Link } from 'react-router-dom'
import Helmet from 'react-helmet'

import styles from './login.module.css'

const Login = (props) => {
  return (
    <div className={styles.page1}>
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
            <Link to="/" className={styles.navlink1}>
              Mission
            </Link>
            <Link to="/" className={styles.navlink2}>
              Support
            </Link>
            <Link to="/" className={styles.navlink3}>
              Join
            </Link>
          </div>
        </div>
        <div className={styles.container4}>
          <div className={styles.container5}>
            <h2 className={styles.heading2}>Username</h2>
            <input type="text" required="true" placeholder="user" className={styles.textinput} />
            <h2 className={styles.heading21}>Password</h2>
            <input
              type="text"
              required="true"
              placeholder="password"
              className={styles.textinput1}
            />
            <button className={styles.button}>Login</button>
            <span className={styles.text}>Don't have an account? Sign up.</span>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Login
