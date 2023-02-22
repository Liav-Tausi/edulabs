import "./OneCityCard.css"


const OneCityCard = ({city}) => {
  return (
    <div className="one-city-card">
      <h3 className="header">{city.city}, {city.country}</h3>
      <img className="pics" alt="city" src={city.img_url}/>
      <p>{city.time.toString()}</p>
    </div>
  );
}

export default OneCityCard;