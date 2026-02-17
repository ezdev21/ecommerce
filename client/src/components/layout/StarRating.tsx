
import { useState } from "react"
import { Star } from "lucide-react"
import { cn } from "@/lib/utils"

type StarRatingProps = {
  totalStars?: number
  value?: number
  onChange?: (value: number) => void
  size?: number
  readOnly?: boolean
}

export function StarRating({
  totalStars = 5,
  value = 0,
  onChange,
  size = 20,
  readOnly = false,
}: StarRatingProps) {
  const [hover, setHover] = useState<number | null>(null)

  return (
    <div className="flex items-center gap-1">
      {Array.from({ length: totalStars }).map((_, index) => {
        const ratingValue = index + 1
        const isActive = hover
          ? ratingValue <= hover
          : ratingValue <= value

        return (
          <Star
            key={index}
            size={size}
            className={cn(
              "cursor-pointer transition-colors duration-200",
              isActive
                ? "fill-yellow-400 text-yellow-400"
                : "text-muted-foreground"
            )}
            onMouseEnter={() => !readOnly && setHover(ratingValue)}
            onMouseLeave={() => !readOnly && setHover(null)}
            onClick={() => !readOnly && onChange?.(ratingValue)}
          />
        )
      })}
    </div>
  )
}
