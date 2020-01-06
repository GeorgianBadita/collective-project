import React from 'react'
import Helmet from 'react-helmet'

import styles from './profile.module.css'

const Profile = (props) => {
  return (
    <div className={styles.profile}>
      <Helmet>
        <title>proiect-colectiv</title>
      </Helmet>
      <span>Soon</span>
    </div>
  )
}

export default Profile
