import React, { useContext } from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import { AuthContext } from '../contexts/AuthContext';

const ProtectedRoute = ({ redirectPath = '/login', children }) => {
  const { isAuthenticated, isLoading } = useContext(AuthContext);

  if (isLoading) {
    // You can add a loading spinner or message here while checking authentication
    return <div>Loading...</div>;
  }

  if (!isAuthenticated) {
    // If the user is not authenticated, redirect to the specified redirectPath
    return <Navigate to={redirectPath} replace />;
  }

  // If the user is authenticated, render the nested route or the children prop
  return children ? children : <Outlet />;
};

export default ProtectedRoute;
