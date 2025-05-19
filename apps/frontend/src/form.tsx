import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"

interface Todo {
  id: number
  description: string
  done: boolean
}

const todos: Todo[] = [
  { id: 1, description: "Item 1", done: false },
  { id: 2, description: "Item 2", done: false },
  { id: 3, description: "Item 3", done: false },
  { id: 4, description: "Item 4", done: true },
]

function TodoItem({ description }: { description: string }) {
  return (
    <li className="my-2">
      <span>{description}</span>
      <Button className="mx-2">Complete</Button>
    </li>
  )
}

export function Form() {
  return (
    <div className="px-120 py-10">
      <div className="flex gap-2">
        <Input type="text" placeholder="Task Ex: Buy Shampoo" />
        <Button>Add</Button>
      </div>
      <div className="flex justify-between mt-4">
        <div>
          <h1>To-do List</h1>
          <ul className="gap-2">
            {todos.map(todo => (
              <TodoItem key={todo.id} description={todo.description} />
            ))}
          </ul>
        </div>
        <div>
          <h1>Completed</h1>
          <ul>
            <TodoItem description="Buy Shampoo" />
          </ul>
        </div>
      </div>
    </div>
  )
}