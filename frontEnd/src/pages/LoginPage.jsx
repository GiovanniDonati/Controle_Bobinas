/* eslint-disable react/no-unknown-property */
import { useNavigate } from "react-router-dom";
import ModalInput from "../components/ModalInput";

function LoginPage() {
  const navigate = useNavigate();

  const handleLogin = () => {
    navigate("/home");
  };

  return (
    <div className="flex items-center justify-center flex-grow h-screen">
      <div className="flex flex-col gap-3 p-3 bg-white border-2 rounded-md shadow-xl w-96">
        <img src="./logo.ico" className="self-center w-28" />
        <h1 className="pl-2 text-xl font-semibold">Login</h1>
        <div>
          <ModalInput type="text" placeholder="Usuário" />
          <br />
          <ModalInput type="password" placeholder="Senha" />
        </div>
        <button
          onClick={handleLogin}
          className="self-center w-2/5 py-2 text-lg font-semibold text-center text-white bg-green-500 rounded-md hover:bg-green-300 "
        >
          Entrar
        </button>
        <p className="self-end text-[10px] text-gray-500">
          Caso ainda não possua login, solicite ao setor de TI
        </p>
      </div>
    </div>
  );
}

export default LoginPage;
