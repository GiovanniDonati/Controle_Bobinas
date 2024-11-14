import Table from "../components/Table/Table";
import Title from "../components/Title";

function ControlPanelPage() {
  return (
    <div className="flex flex-col flex-grow w-full p-2 overflow-hidden bg-white rounded-lg shadow-lg gap-y-4">
      <Title>Control Panel</Title>
      <Table />
    </div>
  );
}

export default ControlPanelPage;
