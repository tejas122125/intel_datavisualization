import React from 'react'
import { Comfortaa } from 'next/font/google'
import Navbar from '@/components/navbar'
import Sidebar from '@/components/sidebar'



const comfortaa = Comfortaa({
    subsets:['latin'],
    weight:'700',
    style:'normal',
    display:'swap',
    
}) 

const DashboardLayout = ({children}:{children : React.ReactNode}) => {
  return (
    <main className={comfortaa.className}>
    <div className='h-full relative '>
        <div className='hidden h-full md:flex md:flex-col md:fixed md:inset-y-0 z-[80] md:w-72'>
            <Sidebar />

        </div>
        <main className='md:pl-72'>
          <Navbar />
          {children}
        </main>

    </div>
    </main>
    
  )
}

export default DashboardLayout