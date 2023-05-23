import React, { useEffect, useState, useCallback } from "react";
// import { Switch, Route } from "react-router-dom";

function App() {

    const [campaigns, setCampaigns] = useState([])
    const [characters, setCharacters] = useState([])
    const [users, setUsers] = useState([])

    const fetchCampaignsFallback = useCallback( () => {
        fetchCampaigns()
    },
    [])

    const fetchUsersFallback = useCallback( () => {
        fetchUsers()
    },
    [])

    const fetchCharactersFallback = useCallback( () => {
        fetchCharacters()
    },
    [])


    useEffect(() => {
        fetchCampaignsFallback()
        fetchUsersFallback()
        fetchCharactersFallback()
    },[fetchCampaignsFallback, fetchUsersFallback, fetchCharactersFallback])

    const fetchCampaigns = () => {
        fetch("/campaigns").then(
            response => response.json()
        ).then(
            data => {
                setCampaigns(data);
            }
        ).then(
            console.log("campaigns: ", campaigns)
        )
    }

    const fetchCharacters = () => {
        fetch("/characters").then(
            response => response.json()
        ).then(
            data => {
                setCharacters(data);
            }
        ).then(
            console.log("Characters: ", characters)
        )
    }

    const fetchUsers = () => {
        fetch("/users").then(
            response => response.json()
        ).then(
            data => {
                setUsers(data);
            }
        ).then(
            console.log("Users: ", users)
        )
    }

    return (
        <div>
            <h1>{users[0].name}</h1>
            <h2>{characters[0].name}</h2>
        </div>
    )
}

export default App;
