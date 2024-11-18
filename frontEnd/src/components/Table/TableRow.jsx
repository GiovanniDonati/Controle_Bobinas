import { ArrowRightLeftIcon, QrCodeIcon, Trash2Icon } from "lucide-react";

function TableRow() {
  return (
    <tr className="odd:bg-blue-50 even:bg-white hover:bg-yellow-50">
      <Row>A-01-02</Row>
      <Row>31333</Row>
      <Row>CORTINA LAMINADA AZUL/PRATA 120G/M2 L=3,20 PROPEX</Row>
      <Row>500 {"Mt"}</Row>
      <Row>12345678</Row>
      <Row>24/10/2024</Row>
      <td className="flex justify-center py-2 gap-x-1 whitespace-nowrap">
        <ArrowRightLeftIcon className="w-6 h-6 text-yellow-500 cursor-pointer hover:text-yellow-300" />
        <QrCodeIcon className="w-6 h-6 text-black cursor-pointer hover:text-gray-500" />
        <Trash2Icon className="w-6 h-6 text-red-500 cursor-pointer hover:text-red-300" />
      </td>
    </tr>
  );
}

export default TableRow;

function Row({ ...props }) {
  return (
    <td
      {...props}
      className="px-1 py-2 text-base text-center text-gray-700 border-x-2 whitespace-nowrap"
    />
  );
}
