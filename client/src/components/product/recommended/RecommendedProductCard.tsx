import { Product } from "@/types"

function RecommendedProductCard({product}: {product: Product}) {
  return (
    <div
      key={product.id}
      className="rounded flex flex-col items-center my-2 shadow-xl"
    >
      <a href={`/product/${product.id}`}>
        <img
          src={product.image}
          alt="image"
          className="object-cover"
        />
        <div className="p-3">
          <h2 className="text-lg font-semibold">{product.name}</h2>
          <p className="text-gray-400">${product.price}</p>
          <p className="text-gray-400">{product.description}</p>
        </div>
      </a>
    </div>
  )
}

export default RecommendedProductCard
