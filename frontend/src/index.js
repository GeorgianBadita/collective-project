import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter as Router, Route } from 'react-router-dom'

import Home from './views/home'
import Login from './views/login'
import Signup from './views/signup'
import FAQ from './views/f-a-q'
import Profile from './views/profile'

const App = () => {
  return (
    <Router>
      <div>
        <Route exact component={Home} path="/" />
        <Route exact component={Login} path="/login" />
        <Route exact component={Signup} path="/signup" />
        <Route exact component={FAQ} path="/f-a-q" />
        <Route exact component={Profile} path="/profile" />
      </div>
    </Router>
  )
}

ReactDOM.render(<App />, document.getElementById('app'))
