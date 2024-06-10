import React, { useState } from 'react'
import Hamburger from 'hamburger-react'

const Hamburgeranimation = () => {

  const [isOpen, setisOpen] = useState(false)

  const handleClick =()=>{
    setisOpen(!isOpen)
  }

  return (
    <Hamburger
      toggled={isOpen}
      toggle={setisOpen}
      color='#171211'
      size = {30}
      label='Show menu'
      hideOutline={false}
      onToggle={handleClick}
      />
  )
}

export default Hamburgeranimation
