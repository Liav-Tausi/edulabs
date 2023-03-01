
import { flightData } from "./flightdata";
import TwoCityCards from "./TwoCityCards/TwoCityCards";
import "./App.css"


const React1 = () => {
  
  return (
    <>
      {flightData.map((element, index) => (
        <div className="outline">
          <div key={index}>
            {console.log(element)}
            <h1 className="head">Flight {element.flight_num}</h1>
            <TwoCityCards key={flightData.id} citys={element}/> 
          </div>
        </div>
      ))}
    </>
  );
}

export default React1;
