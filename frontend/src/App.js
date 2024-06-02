import { BrowserRouter, Routes, Route } from "react-router-dom";
import React from "react";
import Login from "./screens/Login";
import Home from "./screens/Home";
import Signup from "./screens/Signup";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
