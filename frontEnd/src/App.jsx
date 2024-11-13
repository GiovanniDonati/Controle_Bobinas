function App() {
  return (
    <div className="flex w-full h-screen">
      <aside className="flex flex-col pt-10 gap-y-5 items-center justify-start w-1/5 bg-red-100">
        <button>Home</button>
        <button>Pesquisar</button>
        <button>Produção</button>
        <button>Histórico</button>
        <button>Retalhos</button>
      </aside>
      <main className="w-4/5 bg-green-100">
        <h1>Welcome to Control Panel</h1>
      </main>
    </div>
  );
}

export default App;
