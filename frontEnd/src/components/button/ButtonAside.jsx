/* eslint-disable react/prop-types */
function ButtonAside({ bgColor, ...props }) {
  return (
    <button
      {...props}
      className={`flex items-center sm:w-[90%] lg:w-[80%] xl:w-[90%] gap-2 px-4 py-1 text-lg rounded-xl font-bold text-white transition-all duration-300 ${bgColor} hover:rounded-md`}
      onClick={props.onClick}
    >
      {props.children}
    </button>
  );
}

export default ButtonAside;
