import { createContext, useContext, useState } from "react";

const PipelineContext = createContext(null);

export function PipelineProvider({ children }) {
  const [pipeline, setPipeline] = useState(null);

  return (
    <PipelineContext.Provider
      value={{
        pipeline,
        setPipeline,
      }}
    >
      {children}
    </PipelineContext.Provider>
  );
}

export function usePipeline() {
  return useContext(PipelineContext);
}