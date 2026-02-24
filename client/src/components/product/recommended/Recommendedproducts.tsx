import { useState } from "react";
import RecommendedProductCardSkeleton from "./RecommendedProductCardSkeleton";
import RecommendedProductCard from "./RecommendedProductCard";

const RecommendedProducts = () => {
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [products, setProdcuts] = useState<Array<number>>([1,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]);
  const productTest = {
    id: '1',
    name: "Nicon Camera",
    description: "A high-quality camera for capturing stunning photos and videos.",
    price: 100,
    image: "https://images.unsplash.com/photo-1599664223843-9349c75196bc",
    quantity: 1,
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toDateString(),
  }
  return (
    <div>
      <h1 className="text-2xl text-center">Recommended for you</h1>
      <div>
        {isLoading
        ? Array.from({ length: 10 }).map((_, index) => (
            <RecommendedProductCardSkeleton key={index} />
          ))
        : products.map((product) => (
            <RecommendedProductCard product={productTest} />
          ))
        }
      </div>
    </div>
  )
}

export default RecommendedProducts
