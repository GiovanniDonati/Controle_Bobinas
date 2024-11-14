import { useState } from "react";
import Aside from "./components/Aside";
import ControlPanelPage from "./pages/ControlPanelPage";
import SearchPage from "./pages/SearchPage";
import ProductionPage from "./pages/ProductionPage";
import RetailPage from "./pages/RetailPage";
import HistoricPage from "./pages/HistoricPage";
import VisualPage from "./pages/VisualPage";

function App() {
  const [tabOpen, setTabOpen] = useState("");

  return (
    <div className="flex w-full h-screen">
      <Aside tabOpen={tabOpen} setTabOpen={setTabOpen} />
      {tabOpen === "dashboard" ? (
        <ControlPanelPage />
      ) : tabOpen === "search" ? (
        <SearchPage />
      ) : tabOpen === "production" ? (
        <ProductionPage />
      ) : tabOpen === "retalhos" ? (
        <RetailPage />
      ) : tabOpen === "history" ? (
        <HistoricPage />
      ) : (
        tabOpen === "visual" && <VisualPage />
      )}
    </div>
  );
}

export default App;
