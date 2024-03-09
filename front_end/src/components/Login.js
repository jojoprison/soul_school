import React, {useState, useContext} from 'react';
import axios from 'axios';
import {useNavigate} from 'react-router-dom';
import {AuthContext} from '../contexts/AuthContext';
import '../styles.css';

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const {setIsAuthenticated, setAccessToken} = useContext(AuthContext);
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post(
                'http://127.0.0.1/api/v1/auth/jwt/create/',
                {username, password}
            );
            const {access} = response.data;
            localStorage.setItem('accessToken', access);
            setAccessToken(access); // Update the access token in the context
            setIsAuthenticated(true);
            navigate('/lessons'); // Redirect to the lessons page
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div className="centeredContainer">
            <h1 className="bigHeading">Войти</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    placeholder="Имя пользователя"
                    required
                    className="bigInput"
                />
                <input
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="Пароль"
                    required
                    className="bigInput"
                />
                <button type="submit" className="bigButton">
                    Войти
                </button>
            </form>
        </div>
    );
};

export default Login;
