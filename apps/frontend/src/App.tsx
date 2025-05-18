import axios from 'axios'
import { useEffect, useState } from 'react'

function App() {
  const [message, setMessage] = useState('')
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('/api/health')
        setMessage(response.data.status)
      } catch (error) {
        setMessage('Error connecting to backend')
      } finally {
        setLoading(false)
      }
    }

    fetchData()
  }, [])

  return (
    <div className="bg-amber-300">
      <h1>Frontend App</h1>
      <div className="card">
        <p>
          {loading ? 'Loading...' : `Backend status: ${message}`}
        </p>
      </div>
    </div>
  )
}

export default App 