import { useState } from "react";
import { PlusCircleIcon, SearchIcon } from "lucide-react";
import Table from "../components/Table/Table";
import Title from "../components/Title";
import SearchModal from "../components/SearchModal";

function ControlPanelPage() {
  const [modalSearch, setModalSearch] = useState(false);

  // Função para abrir e fechar o modal
  const toggleModal = () => {
    setModalSearch(!modalSearch);
  };

  const buttonTop =
    "fixed flex gap-2 px-3 py-2 font-bold text-white rounded-md";

  return (
    <div className="flex flex-col flex-grow p-4 overflow-x-hidden bg-gray-200">
      <div className="flex items-center">
        <Title>Painel de Controle</Title>
        <button
          className={`${buttonTop} right-40 bg-blue-500 hover:bg-blue-600`}
          onClick={toggleModal}
        >
          <SearchIcon />
          Pesquisar
        </button>
        <button
          className={`${buttonTop} right-5 bg-green-500 hover:bg-green-600`}
        >
          <PlusCircleIcon />
          Adicionar
        </button>
      </div>
      <Table />
      {modalSearch && <SearchModal toggleModal={toggleModal} />}
    </div>
  );
}

export default ControlPanelPage;
