import axios from 'axios'

const api = axios.create({
  baseURL: 'https://todo-app-tthp.onrender.com',
})

export const getTodos = () => api.get('/todos')
export const createTodo = (title) => api.post('/todos', { title })
export const deleteTodo = (id) => api.delete(`/todos/${id}`)