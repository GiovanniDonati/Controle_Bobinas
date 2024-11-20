/* eslint-disable react/prop-types */
import { ArrowRightLeftIcon, QrCodeIcon, Trash2Icon } from "lucide-react";

function TableRow({ rowData }) {
  return (
    <tr className="odd:bg-blue-50 even:bg-white hover:bg-yellow-50">
      {Object.values(rowData).map((value, index) => (
        <TableCol key={index}>{value}</TableCol>
      ))}
      <td className="flex justify-center py-2 gap-x-1 whitespace-nowrap">
        <ArrowRightLeftIcon className="w-6 h-6 text-yellow-500 cursor-pointer hover:text-yellow-300" />
        <QrCodeIcon className="w-6 h-6 text-black cursor-pointer hover:text-gray-500" />
        <Trash2Icon className="w-6 h-6 text-red-500 cursor-pointer hover:text-red-300" />
      </td>
    </tr>
  );
}

function TableCol({ children }) {
  return (
    <td className="px-1 py-2 text-base text-center text-gray-700 max-lg:text-sm border-x-2 whitespace-nowrap">
      {children}
    </td>
  );
}

export default TableRow;
