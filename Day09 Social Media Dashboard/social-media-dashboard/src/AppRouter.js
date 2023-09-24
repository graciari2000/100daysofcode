// src/AppRouter.js

import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

// Import your dashboard components here
import Dashboard from './components/Dashboard';
import Profile from './components/Profile';
import Settings from './components/Settings';

const AppRouter = () => {
    return (
        <Router>
            <Switch>
                <Route exact path="/" component={Dashboard} />
                <Route path="/profile" component={Profile} />
                <Route path="/settings" component={Settings} />
            </Switch>
        </Router>
    );
};

export default AppRouter;
