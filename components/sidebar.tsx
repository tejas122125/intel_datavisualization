'use client'
import React from 'react'
import styles from './Sidebar.module.css'
import Link from 'next/link'
import Image from 'next/image'
import { Montserrat } from 'next/font/google'
import { cn } from '@/lib/utils'
import { Code, FileQuestion, ImageIcon, LayoutDashboard, MessageSquare, Music, Settings, VideoIcon } from 'lucide-react'
import { usePathname } from 'next/navigation'
import { Comfortaa } from 'next/font/google'

const montserrat = Montserrat({
  weight:'600',
  subsets:['latin']
})

const comfortaa = Comfortaa({
  weight:'600',
  subsets:['latin']
})

const routes= [
  {
    label:'Dashboard',
    icon: LayoutDashboard ,
    href:'/dashboard',
    color: "text-purple-950",
  },
  {
    label:'Maximum',
    icon: MessageSquare ,
    href:'/conversation',
    color: "text-purple-950",
  },
  {
    label:'Average',
    icon: Code,
    href:'/image',
    color: "text-purple-950",
  },
  {
    label:'FAQs',
    icon: FileQuestion,
    href:'/video',
    color: "text-purple-950",
  },
  {
    label:'Settings',
    icon: Settings ,
    href:'/settings',
    color: "text-purple-950",
  },

]

const Sidebar = () => {

   const pathname = usePathname();
  return (
    <div className={cn('space-y-4 py-4 flex flex-col  ',styles.sidebar)}>
        <div className='px-3 py-2 flex-1'>
          <Link
          href='/dashboard'
          className='flex items-center pl-3 mb-14'
          >
            <div className='relative w-8 h-8 mr-4'>
              <Image
              src = '/logo.png'
               fill
               alt = "logo"
               />
                </div>
               <h1 className={cn('text-2xl font-bold',montserrat.className)}>Chrono</h1>
          </Link>
          <div className='space-y-1'>
            {routes.map((route)=>(
              <Link
              href={route.href}
              key ={route.href}
              className={cn('text-sm group flex p-3 w-full justify-start font-medium cursor-pointer hover:text-white hover:bg-white/20 rounded-lg transition', pathname===route.href ? 'text-white bg-white/10' :'text-pink-300',comfortaa.className)}
              >
                <div className='flex items-center flex-1'>
                  <route.icon className={cn('h-5 w-5 mr-3',route.color)} />
                  {route.label}
                </div>

              </Link>
            ))}
          </div>

        </div>

    </div>
  )
}

export default Sidebar