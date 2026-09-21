import { useState } from 'react'

import Navbar from './components/Navbar'
import Hero from './components/Hero'
import Workflow from './components/Workflow'
import Features from './components/Features'
import Footer from './components/Footer'
import Login from './pages/Login'
import Register from './pages/Register'

function App() {
  const [page, setPage] = useState('home')

  const handleLoginSuccess = () => {
    setPage('home')
  }

  if (page === 'login') {
    return (
      <Login
        onRegister={() => setPage('register')}
        onSuccess={handleLoginSuccess}
      />
    )
  }

  if (page === 'register') {
    return (
      <Register
        onLogin={() => setPage('login')}
        onSuccess={() => setPage('login')}
      />
    )
  }

  return (
    <>
      <Navbar
        onLogin={() => setPage('login')}
        onRegister={() => setPage('register')}
      />

      <main>
        <Hero
          onLogin={() => setPage('login')}
          onRegister={() => setPage('register')}
        />

        <Workflow />

        <Features />
      </main>

      <Footer />
    </>
  )
}

export default App