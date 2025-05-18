import { BrowserRouter, Route, Routes } from 'react-router'
import { About } from './about'
import { Home } from './home'

export function Router() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </BrowserRouter>
  )
}