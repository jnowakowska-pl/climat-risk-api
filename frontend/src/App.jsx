import { useState } from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css'
import AdminPage from './pages/AdminPage/AdminPage';
import LandingPage from './pages/LandingPage/LandingPage';
import DashboardPage from './pages/DashboardPage/DashboardPage';
import PersonalPage from './pages/PersonalPage/PersonalPage';

function App() {
  const [count, setCount] = useState(0)

  return (
    <Router>

      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/admin" element={<AdminPage />} />
        <Route path="/dashboard" element={<DashboardPage />} />
        <Route path="/personal" element={<PersonalPage />} />

      </Routes>

  </Router>

  )
}

export default App
