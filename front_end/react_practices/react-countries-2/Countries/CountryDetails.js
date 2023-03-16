import axios from "axios"
import { useEffect, useState } from "react"
import { useLocation, useParams } from "react-router-dom"

export default function CountryDetails() {

    const [loading, setLoading] = useState(false)

    const urlParams = useParams()
    console.log(urlParams)

    const location = useLocation()


    const [countryData, setCountryData] = useState(null)

    const sendRequest = (country) => {
        setLoading(true)
        axios.get(`https://restcountries.com/v3.1/name/${country}`)
        .then((responseData) => {
            setCountryData(responseData.data[0])
            setLoading(false)
        })
    }

    useEffect(() => {
        sendRequest(urlParams.countryId)
    }, [urlParams.countryId])

    useEffect(() => {
        if (! location.search) {
            return
        }
        console.log('changes location.search', location.search)
        const country = location.search.replace("?", "").split("=")[1]
        sendRequest(country)
    }, [location.search])

    return(
        <>
            <h3>Details for country {urlParams.countryId}</h3>

            {loading &&
                <p>LOADING.....</p>
            }

            {!loading && countryData && 
                <p>Official name: {countryData.name.official}</p>    
            }
        </>

    )
    
}