import { useState } from "react";
import { PlusCircleIcon, SearchIcon } from "lucide-react";
import Table from "../components/Table/DashboardTable";
import Title from "../components/Title";
import SearchModal from "../components/Modal/SearchModal";
import AddModal from "../components/Modal/AddModal";

function ControlPanelPage() {
  const [modalSearch, setModalSearch] = useState(false);
  const [modalAdd, setModalAdd] = useState(false);

  // Função para abrir e fechar os modais
  const toggleModalSearch = () => {
    setModalSearch(!modalSearch);
  };

  const toggleModalAdd = () => {
    setModalAdd(!modalAdd);
  };

  const buttonTop =
    "fixed flex gap-2 px-3 py-2 font-bold text-white rounded-md";

  return (
    <div className="flex flex-col flex-grow p-4 overflow-x-hidden bg-gray-200">
      <div className="flex items-center">
        <Title>Painel de Controle</Title>
        <button
          className={`${buttonTop} right-40 bg-blue-500 hover:bg-blue-600`}
          onClick={toggleModalSearch}
        >
          <SearchIcon />
          Pesquisar
        </button>
        <button
          className={`${buttonTop} right-5 bg-green-500 hover:bg-green-600`}
          onClick={toggleModalAdd}
        >
          <PlusCircleIcon />
          Adicionar
        </button>
      </div>
      <Table />
      {modalSearch && <SearchModal toggleModalSearch={toggleModalSearch} />}
      {modalAdd && <AddModal toggleModalAdd={toggleModalAdd} />}
    </div>
  );
}

export default ControlPanelPage;
