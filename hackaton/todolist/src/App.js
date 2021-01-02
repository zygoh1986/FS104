import React, { useState } from "react";
import './App.css';
import Form from "./form"
import TodoList from "./TodoList"

function App() {
  const [inputText, setInputText] = useState("");
  const [todos, setTodos] = useState([]);
  return (
    <div className="App">
      <h1> Put in your daily task! </h1>
      <Form inputText={inputText} todos={todos} setTodos={setTodos} setInputText={setInputText}/>
      <TodoList todos={todos}/>
      <TodoList setTodos={setTodos} todos={todos} />
    </div>
  );
}

export default App;
