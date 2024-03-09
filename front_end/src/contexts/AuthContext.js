import React, {createContext, useState, useEffect, useCallback} from 'react';

export const AuthContext = createContext();

export const AuthProvider = ({children}) => {

    const [accessToken, setAccessToken] = useState(
        () => {
            return localStorage.getItem('accessToken');
        });

    const [isAuthenticated, setIsAuthenticated] = useState(
        () => {
            return !!localStorage.getItem('accessToken');
        });

    useEffect(() => {
        if (accessToken) {
            localStorage.setItem('accessToken', accessToken);
        } else {
            localStorage.removeItem('accessToken');
        }
    }, [accessToken]);

    const logout = useCallback(() => {
        setAccessToken(null);
        setIsAuthenticated(false);
    }, []);

    return (
        <AuthContext.Provider value={{
            accessToken, setAccessToken, isAuthenticated,
            setIsAuthenticated, logout
        }}>
            {children}
        </AuthContext.Provider>
    );
};