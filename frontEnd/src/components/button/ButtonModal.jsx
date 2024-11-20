/* eslint-disable react/prop-types */
function ButtonModal({ bgColor, ...props }) {
  return (
    <button
      {...props}
      className={`w-[30%] text-lg font-semibold px-4 py-3 text-white rounded-md ${bgColor}`}
    >
      {props}
    </button>
  );
}

export default ButtonModal;
