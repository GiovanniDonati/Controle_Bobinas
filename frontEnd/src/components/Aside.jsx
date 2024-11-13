import {
  ClipboardPen,
  History,
  HomeIcon,
  Scissors,
  SearchIcon,
  SquareKanban,
} from "lucide-react";
import ButtonAside from "./button/ButtonAside";

function Aside() {
  return (
    <div className="flex flex-col items-center justify-start w-64 pt-4 space-y-4 bg-blue-300">
      <ButtonAside bgColor="hover:bg-green-500">
        <HomeIcon /> Dashboard
      </ButtonAside>

      <ButtonAside bgColor="hover:bg-blue-500">
        <SearchIcon /> Pesquisar
      </ButtonAside>

      <ButtonAside bgColor="hover:bg-orange-400">
        <ClipboardPen />
        Produção
      </ButtonAside>

      <ButtonAside bgColor="hover:bg-red-500">
        <Scissors /> Retalhos
      </ButtonAside>

      <ButtonAside bgColor="hover:bg-purple-500">
        <History />
        Histórico
      </ButtonAside>

      <ButtonAside bgColor="hover:bg-yellow-500">
        <SquareKanban /> Est. Visual
      </ButtonAside>
    </div>
  );
}

export default Aside;
