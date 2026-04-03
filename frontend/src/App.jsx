import { BrowserRouter, Routes, Route, Link } from "react-router-dom"

import Clients from "./pages/Clients"
import Dashboard from "./pages/Dashboard"
import Vehicles from "./pages/Vehicles"

function App() {
  return (
    <BrowserRouter>
      <div>
        <nav className="bg-white shadow px-6 py-4">
          <Link to="/">Dashboard</Link>
          <Link to="/clients">Clients</Link>
          <Link to="/vehicles">Vehicles</Link>
        </nav>
        <div className="bg-gray-100 min-h-screen p-6">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/clients" element={<Clients />} />
            <Route path="/vehicles" element={<Vehicles />} />
          </Routes>
        </div>
      </div>
    </BrowserRouter>
  )
}

export default App
