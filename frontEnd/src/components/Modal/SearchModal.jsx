/* eslint-disable react/prop-types */
import ButtonModal from "../button/ButtonModal";
import ModalInput from "../ModalInput";

function SearchModal({ toggleModalSearch }) {
  console.log("teste");
  return (
    <div className="fixed inset-0 flex items-start justify-center pt-40 bg-black/20">
      <div className="flex flex-col justify-center w-4/12 max-w-xl p-6 space-y-4 bg-white rounded-lg md:w-4/6">
        <h2 className="mb-2 text-2xl font-semibold">Pesquisar bobina</h2>
        <ModalInput placeholder="Endereço" />
        <ModalInput placeholder="Código" type="number" />
        <ModalInput placeholder="Lote" type="number" />
        <div className="flex justify-around">
          <ButtonModal
            bgColor="bg-red-500 hover:bg-red-600"
            onClick={toggleModalSearch}
          >
            Fechar
          </ButtonModal>
          <ButtonModal
            onClick={toggleModalSearch}
            bgColor="bg-blue-500 hover:bg-blue-600"
          >
            Pesquisar
          </ButtonModal>
        </div>
      </div>
    </div>
  );
}

export default SearchModal;
