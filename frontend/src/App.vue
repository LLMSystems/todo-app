<script setup>
import { ref, onMounted } from 'vue'
import { getTodos, createTodo, deleteTodo } from './api/todos'

const todos = ref([])
const newTitle = ref('')

// 頁面載入時取得清單
onMounted(async () => {
  const res = await getTodos()
  todos.value = res.data
})

// 新增
async function addTodo() {
  if (!newTitle.value) return
  const res = await createTodo(newTitle.value)
  todos.value.push(res.data)
  newTitle.value = ''
}

// 刪除
async function removeTodo(id) {
  await deleteTodo(id)
  todos.value = todos.value.filter((t) => t.id !== id)
}
</script>

<template>
  <div>
    <h1>待辦清單</h1>

    <input v-model="newTitle" placeholder="新增待辦事項" />
    <button @click="addTodo">新增</button>

    <ul>
      <li v-for="todo in todos" :key="todo.id">
        {{ todo.title }}
        <button @click="removeTodo(todo.id)">刪除</button>
      </li>
    </ul>
  </div>
</template>