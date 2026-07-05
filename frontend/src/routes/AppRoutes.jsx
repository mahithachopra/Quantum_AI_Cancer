import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";

import DashboardLayout from "../layouts/DashboardLayout";

import Dashboard from "../pages/Dashboard";
import MutationAnalysis from "../pages/MutationAnalysis";
import Recommendations from "../pages/Recommendations";
import ClinicalTrials from "../pages/ClinicalTrials";
import Literature from "../pages/Literature";
import Reports from "../pages/Reports";
import Explainability from "../pages/Explainability";
import Settings from "../pages/Settings";

export default function AppRoutes() {
  return (
    <BrowserRouter>
      <DashboardLayout>
        <Routes>

          <Route
            path="/"
            element={<Dashboard />}
          />

          <Route
            path="/mutation"
            element={<MutationAnalysis />}
          />

          <Route
            path="/recommendations"
            element={<Recommendations />}
          />

          <Route
            path="/trials"
            element={<ClinicalTrials />}
          />

          <Route
            path="/literature"
            element={<Literature />}
          />

          <Route
            path="/reports"
            element={<Reports />}
          />
            <Route
            path="/explainability"
            element={<Explainability />}
            />
          <Route
            path="/settings"
            element={<Settings />}
          />

        </Routes>
      </DashboardLayout>
    </BrowserRouter>
  );
}