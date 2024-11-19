import TableRow from "./TableRow";

function Table() {
  return (
    <div className="self-center w-full mt-2 overflow-auto bg-white rounded-md">
      <table className="min-w-full text-sm divide-y divide-gray-500 ">
        <thead>
          <tr>
            <TableIndex>Endereço</TableIndex>
            <TableIndex>Código</TableIndex>
            <TableIndex>Descrição</TableIndex>
            <TableIndex>Mts</TableIndex>
            <TableIndex>Lote</TableIndex>
            <TableIndex>Data Criação</TableIndex>
            <TableIndex>Ações</TableIndex>
          </tr>
        </thead>
        <tbody>
          <TableRow />
          <TableRow />
          <TableRow />
          <TableRow />
          <TableRow />
          <TableRow />
          <TableRow />
          <TableRow />
          <TableRow />
          <TableRow />
          <TableRow />
          <TableRow />
          <TableRow />
          <TableRow />
          <TableRow />
          <TableRow />
          <TableRow />
          <TableRow />
          <TableRow />
        </tbody>
      </table>
    </div>
  );
}

export default Table;

function TableIndex({ ...props }) {
  return (
    <th
      {...props}
      className="px-2 py-2 text-base font-medium text-gray-900 bg-green-100 border-green-200 max-xl:text-xs border-x-2 whitespace-nowrap"
    />
  );
}
