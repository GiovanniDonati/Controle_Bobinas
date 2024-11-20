import { useState } from "react";
import { PlusCircleIcon, SearchIcon } from "lucide-react";
import Table from "../components/Table/Table";
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

  const testeJson = {
    Endereço: "A1-01",
    Código: 31333,
    Descrição: "CORTINA LAMINADA BRANCA/METALIZADO 155G/M2 L=1,60 TEXTIL",
    Mts: 500,
    Lote: "12345678",
    "Data Criação": "24/10/2024",
  };

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
      <Table data={testeJson} />
      {modalSearch && <SearchModal toggleModalSearch={toggleModalSearch} />}
      {modalAdd && <AddModal toggleModalAdd={toggleModalAdd} />}
    </div>
  );
}

export default ControlPanelPage;
