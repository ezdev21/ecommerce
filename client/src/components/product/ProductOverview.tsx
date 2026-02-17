import { Product } from "@/types"

const ProductOverview = ({product}: {product: Product}) => {
  return (
    <div>
       <div>
        <h1 className="text-3xl">Overview</h1>
         <h1 className="text-2xl">{product.name}</h1>
         <div>
          stars(2 reviews)
         </div>
         <p>{product.description}</p>
         <div className="flex border-b border-gray-300 my-4 py-4">
          <p className="text-2xl font-bold">${product.price}</p>
          <div className="mx-5">
            <p className="text-xl font-bold">Quantity</p>
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
            <button className="border-primary text-primary bg-white p-2">Make Offer</button>
            <button className="border-primary text-primary bg-white p-2">Call Now</button>
            <button className="border-primary text-primary bg-white p-2">Chat Now</button>
         </div>
       </div>
    </div>
  )
}

export default ProductOverview
