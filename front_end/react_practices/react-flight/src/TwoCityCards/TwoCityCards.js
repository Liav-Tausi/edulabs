import OneCityCard from "../OneCityCard/OneCityCard";
import "./TwoCityCards.css"

const TwoCityCards = ({citys}) => {
  return (
    <>
    <div className="two-city-card">
      <OneCityCard city={citys.origin}/>
      <img 
        className="arrow"
        alt="arrow"
        src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Arrow_east.svg/2560px-Arrow_east.svg.png"
      />
      <OneCityCard city={citys.destination}/>
      </div>
      <div className="container">
      <img 
        className="seat" 
        alt="airplane seat" 
        src="https://static.thenounproject.com/png/51086-200.png"
      />
      {        
        citys.seats_left >= 20
      ?
        <p className="green">Seats left {citys.seats_left}</p>
      : 
        citys.seats_left < 20 && citys.seats_left  >=8 
      ?
        <p className="yellow">Seats left {citys.seats_left}</p>
      :
        citys.seats_left < 8 && citys.seats_left  >=0 
      ?
        <p className="red">Seats left {citys.seats_left}</p>
      :
        <p> No Seats left </p>
      }
    </div>
    </>
  );
}

export default TwoCityCards;