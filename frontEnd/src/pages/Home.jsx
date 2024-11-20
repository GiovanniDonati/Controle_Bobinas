import { useState } from "react";
import Aside from "../components/Aside";
import ControlPanelPage from "./ControlPanelPage";
import ProductionPage from "./ProductionPage";
import RetailPage from "./RetailPage";
import HistoricPage from "./HistoricPage";
import VisualPage from "./VisualPage";

function Home() {
  const [tabOpen, setTabOpen] = useState("dashboard");
  const [menuVisibility, setMenuVisibily] = useState(false);
  return (
    <div className="flex w-full h-screen">
      <Aside
        tabOpen={tabOpen}
        setTabOpen={setTabOpen}
        menuVisibility={menuVisibility}
        setMenuVisibily={setMenuVisibily}
      />

      {tabOpen === "dashboard" ? (
        <ControlPanelPage />
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

export default Home;
