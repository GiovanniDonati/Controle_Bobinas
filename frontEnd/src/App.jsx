import { useState } from "react";
import Aside from "./components/Aside";
import ControlPanel from "./pages/ControlPanelPage";

function App() {
  const [tabOpen, setTabOpen] = useState("");

  return (
    <div className="flex w-full h-screen">
      <Aside tabOpen={tabOpen} setTabOpen={setTabOpen} />
      <ControlPanel></ControlPanel>
    </div>
  );
}

export default App;
