/* eslint-disable react/prop-types */
import {
  ClipboardPen,
  History,
  HomeIcon,
  Scissors,
  SquareKanban,
} from "lucide-react";
import ButtonAside from "./button/ButtonAside";

function Aside({ tabOpen, setTabOpen }) {
  return (
    <div className="flex flex-col items-center justify-start pt-4 space-y-4 bg-blue-300 w-60">
      <ButtonAside
        bgColor={
          tabOpen === "dashboard" ? "bg-green-500" : "hover:bg-green-500"
        }
        onClick={() => setTabOpen("dashboard")}
      >
        <HomeIcon /> Dashboard
      </ButtonAside>

      <ButtonAside
        bgColor={tabOpen === "visual" ? "bg-yellow-500" : "hover:bg-yellow-500"}
        onClick={() => setTabOpen("visual")}
      >
        <SquareKanban /> Est. Visual
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

      <p className="fixed font-serif text-xs text-center text-white bottom-2">
        Development by: <br />
        <i>Giovanni R. Donati</i>
      </p>
    </div>
  );
}

export default Aside;
