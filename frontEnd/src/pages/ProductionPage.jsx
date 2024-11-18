import { useState } from "react";
import Table from "../components/Table/DashboardTable";
import Title from "../components/Title";
import SearchModal from "../components/Modal/SearchModal";
import AddModal from "../components/Modal/AddModal";

function ProductionPage() {
  const [modalSearch, setModalSearch] = useState(false);
  const [modalAdd, setModalAdd] = useState(false);

  // Função para abrir e fechar os modais
  const toggleModalSearch = () => {
    setModalSearch(!modalSearch);
  };

  const toggleModalAdd = () => {
    setModalAdd(!modalAdd);
  };

  return (
    <div className="flex flex-col flex-grow p-4 overflow-x-hidden bg-gray-200">
      <Title>Painel de Produção</Title>
      <Table />
      {modalSearch && <SearchModal toggleModalSearch={toggleModalSearch} />}
      {modalAdd && <AddModal toggleModalAdd={toggleModalAdd} />}
    </div>
  );
}

export default ProductionPage;
