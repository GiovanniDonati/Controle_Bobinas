/* eslint-disable react/prop-types */
import {
  ClipboardPen,
  History,
  HomeIcon,
  MenuIcon,
  Scissors,
  SquareKanban,
  UserCircle2,
} from "lucide-react";
import ButtonAside from "./button/ButtonAside";
import { useNavigate } from "react-router-dom";

function Aside({ tabOpen, setTabOpen, menuVisibility, setMenuVisibily }) {
  const navigate = useNavigate();

  const handleExit = () => {
    navigate("/login");
  };

  const desktop = window.innerWidth > 1024;
  return (
    <div
      className={`flex flex-col items-center justify-start pt-4 space-y-4 bg-blue-300 ${
        desktop || menuVisibility
          ? `w-[220px] ${menuVisibility && "absolute h-screen"}`
          : "w-[80px]"
      }`}
    >
      {(desktop || menuVisibility) && (
        <div className="flex flex-col items-center px-2 pt-1 bg-white rounded-md shadow-lg w-28 justify-">
          <UserCircle2 />
          <button>Admin</button>
          <button className="self-end text-sm" onClick={handleExit}>
            Sair
          </button>
        </div>
      )}
      {!desktop && (
        <ButtonAside onClick={() => setMenuVisibily(!menuVisibility)}>
          <MenuIcon />
          {desktop || (menuVisibility && "Menu")}
        </ButtonAside>
      )}

      <ButtonAside
        bgColor={
          tabOpen === "dashboard" ? "bg-green-500" : "hover:bg-green-500"
        }
        onClick={() => {
          setTabOpen("dashboard");
          menuVisibility && setMenuVisibily(!menuVisibility);
        }}
      >
        <HomeIcon />
        {(desktop || menuVisibility) && " Dashboard"}
      </ButtonAside>

      <ButtonAside
        bgColor={tabOpen === "visual" ? "bg-yellow-500" : "hover:bg-yellow-500"}
        onClick={() => {
          setTabOpen("visual");
          menuVisibility && setMenuVisibily(!menuVisibility);
        }}
      >
        <SquareKanban />
        {(desktop || menuVisibility) && " Est. Visual"}
      </ButtonAside>

      <ButtonAside
        bgColor={
          tabOpen === "production" ? "bg-orange-500" : "hover:bg-orange-400"
        }
        onClick={() => {
          setTabOpen("production");
          menuVisibility && setMenuVisibily(!menuVisibility);
        }}
      >
        <ClipboardPen />
        {(desktop || menuVisibility) && " Produção"}
      </ButtonAside>

      <ButtonAside
        bgColor={tabOpen === "retalhos" ? "bg-red-500" : "hover:bg-red-500"}
        onClick={() => {
          setTabOpen("retalhos");
          menuVisibility && setMenuVisibily(!menuVisibility);
        }}
      >
        <Scissors />
        {(desktop || menuVisibility) && " Retalhos"}
      </ButtonAside>

      <ButtonAside
        bgColor={
          tabOpen === "history" ? "bg-purple-500" : "hover:bg-purple-500"
        }
        onClick={() => {
          setTabOpen("history");
          menuVisibility && setMenuVisibily(!menuVisibility);
        }}
      >
        <History />
        {(desktop || menuVisibility) && " Histórico"}
      </ButtonAside>
      {(desktop || menuVisibility) && (
        <p className="absolute font-serif text-xs text-center text-white bottom-2">
          Development by: <br />
          <i>Giovanni R. Donati</i>
        </p>
      )}
    </div>
  );
}

export default Aside;
