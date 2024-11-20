import { useState } from "react";
import Table from "../components/Table/Table";
import Title from "../components/Title";
import SearchModal from "../components/Modal/SearchModal";
import ButtonTabs from "../components/button/ButtonTabs";
import { SearchIcon } from "lucide-react";

function ProductionPage() {
  const [modalSearch, setModalSearch] = useState(false);

  const toggleModalSearch = () => {
    setModalSearch(!modalSearch);
  };

  const dataTable = {
    Endereço: "A1-01",
    Código: "31333",
    Descrição: "CORTINA LAMINADA BRANCA/METALIZADO 155G/M2 L=1,60 TEXTIL",
    Mts: 500,
    Lote: "12345678",
    "Data Criação": "24/10/2024",
  };

  return (
    <div className="flex flex-col flex-grow p-4 overflow-x-hidden bg-gray-200">
      <div className="flex items-center">
        <Title>Painel de Produção</Title>
        <ButtonTabs
          bgColor="right-5 bg-blue-500 hover:bg-blue-600"
          onClick={toggleModalSearch}
        >
          <SearchIcon />
          Pesquisar
        </ButtonTabs>
      </div>
      <Table data={dataTable} />
      {modalSearch && <SearchModal toggleModalSearch={toggleModalSearch} />}
    </div>
  );
}

export default ProductionPage;
