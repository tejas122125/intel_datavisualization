import React from 'react'
import { SignUp } from '@clerk/nextjs'

const SignUpPage = () => {
  return (
    <div className='flex items-center w-full justify-center h-screen'>
        <SignUp />
    </div>
  )
}

export default SignUpPage