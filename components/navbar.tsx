import React from 'react'

import { UserButton } from '@clerk/nextjs';
import MobileSideBar from './mobile-sidebar';

const Navbar = () => {
  return (
    //Still working upon that account
    <div className='flex items-center p-4'>
            <MobileSideBar />
        <div className='flex w-full justify-end '>
            <UserButton afterSignOutUrl='/' />
        </div>
    </div>
  )
}

export default Navbar