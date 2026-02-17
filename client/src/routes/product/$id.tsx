import ProductNotFound from '@/components/product/ProductNotFound'
import ProductOverview from '@/components/product/ProductOverview'
import ProductReviews from '@/components/product/ProductReview'
import RecommendedProducts from '@/components/product/recommended/Recommendedproducts'
import { createFileRoute, useLoaderData } from '@tanstack/react-router'

export const Route = createFileRoute('/product/$id')({
  component: RouteComponent,
  loader: async ({ params }) => {
    const { id } = params
    return {
      id: id,
      name: "Nicon Camera",
      description: "A high-quality camera for capturing stunning photos and videos.",
      price: 100,
      image: "https://images.unsplash.com/photo-1599664223843-9349c75196bc",
      quantity: 1,
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toDateString(),
    }
  },  
  notFoundComponent: ProductNotFound
})

function RouteComponent() {
  const product = useLoaderData({from: '/product/$id'})
  return(
    <div className='flex'>
      <div className='w-1/4'>
        <img
          src={product.image}
          alt="image"
          className="w-96 h-96 mb-4 object-cover"
        />
        <img
          src={product.image}
          alt="image"
          className="w-96 h-96 mb-4 object-cover"
        />
        <img
          src={product.image}
          alt="image"
          className="w-96 h-96 mb-4 object-cover"
        />
      </div>
      <div className='w-1/2 p-3'>
        <ProductOverview product={product}/>
        <ProductReviews />
      </div>
      <div className='w-1/4'>
         <RecommendedProducts />
      </div>
    </div>
  )
}
