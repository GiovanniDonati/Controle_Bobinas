/* eslint-disable react/prop-types */
import {
  ClipboardPen,
  History,
  HomeIcon,
  Scissors,
  SearchIcon,
  SquareKanban,
} from "lucide-react";
import ButtonAside from "./button/ButtonAside";

function Aside({ tabOpen, setTabOpen }) {
  return (
    <div className="flex flex-col items-center justify-start w-64 pt-4 space-y-4 bg-blue-300">
      <ButtonAside
        bgColor={
          tabOpen === "dashboard" ? "bg-green-500" : "hover:bg-green-500"
        }
        onClick={() => setTabOpen("dashboard")}
      >
        <HomeIcon /> Dashboard
      </ButtonAside>

      <ButtonAside
        bgColor={tabOpen === "search" ? "bg-blue-500" : "hover:bg-blue-500"}
        onClick={() => setTabOpen("search")}
      >
        <SearchIcon /> Pesquisar
      </ButtonAside>

      <ButtonAside
        bgColor={
          tabOpen === "production" ? "bg-orange-500" : "hover:bg-orange-400"
        }
        onClick={() => setTabOpen("production")}
      >
        <ClipboardPen /> Produção
      </ButtonAside>

      <ButtonAside
        bgColor={tabOpen === "retalhos" ? "bg-red-500" : "hover:bg-red-500"}
        onClick={() => setTabOpen("retalhos")}
      >
        <Scissors /> Retalhos
      </ButtonAside>

      <ButtonAside
        bgColor={
          tabOpen === "history" ? "bg-purple-500" : "hover:bg-purple-500"
        }
        onClick={() => setTabOpen("history")}
      >
        <History /> Histórico
      </ButtonAside>

      <ButtonAside
        bgColor={tabOpen === "visual" ? "bg-yellow-500" : "hover:bg-yellow-500"}
        onClick={() => setTabOpen("visual")}
      >
        <SquareKanban /> Est. Visual
      </ButtonAside>
    </div>
  );
}

export default Aside;
