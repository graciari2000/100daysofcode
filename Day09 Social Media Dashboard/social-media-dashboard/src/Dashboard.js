// src/components/Dashboard.js

import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Dashboard = () => {
    const [posts, setPosts] = useState([]);

    useEffect(() => {
        // Fetch social media posts data from an API using Axios
        axios.get('https://api.example.com/posts')
            .then((response) => {
                setPosts(response.data);
            })
            .catch((error) => {
                console.error('Error fetching posts:', error);
            });
    }, []);

    return (
        <div>
            <h2>Dashboard</h2>
            <div>
                {posts.map((post) => (
                    <div key={post.id} className="post">
                        <h3>{post.title}</h3>
                        <p>{post.body}</p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Dashboard;

