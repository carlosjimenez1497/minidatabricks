import { useEffect, useState } from "react";
import client from "../api/client";

export default function JobList({ refreshTrigger }) {
  const [jobs, setJobs] = useState([]);

  async function fetchJobs() {
    const response = await client.get("/jobs");
    setJobs(response.data);
  }

  useEffect(() => {
    fetchJobs();
  }, [refreshTrigger]);

  return (
    <div>
      <h2>Jobs</h2>
      <ul>
        {jobs.map((job) => (
          <li key={job.id}>
            <strong>ID:</strong> {job.id} — 
            <strong>Status:</strong> {job.status} —
            <strong>Result:</strong>{" "}
            {job.result ? JSON.stringify(job.result) : "pending"}
          </li>
        ))}
      </ul>
    </div>
  );
}
