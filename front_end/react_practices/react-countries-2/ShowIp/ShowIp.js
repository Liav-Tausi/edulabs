import axios from "axios"
import { useState } from "react"

const ShowIp = () => {
  const [ip, setIp] = useState('')


  const getIp = async () => {
    try {
      const responseOne = await
       axios("https://api.ipify.org/?format=json")
      if (responseOne.status === 200) {
        const responsetwo = await axios(
          `http://ip-api.com/json/${responseOne.data.ip}`
        );
        if (responsetwo.status === 200) {
          setIp(responsetwo.data.timezone);
        } else {
          throw responsetwo.statusText;
        }
      } else {
        throw responseOne.statusText;
      }
    } catch (error) {
      getIp('ERROR')
    }
  }

  return (
    <>
      <button onClick={getIp}>show ip</button>
      {ip !== '' && <div>{ip}</div>}
    </>
  );
}

export default ShowIp;