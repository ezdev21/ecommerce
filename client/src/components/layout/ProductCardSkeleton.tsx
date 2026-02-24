
const ProductCardSkeleton = ({key}: {key: number}) => {
  return (
    <div
      key={key}
      className="bg-white p-4 rounded shadow flex flex-col items-center"
    >
      <div className="w-48 h-48 mb-4 bg-gray-300 animate-pulse" />
      <div className="w-28 h-6 bg-gray-300 animate-pulse mb-2" />
      <div className="w-16 h-4 bg-gray-300 animate-pulse" />
    </div>
  )
}

export default ProductCardSkeleton
