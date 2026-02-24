import { Product } from "@/types"
import { StarRating } from "../layout/StarRating"

const ProductOverview = ({product}: {product: Product}) => {
  return (
    <div>
       <div>
         <h1 className="text-2xl">{product.name}</h1>
         <div className="my-2">
          <StarRating value={4} readOnly />
         </div>
         <p className="text-gray-600">{product.description}</p>
         <div className="flex border-b border-gray-300 py-4">
          <p className="text-xl">${product.price}</p>
          <div className="mx-5">
            <p className="text-xl">Quantity</p>
            <div className="flex items-center">
              <button className="px-3 py-1 bg-gray-200 rounded-l">-</button>
              {product.quantity}
              <button className="px-3 py-1 bg-gray-200 rounded-r">+</button>
            </div>
          </div>
          <div>
            <button className="ml-4 px-4 py-2 bg-white text-primary border border-primary rounded">Buy It Now</button>
            <button className="ml-4 px-4 py-2 bg-primary text-white rounded">Visit Store</button>
          </div>
         </div>
         <div className="flex border-b border-gray-300 my-4 gap-5 py-4">
            <button className="border border-primary text-primary bg-white p-2 rounded">Make Offer</button>
            <button className="border border-primary text-primary bg-white p-2 rounded">Call Now</button>
            <button className="border border-primary text-primary bg-white p-2 rounded">Chat Now</button>
         </div>
       </div>
    </div>
  )
}

export default ProductOverview
