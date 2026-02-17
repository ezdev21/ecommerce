import { FormEvent, useState } from "react"
import { StarRating } from "../layout/StarRating"
import { Input } from "../ui/input"
import { Textarea } from "../ui/textarea";

function ProductReview() {
    const [name, setName] = useState<string>('');
    const [email, setEmail] = useState<string>('');
    const [rating, setRating] = useState<number>(0);
    const [comment, setComment] = useState<string>('');
  return (
    <div>
      <h1 className="text-xl mb-5">Reviews(2 total reviews)</h1>
      <form>
        <Input
          type="text"
          name="name"
          placeholder="John Doe"
          onChange={(e) => setName(e.target.value)}
          required
          className="mb-4 flex-1 p-3 border border-gray-300 rounded-sm bg-white text-gray-800 focus:outline-2 focus:outline-primary outline-1 outline-primary"
        />

        <Input
          type="email"
          name="email"
          placeholder="john@example.com"
          onChange={(e) => setEmail(e.target.value)}
          required
          className="mb-4 flex-1 p-3 border border-gray-300 rounded-sm bg-white text-gray-800 focus:outline-2 focus:outline-primary outline-1 outline-primary"
        />

        <StarRating value={0} />

        <Textarea
          name="message"
          placeholder="Hello..."
          onChange={(e) => setComment(e.target.value)}
          rows={5}
          required
          className="my-4 w-full p-3 border border-gray-300 rounded-sm bg-white text-gray-800 outline-1 outline-primary focus:outline-2 focus:outline-primary resize-none"
        />
      </form>
    </div>
  )
}

export default ProductReview
