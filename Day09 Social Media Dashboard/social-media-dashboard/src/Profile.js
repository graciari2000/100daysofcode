// src/components/Profile.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Profile = () => {
    const [userData, setUserData] = useState({});

    useEffect(() => {
        // Fetch user profile data from an API using Axios
        axios.get('https://api.example.com/user')
            .then((response) => {
                setUserData(response.data);
            })
            .catch((error) => {
                console.error('Error fetching user data:', error);
            });
    }, []);

    return (
        <div>
            <h2>Profile</h2>
            <div className="user-profile">
                <img src={userData.profileImage} alt="Profile" />
                <h3>{userData.username}</h3>
                <p>{userData.bio}</p>
            </div>
        </div>
    );
};

export default Profile;

