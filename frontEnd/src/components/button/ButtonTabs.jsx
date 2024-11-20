/* eslint-disable react/prop-types */
function ButtonTabs({ bgColor, ...props }) {
  return (
    <button
      {...props}
      className={`fixed flex gap-2 px-3 py-2 font-bold text-white rounded-md ${bgColor}`}
    >
      {props.children}
    </button>
  );
}

export default ButtonTabs;
