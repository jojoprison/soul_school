import React from 'react';
import {
    BrowserRouter as Router, Routes, Route, Navigate
} from 'react-router-dom';
import {AuthProvider} from './contexts/AuthContext';
import Login from './components/Login';
import Lessons from './components/Lessons';
import ProtectedRoute from './components/ProtectedRoute';

const App = () => {
    return (
        <AuthProvider>
            <Router>
                <Routes>
                    <Route path="/login" element={<Login/>}/>
                    <Route
                        path="/lessons"
                        element={
                            <ProtectedRoute>
                                <Lessons/>
                            </ProtectedRoute>
                        }
                    />
                    <Route path="*" element={<Navigate to="/login" replace/>}/>
                </Routes>
            </Router>
        </AuthProvider>
    );
};

export default App;
