import { Link } from '@tanstack/react-router'

import { useState } from 'react'
import Sidebar from './Sidebar'
import Navbar from './Navbar'

export default function Header() {
  const [isOpen, setIsOpen] = useState(false)

  return (
    <>
        {/* <button
          onClick={() => setIsOpen(true)}
          className="p-2 hover:bg-gray-700 rounded-lg transition-colors"
          aria-label="Open menu"
        >
          <Menu size={24} />
        </button> */}
        <Navbar />
      <Sidebar isOpen={isOpen} setIsOpen={setIsOpen} />
    </>
  )
}
