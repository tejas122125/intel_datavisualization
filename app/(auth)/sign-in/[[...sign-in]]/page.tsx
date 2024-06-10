import React from 'react'
import { SignIn } from '@clerk/nextjs'

const SignInPage = () => {
  return (
    <div className='flex items-center h-screen w-full justify-center'>
      <SignIn />
    </div>
  )
}

export default SignInPage