/* eslint-disable react/prop-types */
function ModalInput({ placeholder, ...props }) {
  return (
    <label className="relative block py-3 text-base border border-gray-200 rounded-md shadow-sm focus-within:border-blue-600 focus-within:ring-1 focus-within:ring-blue-600">
      <input
        {...props}
        placeholder={placeholder}
        className="px-2 text-xl placeholder-transparent uppercase bg-transparent border-none peer focus:border-transparent focus:outline-none focus:ring-0"
      />
      <span className="pointer-events-none absolute start-2.5 top-0 -translate-y-1/2 bg-white p-0.5 text-base text-gray-700 transition-all peer-placeholder-shown:top-1/2 peer-placeholder-shown:text-sm peer-focus:top-0 peer-focus:text-xs">
        {placeholder}
      </span>
    </label>
  );
}

export default ModalInput;
