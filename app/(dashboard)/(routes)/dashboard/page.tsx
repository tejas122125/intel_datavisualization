'use client'


import React from 'react'
import { cn } from '@/lib/utils'
import { useRouter } from 'next/navigation'



const dashboard = () => {

  const router = useRouter()

  return (
    <div>
    <div className='mb-8 space-y-4'>
      <h2 className='text-2xl md:text-4xl font-bold text-center'>
        This is your Dashboard
      </h2>
      <p className='text-muted-foreground font-light text-sm md:text-lg text-center'>
        Analysis here !
      </p>
    </div>
  
    </div>
  )
}

export default dashboard