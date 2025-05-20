import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { useEffect, useState } from "react"

interface Todo {
  id: number
  description: string
  done: boolean
}

async function fetchTodos(): Promise<Todo[]> {
  const todoList = await fetch("http://localhost:8000/api/todos").then(response => response.json())
  return todoList
}

async function createTodo(description: string): Promise<void> {
  return fetch("http://localhost:8000/api/todos", {
    method: "POST", body: JSON.stringify({ description }), headers: {
      "Content-Type": "application/json"
    }
  }).then(response => console.log(response))
}


async function updateTodo(todoId: number, body: Todo): Promise<void> {
  return fetch(`http://localhost:8000/api/todos/${todoId}`, {
    method: "PUT", body: JSON.stringify(body), headers: {
      "Content-Type": "application/json"
    }
  }).then(response => console.log(response))
}

function TodoItem({ todo, onUpdate }: { todo: Todo, onUpdate: () => Promise<void> }) {
  const handleUpdateTodo = (todoId: number) => {
    updateTodo(todoId, {
      ...todo,
      done: true
    }).then(() => onUpdate())
  }

  return (
    <li className="my-2">
      <span>{todo.description}</span>
      <Button className="mx-2" onClick={() => handleUpdateTodo(todo.id)}>Complete</Button>
    </li>
  )
}

export function Form() {
  const [todos, setTodos] = useState<Todo[]>([])
  const [inputValue, setInputValue] = useState("")

  function refreshTodos(): Promise<void> {
    return fetchTodos().then(response => setTodos(response))
  }

  useEffect(() => {
    refreshTodos()
  }, [])

  const handleCreateTodo = async () => {
    await createTodo(inputValue)
    await refreshTodos()
    setInputValue("")
  }

  const todoList = todos.filter(todos => !todos.done)
  const doneList = todos.filter(todos => todos.done)

  return (
    <div className="px-120 py-10">
      <div className="flex gap-2">
        <Input type="text" placeholder="Task Ex: Buy Shampoo" value={inputValue} onChange={(e) => setInputValue(e.target.value)} />
        <Button onClick={handleCreateTodo}>Add</Button>
      </div>
      <div className="flex justify-between mt-4">
        <div>
          <h1>To-do List</h1>
          <ul className="gap-2">
            {todoList.map(todo => (
              <TodoItem key={todo.id} todo={todo} onUpdate={refreshTodos} />
            ))}
          </ul>
        </div>
        <div>
          <h1>Completed</h1>
          <ul>
            {doneList.map(todo => (
              <TodoItem todo={todo} onUpdate={refreshTodos} />
            ))}
          </ul>
        </div>
      </div>
    </div>
  )
}