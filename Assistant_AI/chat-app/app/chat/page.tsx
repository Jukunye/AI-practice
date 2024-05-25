"use client";
import React, { useState } from "react";
import axios from "axios";
import Markdown from "react-markdown";
import remarkGfm from "remark-gfm";

interface Output {
  answer: string;
}

export default function MyComponent() {
  const [input, setInput] = useState<string>("");
  const [quiz, setQuiz] = useState<string>("");
  const [loading, setLoading] = useState<Boolean>(false);
  const [output, setOutput] = useState<Output | null>(null);

  const handleChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
    setInput(event.target.value);
  };

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setLoading(true);
    setOutput(null);
    setQuiz(input);
    axios
      .get(`http://127.0.0.1:8000/chat/`, {
        params: {
          prompt: input,
        },
      })
      .then((response) => {
        setOutput(response.data);
        console.log(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error:", error);
        setLoading(false);
      });
  };

  interface output {
    answer: string;
  }

  return (
    <>
      {/* <div className="fixed top-4">
        <button
          type="submit"
          className="flex items-center gap-2 bg-emerald-400 text-white m-2 rounded-md px-2 py-1"
        >
          {" "}
          New chat
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            strokeWidth={1.5}
            stroke="currentColor"
            className="w-6 h-6"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              d="M12 9v6m3-3H9m12 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"
            />
          </svg>
        </button>
      </div> */}
      <div className="flex flex-col p-10 max-w-screen-md mx-auto mb-40">
        <div className="mt-4 p-4 rounded-lg">
          <p className="mb-3 text-sm text-emerald-800">{quiz}</p>
          {output ? (
            <div className="p-3 border border-emerald-500 rounded-lg text-gray-800">
              <Markdown remarkPlugins={[remarkGfm]}>{output.answer}</Markdown>
            </div>
          ) : (
            <></>
          )}
          {loading && <p className="text-emerald-600">Loading...</p>}
        </div>
        <div className="fixed bottom-0 bg-white w-full">
          <form
            onSubmit={handleSubmit}
            className="flex items-end mb-8 border rounded-lg w-[670px] bg-slate-50"
          >
            <textarea
              value={input}
              onChange={handleChange}
              className="text-sm px-4 py-2 h-20 w-[600px] outline-none bg-slate-50"
            />
            <div className="">
              <button
                type="submit"
                className=". bg-emerald-500 text-white m-2 font-semibold rounded-md px-4 py-2"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  strokeWidth={1.5}
                  stroke="currentColor"
                  className="w-6 h-6"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    d="M6 12 3.269 3.125A59.769 59.769 0 0 1 21.485 12 59.768 59.768 0 0 1 3.27 20.875L5.999 12Zm0 0h7.5"
                  />
                </svg>
              </button>
            </div>
          </form>
        </div>
      </div>
    </>
  );
}
