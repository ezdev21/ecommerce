
const ProductCard = ({product}: {product: any}) => {
  return (
    <div
      key={product.id}
      className="bg-white p-4 rounded shadow flex flex-col items-center"
    >
      <img
        src={product.image}
        alt="image"
        className="w-48 h-48 mb-4 object-cover"
      />
      <h2 className="text-lg font-semibold">{product.name}</h2>
      <p className="text-gray-400">${product.price}</p>
    </div>
  )
}

export default ProductCard
