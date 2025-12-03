import { useState } from "react";
import client from "../api/client";

export default function JobForm({ onJobCreated }) {
  const [value, setValue] = useState("");

  async function submitJob(e) {
    e.preventDefault();

    const response = await client.post("/jobs", { value: Number(value) });
    onJobCreated(response.data);
    setValue("");
  }

  return (
    <form onSubmit={submitJob} style={{ marginBottom: "20px" }}>
      <h2>Create Job</h2>

      <input
        type="number"
        placeholder="Enter a number"
        value={value}
        onChange={(e) => setValue(e.target.value)}
        required
      />

      <button type="submit">Submit Job</button>
    </form>
  );
}
