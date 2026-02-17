import ProductNotFound from '@/components/product/ProductNotFound'
import ProductOverview from '@/components/product/ProductOverview'
import ProductReviews from '@/components/product/ProductReviews'
import RecommendedProducts from '@/components/product/Recommendedproducts'
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
      image: "https://images.unsplash.com/photo-1519183071298-a2962ccf0e1c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y2FtZXJhfGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60",
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
      </div>
      <div className='w-1/2'>
        <ProductOverview product={product}/>
        <ProductReviews />
      </div>
      <div className='w-1/4'>
         <RecommendedProducts />
      </div>
    </div>
  )
}
