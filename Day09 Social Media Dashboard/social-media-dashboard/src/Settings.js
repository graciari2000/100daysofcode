// src/components/Settings.js

import React, { useState } from 'react';

const Settings = () => {
    const [theme, setTheme] = useState('light');

    const toggleTheme = () => {
        const newTheme = theme === 'light' ? 'dark' : 'light';
        setTheme(newTheme);
        // Implement logic to update the theme in your application
    };

    return (
        <div>
            <h2>Settings</h2>
            <div className="theme-settings">
                <p>Theme: {theme}</p>
                <button onClick={toggleTheme}>Toggle Theme</button>
            </div>
        </div>
    );
};

export default Settings;

