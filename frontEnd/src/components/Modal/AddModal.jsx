/* eslint-disable react/prop-types */
import ModalInput from "../ModalInput";

function AddModal({ toggleModalAdd }) {
  const buttonModal =
    "min-lg:w-[30%] text-lg font-semibold px-4 py-3 text-white rounded-md text-center w-[40%]";
  return (
    <div className="fixed inset-0 flex items-start justify-center pt-20 bg-black/20">
      <div className="flex flex-col justify-center w-4/12 max-w-xl p-6 space-y-4 bg-white rounded-lg md:w-4/6 shadow-">
        <h2 className="mb-2 text-2xl font-semibold">Adicionar bobina</h2>
        <div className="flex w-full gap-5">
          <select
            name="local"
            className="px-2 py-4 text-base text-gray-700 bg-white border border-gray-200 rounded-md shadow-sm focus-within:border-blue-600 focus-within:ring-1 focus-within:ring-blue-600"
          >
            <option value="Prateleiras">Prateleiras</option>
            <option value="Grupos">Grupos</option>
            <option value="Retalhos">Retalhos</option>
          </select>
          <ModalInput placeholder="Endereço" />
        </div>
        <ModalInput placeholder="Código" type="number" />
        <ModalInput placeholder="Descrição" type="text" />
        <ModalInput placeholder="Metragem" type="number" />
        <ModalInput placeholder="Lote" type="number" />
        <ModalInput placeholder="Data" type="date" />
        <div className="flex justify-around">
          <button
            onClick={toggleModalAdd}
            className={`bg-red-500 hover:bg-red-600 ${buttonModal}`}
          >
            Fechar
          </button>
          <button
            onClick={toggleModalAdd}
            className={`bg-blue-500 hover:bg-blue-600 ${buttonModal}`}
          >
            Pesquisar
          </button>
        </div>
      </div>
    </div>
  );
}

export default AddModal;
