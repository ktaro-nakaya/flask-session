import "./App.css";
import React, { useState } from "react";

function App() {
  const [currentNum, setCurrentNum] = useState(0);
  const [sessionKey, setSessionkey] = useState("");
  function countUp(e) {
    fetch("/api/count/")
      .then((response) => {
        if (!response.ok) {
          console.error("エラーレスポンス", response);
          return;
        }
        response.json().then((json) => {
          setCurrentNum(json.number);
        });
      })
      .catch((e) => {
        console.error("通信に失敗しました", e);
      });
  }
  return (
    <div className="App">
      <h1>{currentNum}</h1>
      <br />
      <button onClick={() => countUp()}>カウントアップ</button>
    </div>
  );
}

export default App;
