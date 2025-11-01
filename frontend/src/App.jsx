import React from "react";
import SentimentForm from "./components/SentimentForm";

function App() {
  return (
    <div
      className="min-vh-100 w-100 d-flex flex-column justify-content-center align-items-center text-light"
      style={{
        background: "linear-gradient(135deg, #0f0c29, #302b63, #24243e)",
        overflowX: "hidden",
        backgroundSize: "400% 400%",
        animation: "gradientFlow 12s ease infinite",
      }}
    >
      <style>
        {`
          @keyframes gradientFlow {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
          }
        `}
      </style>

      <div className="text-center mb-4">
        <h1 className="fw-bold display-5 mb-2 text-glow">
          🎬 Movie Review Sentiment Analyzer
        </h1>
        <p className="text-light opacity-75 fs-5">
          Instantly detect the mood of your reviews
        </p>
      </div>

      <SentimentForm />
    </div>
  );
}

export default App;
