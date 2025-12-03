import { useState } from "react";
import JobForm from "./components/JobForm";
import JobList from "./components/JobList";

export default function App() {
  const [refreshKey, setRefreshKey] = useState(0);

  function refreshJobs() {
    setRefreshKey((prev) => prev + 1);
  }

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>Mini Databricks Frontend</h1>

      <JobForm onJobCreated={refreshJobs} />
      <JobList refreshTrigger={refreshKey} />
    </div>
  );
}
