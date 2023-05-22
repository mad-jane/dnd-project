import React, { useEffect, useState } from "react";
// import { Switch, Route } from "react-router-dom";

function App() {

    const [data, setData] = useState([])

    useEffect(() => {
        fetch("/campaigns").then(
            response => response.json()
        ).then(
            data => {
                    setData(data)
                    console.log(data)
            }
        )
    },[])

    return (
        <div>

        </div>
    )
}

export default App;
