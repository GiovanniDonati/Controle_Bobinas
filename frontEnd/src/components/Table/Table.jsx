/* eslint-disable react/prop-types */
import TableRow from "./TableRow";

function Table({ data }) {
  return (
    <div className="self-center w-full mt-2 overflow-auto bg-white rounded-md">
      <table className="min-w-full text-sm divide-y divide-gray-500">
        <thead>
          <tr>
            {Object.keys(data).map((value, index) => (
              <TableIndex key={index}>{value}</TableIndex>
            ))}
            <TableIndex>Ações</TableIndex>
          </tr>
        </thead>
        <tbody>
          <TableRow rowData={data} />
        </tbody>
      </table>
    </div>
  );
}

export default Table;

function TableIndex({ children }) {
  return (
    <th className="px-2 py-2 text-base font-medium text-gray-900 bg-green-100 border-green-200 max-xl:text-xs border-x-2 whitespace-nowrap">
      {children}
    </th>
  );
}
