import React, { useEffect } from "react"

const Home = () => {
    useEffect(()=>{
        console.log("i run first when the app loads")
    },[])
    return (
        <>Hello from Home</>
    )
}
export default Home