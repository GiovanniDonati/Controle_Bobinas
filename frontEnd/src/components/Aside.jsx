/* eslint-disable react/prop-types */
import {
  ClipboardPen,
  History,
  HomeIcon,
  MenuIcon,
  Scissors,
  SquareKanban,
} from "lucide-react";
import ButtonAside from "./button/ButtonAside";

function Aside({ tabOpen, setTabOpen, menuVisibility, setMenuVisibily }) {
  const desktop = window.innerWidth > 1024;
  return (
    <div
      className={`flex flex-col items-center justify-start pt-4 space-y-4 bg-blue-300 ${
        desktop || menuVisibility
          ? `w-[200px] ${menuVisibility && "absolute h-screen"}`
          : "w-[80px]"
      }`}
    >
      {desktop || menuVisibility ? (
        <div className="flex flex-col justify-between w-1/2 h-20 p-1 bg-white rounded-md shadow-lg">
          <button>Admin</button>
          <button className="text-sm font-semibold text-end">Sair</button>
        </div>
      ) : (
        <MenuIcon
          className="items-center text-white"
          onClick={() => setMenuVisibily(!menuVisibility)}
        />
      )}

      <ButtonAside
        bgColor={
          tabOpen === "dashboard" ? "bg-green-500" : "hover:bg-green-500"
        }
        onClick={() => setTabOpen("dashboard")}
      >
        <HomeIcon />
        {desktop || (menuVisibility && " Dashboard")}
      </ButtonAside>

      <ButtonAside
        bgColor={tabOpen === "visual" ? "bg-yellow-500" : "hover:bg-yellow-500"}
        onClick={() => setTabOpen("visual")}
      >
        <SquareKanban />
        {desktop || (menuVisibility && " Est. Visual")}
      </ButtonAside>

      <ButtonAside
        bgColor={
          tabOpen === "production" ? "bg-orange-500" : "hover:bg-orange-400"
        }
        onClick={() => setTabOpen("production")}
      >
        <ClipboardPen />
        {desktop && " Produção"}
      </ButtonAside>

      <ButtonAside
        bgColor={tabOpen === "retalhos" ? "bg-red-500" : "hover:bg-red-500"}
        onClick={() => setTabOpen("retalhos")}
      >
        <Scissors />
        {desktop && " Retalhos"}
      </ButtonAside>

      <ButtonAside
        bgColor={
          tabOpen === "history" ? "bg-purple-500" : "hover:bg-purple-500"
        }
        onClick={() => setTabOpen("history")}
      >
        <History />
        {desktop && " Histórico"}
      </ButtonAside>

      {desktop && (
        <p className="fixed font-serif text-xs text-center text-white bottom-2">
          Development by: <br />
          <i>Giovanni R. Donati</i>
        </p>
      )}
    </div>
  );
}

export default Aside;
