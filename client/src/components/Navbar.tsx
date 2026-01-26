import { Search, Heart, Bell, ShoppingCart, Phone, Menu, User } from "lucide-react";

export default function Navbar() {
  return (
    <header className="w-full bg-green-400 text-white flex justify-between items-center">
      <div className="flex items-center gap-2 px-5">
        <img src="ecommerce.png" className="w-40"/>
        <h1 className="text-5xl font-bold">Ezra <br></br> Market</h1>
      </div>
      <div className="flex flex-col">
        <div className="flex items-center justify-between px-6 py-3 gap-15">
          {/* Search */}
          <div className="flex flex-1 max-w-2xl">
            <select className="px-5 py-2 text-gray-700 bg-gray-200 rounded-l outline-none">
              <option>Filter</option>
              <option>Electronics</option>
              <option>Fashion</option>
              <option>Vehicles</option>
              <option>Property</option>
              <option>Furniture</option>
              <option>Bauty</option>
              <option>Construction</option>
              <option>Babies and Kids</option>
            </select>
            <input
              type="text"
              placeholder="I'm shopping for..."
              className="flex-1 px-4 py-2 text-gray-700 bg-white outline-none"
            />
            <button className="px-7 bg-green-700 rounded-r-full">
              <Search size={18} />
            </button>
          </div>

          {/* Icons */}
          <div className="flex items-center gap-10">
            <div className="relative">
              <Heart />
              <span className="absolute -top-2 -right-2 text-xs bg-green-700 rounded-full px-1">0</span>
            </div>
            <div className="relative">
              <Bell />
              <span className="absolute -top-2 -right-2 text-xs bg-green-700 rounded-full px-1">1</span>
            </div>
            <div className="relative">
              <ShoppingCart />
              <span className="absolute -top-2 -right-2 text-xs bg-green-700 rounded-full px-1">2</span>
            </div>
          </div>
          <div className="cursor-pointer rounded-full bg-green-700 p-3">
            <User size={20} />
          </div>
        </div>
        <nav className="flex items-center justify-between px-6 py-2 bg-green-600">
          <button className="flex items-center gap-2 bg-green-700 px-4 py-2 rounded">
            <Menu size={18} />
            <span>Shop by Category</span>
          </button>

          <ul className="flex items-center gap-8">
            <li className="cursor-pointer">Home</li>
            <li className="cursor-pointer">News</li>
            <li className="cursor-pointer">Vendors</li>
            <li className="cursor-pointer">Suppliers</li>
          </ul>

          <div className="flex items-center gap-6">
            <span className="cursor-pointer">Become a Seller</span>
            <div className="flex items-center gap-2 cursor-pointer">
              <Phone size={16} />
              <span>Contact Us</span>
            </div>
          </div>
        </nav>
      </div>
    </header>
  );
}
