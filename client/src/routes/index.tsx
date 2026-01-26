import ProductCardSkeleton from '@/components/layout/ProductCardSkeleton'
import ProductCard from '@/components/product/ProductCard'
import { createFileRoute } from '@tanstack/react-router'
import { useEffect, useState } from 'react'

export const Route = createFileRoute('/')({ component: App })

function App() {
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [products, setProducts] = useState<Array<number>>([1,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]);
  const productTest = {
    id: 1,
    name: 'Sample Product',
    price: 29.99,
    image: '/ecommerce.png',
  };

  useEffect(() => {
    setIsLoading(true);
    setTimeout(() => {
      setIsLoading(false);
    }, 2000);
  }, []);

  return (
    <div>
       <div
        className="grid gap-6 grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4"
      >
        {isLoading
        ? Array.from({ length: 20 }).map((_, index) => (
            <ProductCardSkeleton key={index} />
          ))
        : products.map((product) => (
            <ProductCard product={productTest} />
          ))
        }
      </div>
    </div>
  )
}
