/* eslint-disable react/prop-types */
import ModalInput from "./ModalInput";

function SearchModal({ toggleModal }) {
  const buttonModal =
    "w-[30%] text-lg font-semibold px-4 py-3 text-white rounded-full";

  return (
    <div className="fixed inset-0 flex items-start justify-center pt-40 bg-black/20">
      <div className="flex flex-col justify-center w-4/12 max-w-xl p-6 space-y-4 bg-white rounded-lg shadow-">
        <h2 className="mb-2 text-2xl font-semibold">Pesquisar bobina</h2>
        <ModalInput placeholder="Endereço" />
        <ModalInput placeholder="Código" type="number" />
        <ModalInput placeholder="Lote" type="number" />
        <div className="flex justify-around">
          <button
            onClick={toggleModal}
            className={`bg-red-500 hover:bg-red-600 ${buttonModal}`}
          >
            Fechar
          </button>
          <button
            onClick={toggleModal}
            className={`bg-blue-500 hover:bg-blue-600 ${buttonModal}`}
          >
            Pesquisar
          </button>
        </div>
      </div>
    </div>
  );
}

export default SearchModal;
