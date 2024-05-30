import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [users, setUsers] = useState([])

  useEffect(() => {
    fetchUsers()
  }, [])
  
  const fetchUsers = async () => {
    const response = await fetch("http://127.0.0.1:5000/users")
    const data = await response.json()
    setUsers(data.users)
    console.log(data.users) 
  }

  return <div>
  <h2>Forrest users</h2>
  <table>
      <thead>
          <tr>
              <th>Fullname</th>
              <th>Contact number</th>
              <th>User type</th>
              <th>Actions</th>
          </tr>
      </thead>
      <tbody>
          {users.map((user) => (
              <tr key={user.id}>
                  <td>{user.fullName}</td>
                  <td>{user.contactNumber}</td>
                  <td>{user.userType}</td>
                  <td>
                      <button>Update</button>
                      <button>Delete</button>
                  </td>
              </tr>
          ))}
      </tbody>
  </table>
</div>
}

export default App
