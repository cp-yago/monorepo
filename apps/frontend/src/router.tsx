import { BrowserRouter, Route, Routes } from 'react-router'
import { Form } from './form'
import { Home } from './home'

export function Router() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/form" element={<Form />} />
      </Routes>
    </BrowserRouter>
  )
}