import React, {useState, useEffect, useContext} from 'react';
import axios from 'axios';
import {AuthContext} from '../contexts/AuthContext';
import '../styles.css';

const Lessons = () => {
    const [lessons, setLessons] = useState([]);
    const {accessToken, logout} = useContext(AuthContext);

    const handleLogout = () => {
        logout();
    };

    useEffect(() => {
        const fetchLessons = async () => {
            try {
                const response = await axios.get(
                    'http://127.0.0.1/api/v1/lessons/',
                    {
                        headers: {Authorization: `JWT ${accessToken}`},
                    });
                setLessons(response.data);
            } catch (error) {
                console.error(error);
            }
        };

        if (accessToken) {
            fetchLessons();
        }
    }, [accessToken]);

    return (
        <div className="centeredContainer">
            <h1 className="bigHeading">Уроки Soul School</h1>
            <button className="bigButton" onClick={handleLogout}>Выйти</button>
            <ul>
                {lessons.map((lesson) => (
                    <li key={lesson.id}>{lesson.title}</li>
                ))}
            </ul>
        </div>
    );
};

export default Lessons;
